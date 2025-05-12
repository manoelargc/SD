import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)  # REP = Reply
socket.bind("tcp://*:5555")

print("Servidor pronto. Aguardando mensagens...")

while True:
    message = socket.recv_string()
    print(f"Recebido do cliente: {message}")
    socket.send_string(f"Resposta recebida: {message}")
