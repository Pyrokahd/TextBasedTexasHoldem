import socket
import threading

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 49999))


def recieve():
    #print("recieve client")
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "NICK":
                client.send(nickname.encode("ascii"))
            else:
                print(message)
        except:
            print("error! disconnecting")
            client.close()
            break


def write():
    while True:
        message = input()
        messageToSend = f"{nickname}: " + message
        client.send(messageToSend.encode("ascii"))


recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

