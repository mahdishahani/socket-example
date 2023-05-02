import socket
s = socket.socket()
port = 8000
ip = '127.0.0.1'
s.bind((ip, port))
s.listen()
c, addr = s.accept()
print('Connected')
while True:
    message = input('Your Message : ')
    c.send(message.encode())
    print(c.recv(1024).decode())