import socketserver

X = 99
logList = []


class GameData():
    def __init__(self):
        self.__pCount = 0
        self.playerDict = {}
    def get_pCount(self):
        return self.__pCount
    def set_pCount(self, count):
        self.__pCount = count
    def increase_pCount(self):
        self.__pCount += 1

class ChatRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.GameData = self.server.MyDataControllers

        self.GameData.increase_pCount()
        print(self.GameData.get_pCount())

        # Save Socket und Player zuweisen
        self.GameData.playerDict["player"+str(self.GameData.get_pCount())] = self.request

        addr = self.client_address[0]
        print("[{}] Verbindung hergestellt".format(addr))

        while True:
            msg = self.request.recv(1024)  # request is der Client

            if msg:
                logList.append(msg.decode())
                print("[{}] {}".format(addr, msg.decode()))

                if msg.decode() == str(X):
                    print("send answer:")
                    answer = ""
                    for word in logList:
                        answer = answer + "\n" + word
                    self.request.send(str(X).encode())  # no encode() for ints   https://stackoverflow.com/questions/33913308/socket-module-how-to-send-integer
            else:
                print("[{}] Verbindung geschlossen".format(addr))
                break


# TheadingTCPServer Overriden class to include a custom data Object in the constructor (myDataControllers)
class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    def __init__(self, host_port_tuple, streamhandler, myDataControllers):
        super().__init__(host_port_tuple, streamhandler)
        self.MyDataControllers = myDataControllers

    ##  server = socketserver.ThreadingTCPServer(("", 50000), ChatRequestHandler, "TEST")

# Create the custom TCPServer with the GameData class as custom Data
myGameData = GameData()
server = ThreadingTCPServer(("", 50000), ChatRequestHandler, myGameData)  # "" = any adress, socket.gethostname = global, else local
try:
    print("server started")
    server.serve_forever()
finally:
    server.server_close()

print("Test helo")