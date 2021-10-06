import selectors
import socket

import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", 50000))
server.setblocking(False)
server.listen(1)

###
potential_readers = []
potential_writers = []
potential_errs = []
timeout = 0
ready_to_read, ready_to_write, in_error = select.select(potential_readers, potential_writers, potential_errs, timeout)
###


def acceptFunc(selector, server):
    #print("accept Part")
    client, addr = server.accept()
    client.setblocking(False)
    selector.register(client, selectors.EVENT_READ, messageFunc)


selector = selectors.DefaultSelector()
selector.register(server, selectors.EVENT_READ, acceptFunc)


def messageFunc(selector, client):
    #print("message part")
    nachricht = client.recv(1024)
    ip = client.getpeername()[0]
    if nachricht:
        print(nachricht.decode())
    else:
        print("end connection")
        selector.unregister(client)
        client.close()





while True:
    for key, mask in selector.select():
        key.data(selector, key.fileobj)