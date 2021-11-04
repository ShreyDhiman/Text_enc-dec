import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 3213))

msg = s.recv(1000)

msg = msg.decode("utf-8")
    
print(msg)