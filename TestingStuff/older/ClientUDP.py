import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = input("IP-Adresse: ")
nachricht = input("Nachricht: ")
s.sendto(nachricht.encode(), (ip, 50000))
s.close()