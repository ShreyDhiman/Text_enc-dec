import socket

dec_key = input("Give the enc key  ")

if len(dec_key) == 41:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((socket.gethostname(), 3213))

    msg = s.recv(1000)

    msg = msg.decode("utf-8")
    
    val = dec_key[:: -1]
    dec = dict(zip(val , dec_key))

    msg = "".join([dec[words] for words in msg])

    print(msg)

else:
    print("not authorised")
    

