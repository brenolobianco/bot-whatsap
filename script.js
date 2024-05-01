const http = require('http');
const { exec } = require('child_process');

const server = http.createServer((req, res) => {
    res.setHeader('Content-Type', 'text/plain');

    if (req.url === '/executarPython' && req.method === 'POST') {
        // Executa o script Python
        exec('app.py', (error, stdout, stderr) => {
            if (error) {
                res.statusCode = 500;
                res.end(`Erro ao executar o script Python: ${error}`);
                return;
            }
            res.end(`Script Python executado: ${stdout}`);
        });
    } else {
        res.statusCode = 404;
        res.end('Página não encontrada');
    }
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Servidor Node.js rodando em http://localhost:${PORT}`);
});
