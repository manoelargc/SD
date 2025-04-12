from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 12345))
s.listen(5)

print('Servidor aguardando conexões...')

while True:
    conn, addr = s.accept()
    print(f'Conexão recebida de {addr}')
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data + b'*')  # devolve os dados com um "*"
    conn.close()
