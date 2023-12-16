import socket


server=socket.socket()
print("socket created")
server.bind(('localhost',12000))

server.listen()
print("Server listening at 12000")


while True:
    print("waiting for apllication")
    client,address=server.accept()
    print("connection established")
    server.send(bytes('Hello Client','utf-8'))
    recData=server.recv(1024).decode( )
    print("Client:",recData)
