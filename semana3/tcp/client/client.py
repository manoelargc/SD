import time
from socket import *

time.sleep(2)

while True:
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('server-service', 12345))  # nome correto do service
        s.send(b'Hello, world')
        data = s.recv(1024)
        print("Resposta do servidor:", data)
        s.close()
        time.sleep(3)
    except Exception as e:
        print("Erro ao conectar no servidor:", e)
        time.sleep(3)
