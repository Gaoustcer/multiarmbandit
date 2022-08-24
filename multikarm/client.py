import socket
if __name__ == "__main__":
    clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientsocket.connect(('127.0.0.1',8080))
    clientsocket.send("Knum".encode())
    # print(obj)
    # while True:
    #     pass
    clientsocket.close()
