import socket
s = socket.socket()
port = 8000
ip = '127.0.0.1' #IP کامپیوتر سرور
s.connect((ip, port))
print('Connected')
while True:
    print(s.recv(1024).decode())
    message = input('Your Message : ')
    s.send(message.encode())