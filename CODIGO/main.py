from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

# Definindo o diretório raiz como "public"
os.chdir('./public')

# Definindo a classe do manipulador de requisições
class CustomHandler(SimpleHTTPRequestHandler):
    # Sobrescrevendo o método para servir arquivos estáticos
    def do_GET(self):
        # Rotas
        if self.path == '/':
            self.path = '/home.html'
        elif self.path == '/curiosidades':
            self.path = '/curiosidades.html'
        elif self.path == '/sobre':
            self.path = '/sobre.html'
        return SimpleHTTPRequestHandler.do_GET(self)

# Configurando o endereço IP e a porta
host = 'localhost'
port = 8000

# Configurando o servidor com o diretório raiz definido e o manipulador personalizado
server_address = (host, port)
httpd = HTTPServer(server_address, CustomHandler)

# Adicionando mensagem de inicialização
print(f'SERVIDOR RODANDO EM http://{host}:{port}/')

# Iniciando o servidor
httpd.serve_forever()
