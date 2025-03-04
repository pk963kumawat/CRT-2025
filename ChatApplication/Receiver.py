import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_add = "127.0.0.1"
port = 1234
complete = (ip_add,port)
s.bind(complete)
while True:
    message=s.recvfrom(1024)
    print(message[0].decode('ascii'))

