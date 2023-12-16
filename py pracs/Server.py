import socket

s=socket.socket()
print("socket created")

s.bind(('localhost',9999))

s.listen(3)
print('waiting for connections')

while True:
    name=c.recv(1024).decode()
    c,addr=s.accept()
    print("Connected with",addr)
   
    c.send(bytes("welcome to Telusko",'utf-8'))
    c.close()
