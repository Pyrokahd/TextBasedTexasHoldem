import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Stream = TCP
s.bind(("", 50000))
s.listen(4)  # maximale zu puffernde Verbindungsversuche
def serverEinThread():
    try:
        while True:
            komm, addr = s.accept()  # komm = socket vom client und addr die adresse
            while True:
                data = komm.recv(1024)  # Nachricht erwarten
                if not data:  # leerer String ? => Verbindung abbgebrochen socket schließen
                    komm.close()
                    break
                print("[{}] {}".format(addr[0], data.decode()))  # Nachricht Anzeigen vom client
                nachricht = input("Antwort: ")  # Antwort eingeben
                komm.send(nachricht.encode())  # antwort zum client senden
    finally:
        s.close()
#serverEinThread()
## Multithread
#  1. class X(theading.Thread)
#  2. __init__ und super().__init__()
#  3. override run(self)
#  4. Threads speichern in list []
#  5. Threads starten in while loop mit try and except
#  (optional) loop over threads in list mit t.join() um darauf zu warten dass alle beendet werden
class ServerThreat(threading.Thread):
    def __init__(self, komm, addr):
        super().__init__()
        self.komm = komm
        self.addr = addr
        self.messages = ["Test"]
    def run(self):
        # todo listen for shit 1 socket oder mehrere?
        try:
            while True:
                data = self.komm.recv(1024)  # Nachricht erwarten
                if not data:  # leerer String ? => Verbindung abbgebrochen socket schließen
                    self.komm.close()
                    break
                print("[{}] {}".format(self.addr[0], data.decode()))  # Nachricht Anzeigen vom client
                # nachricht = "automated answer" #  = input("Antwort: ")  # Antwort eingeben
                self.messages.append(data)
                for item in self.messages:
                    komm.send(item.encode())  # antwort zum client senden
                self.messages = []
        finally:
            s.close()

myTheads = []
#thread = ServerThreat
# append
#thread.start()
try:
    while True:
        komm, addr = s.accept()  # komm = socket vom client und addr die adresse
        #dann neuer thread
        newThread = ServerThreat(komm, addr)
        myTheads.append(newThread)
        newThread.start()
finally:
    s.close()