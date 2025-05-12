import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REQ)

# Aguarda servidor estar disponível
while True:
    try:
        socket.connect("tcp://servidor:5555")
        break
    except Exception:
        print("Tentando se conectar ao servidor...")
        time.sleep(1)

mensagem = "Olá servidor!"
print(f"Enviando: {mensagem}")
socket.send_string(mensagem)

resposta = socket.recv_string()
print(f"Resposta do servidor: {resposta}")
