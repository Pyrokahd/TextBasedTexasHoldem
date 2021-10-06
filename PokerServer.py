import random
import threading
import socket
from GameState import Gamestate
from playerData import Player

host = "127.0.0.1"  # Adresse vom Server wo dieser Code läuft #global also die router IP?
port = 49999  # Port vom Server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Ipv4 und TCP
server.bind((host, port))  # Server an das socket mit host und port binden
server.listen()  # start listening

clients = []
nicknames = []


def broadcast(message):
    """ text message for all clients """
    for client in clients:
        client.send(message)


def sendMessageToPlayer(Player):
    # Todo send to right client/socket based on player from gamestateplayerList
    return


def handleC(client):
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
            nicknames.remove(nickname)


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
        client.send("you connected to server".encode("ascii"))

        thread = threading.Thread(target=handleC, args=(client,))
        thread.start()


# TODO main function to start GameStat Init
def printmoney(list):
    fstring = ""
    for item in list:
        fstring += f" [{item.money}] "
    print(fstring)


# Testing Blinds
# Create Testplayer
playList = []
for i in range(3):
    playList.append(Player())
# Create new Gamestate
gamestate = Gamestate(playList)
gamestate.roundInitialization()

#printmoney(gamestate.playerList)

# !! LISTEN WERDEN ALS REFERENZEN BEHANDELT LISTE = LISTE1, dadurch verändert LISTE auch LISTE1
print("")
print("deck test")
card = gamestate.deckmanager.drawCard()
gamestate.deck[1].printCardStats()

