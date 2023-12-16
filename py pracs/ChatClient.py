import socket 

client=socket.socket()
client.connect(('localhost',12000))
print("connected to server")


    
while True:
    recData=client.recv(1024).decode()
    print(recData)
    client.send(bytes("hello server",'utf-8'))
    print("Data Sent")


