import time
from socket import *

time.sleep(2) 
s = socket(AF_INET, SOCK_STREAM)
s.connect(('server', 12345))  # <--- use o nome do serviço, NÃO localhost!

s.send(b'Hello, world')
data = s.recv(1024)
print("Resposta do servidor:", data)

s.close()
