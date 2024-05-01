import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import os 

workbook = openpyxl.load_workbook('clientes.xlsx')
pagina_clientes = workbook['Página1']

for linha in pagina_clientes.iter_rows(min_row=2):
    nome = linha[0].value  
    telefone = str(int(linha[1].value))
    vencimento = linha[2].value
    mensagem_personalizada = linha[3].value  
    
    print(f"Enviando mensagem para {nome} ({telefone}) com vencimento em {vencimento.strftime('%d/%m/%Y')}...")
    
    mensagem = f'Olá {nome}, {mensagem_personalizada}. Favor pagar até o dia {vencimento.strftime('%d/%m/%Y')} no link https://www.link_do_pagamento.com'

    # Criar link personalizado do WhatsApp e enviar mensagem
    try:
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        webbrowser.open(link_mensagem_whatsapp)
        sleep(20)  # Tempo suficiente para carregar a página
        seta = pyautogui.locateCenterOnScreen('seta.png', confidence=0.9)  # Ajuste a confiança conforme necessário
        if seta:
            pyautogui.click(seta[0], seta[1])
            sleep(5)  # Tempo para voltar à lista de chats
            pyautogui.hotkey('ctrl', 'w')  # Fecha a aba do WhatsApp Web
        else:
            print(f"Não foi possível localizar a seta para voltar à lista de chats para {nome}.")
            with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
                arquivo.write(f'{nome},{telefone}\n')
    except Exception as e:
        print(f'Não foi possível enviar mensagem para {nome}: {str(e)}')
        with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{telefone}\n')
    
print("Mensagens enviadas para todos os clientes.")
