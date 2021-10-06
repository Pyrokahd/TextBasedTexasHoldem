import socket
import select  # ready = select.select(s, [], [], 5)  # 5 sec timeout  # als idee  https://stackoverflow.com/questions/2719017/how-to-set-timeout-on-pythons-socket-recv-method

ip = input("IP_Adresse: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket erstellen und dann verbinden
s.connect((ip, 50000))
s.settimeout(5)
s.setblocking(False)
try:
    while True:
        nachricht = input("Nachricht: ")
        s.send(nachricht.encode())

        try:
            antwort = s.recv(1024)  # antwort vom server erhalten (max 1024 bit)
            print("[{}] {}".format(ip, antwort.decode()))
        except:
            print("no data recieved")

finally:
    s.close()
