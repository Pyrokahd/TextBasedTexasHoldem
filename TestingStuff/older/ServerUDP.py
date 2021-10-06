import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # INET = IPv4, DGRAM = UDP
try:
    s.bind(("", 50000))  # keine Adresse = Alle auch localhost
    while True:
        daten, addr = s.recvfrom(1024)  # maximale Paketgröße 1024 it
        print("[{}] {}".format(addr[0], daten.decode()))
finally:
    s.close()