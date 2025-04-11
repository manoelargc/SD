from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 12345))
s.listen(1)
# print('Server is listening...')

(conn, addr) = s.accept()  # retorna novo socket e endereço do cliente
while True:
    print('Server is listening...')
    data = conn.recv(1024)  # recebe dados do cliente
    if not data:
        break  # encerra se o cliente parar
    conn.send(str(data).encode() + b"*")  # devolve os dados com um "*"
conn.close()
