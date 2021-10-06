import socket

ip = input("ip: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 50000))

try:
    while True:
        nachricht = input("msg: ")
        s.send(nachricht.encode())
finally:
    s.close()