import socket
import threading

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ipsys = "localhost"
portrec = 5000

s.bind((ipsys, portrec))

def sender():
    while True:
        text = input("\nEnter the text:")
        s.sendto(text.encode(), (ipsys, portrec))
        print("")   

def reciever():
    while True:
        x = s.recvfrom(1024)
        print("\nMessage from client: " + x[0].decode())
        
t1 = threading.Thread(target=reciever)
t2 = threading.Thread(target=sender)

t1.start()
t2.start()
