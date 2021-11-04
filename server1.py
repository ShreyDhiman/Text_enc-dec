


import socket

msg = input("enter the message")

key = "abcdefghijklmnopqrstuvwxyz1234567890 !@#."
val = key[:: -1]

enc = dict(zip(key, val))

msg = "".join([enc[words] for words in msg.lower()])
print((msg))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 3213))

s.listen(5)

while True:
    clt, adr = s.accept()
    clt.send(bytes(msg, "utf-8"))