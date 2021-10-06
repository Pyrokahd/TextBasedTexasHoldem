# git remote add origin https://github.com/yourusername/your-repo-name.git

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
playerList = []
nicknames = []


def broadcast(message):
    """
    text message for all clients
    :param message: String, the message
    :return:
    """
    for client in clients:
        client.send(message.encode("ascii"))


def sendMessageToPlayer(player, message):
    """
    message to specific player
    :param player: socket from player
    :param message: String, the message
    :return:
    """
    player.send(message.encode("ascii"))
    return


def handleC(client):
    #print("handle client")
    while True:
        try:
            sendMessageToPlayer(client, "type !start to start the game")
            message = client.recv(1024)  # kein Decode => damit vorm senden nicht erneut encoded  #.decode("ascii")
            if message.decode("ascii") == "!start":
                playerList[clients.index(client)].isready = True  # player is ready (client and player array index correspond)
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
    """
    If a client connects it is saved in a list and handled via a handleC method in a new Thread
    :return:
    """
    # TODO nur so lange bis das spiel los geht
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

for i in range(3):
    playerList.append(Player())
# Create new Gamestate
gamestate = Gamestate(playerList)
gamestate.roundInitialization()



#printmoney(gamestate.playerList)

# !! LISTEN WERDEN ALS REFERENZEN BEHANDELT LISTE = LISTE1, dadurch verändert LISTE auch LISTE1
# Chanes in der Playerlist in GameState effects the Playerlist in PokerServer
print("")
print("deck test")
card = gamestate.deckmanager.drawCard()
gamestate.deckmanager.deck[1].printCardStats()

