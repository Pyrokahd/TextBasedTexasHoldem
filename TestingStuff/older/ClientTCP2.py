import socket
ip = input("IP_Adresse: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket erstellen und dann verbinden
s.connect((ip, 50000))
try:
    while True:
        nachricht = input("Nachricht: ")
        s.send(nachricht.encode())
        antwort = s.recv(1024)  # antwort vom server erhalten (max 1024 bit)
        print("[{}] {}".format(ip, antwort.decode()))
finally:
    s.close()
