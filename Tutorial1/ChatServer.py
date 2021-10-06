import threading
import socket

host = "127.0.0.1"  # Adresse vom Server wo dieser Code läuft #global also die router IP?
port = 49999  # Port vom Server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Ipv4 und TCP
server.bind((host, port))  # Server an das socket mit host und port binden
server.listen()  # start listening

clients = []
nicknames = []


# Message to all clients
def broadcast(message):
    for client in clients:
        client.send(message)


# Endless loop for each client mit disconnect on except
def handleC(client):#
    #print("handle client")
    while True:
        try:
            message = client.recv(1024)  # kein Decode => damit vorm senden nicht erneut encoded  #.decode("ascii")
            broadcast(message)
        except:
            print("Fehler bei Client")
            # disconnect client and remove from list
            index = clients.index(client)  # index vom client in der liste
            clients.remove(client)
            client.close()
            # nickname entfernen
            nickname = nicknames[index]
            broadcast(f"{nickname} left chat!".encode("ascii"))
            nicknames.remove(nickname)


#  what happens when a client connects and how he connects
def recieveC():
    while True:
        # accept connections
        client, adress = server.accept()
        print(f"connected with {str(adress)}")

        client.send("NICK".encode("ascii"))  # send keyword NICK which the client will react on
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of client is {nickname}")
        broadcast(f"{nickname} joined chat".encode("ascii"))
        client.send("you connected to server".encode("ascii"))

        thread = threading.Thread(target=handleC, args=(client,))
        thread.start()

print("server started: ")
recieveC()