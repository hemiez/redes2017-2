#responsável por receber os comandos de webserver.py, executar e responder



import socket
import sys

# cria socket para conexo tcp

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conecta no servidor
host = 192.168.56.101
porta = 8000
servidor = (host, porta)
print >>sys.stderr, 'conectando...' 
sock.connect(servidor)
try:
    
        dados = sock.recv(1024)
        print >>sys.stderr, 'recebeu "%s"' % dados

finally:
    print >>sys.stderr, 'fim da conexao'
    sock.close()
