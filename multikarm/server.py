import socket
from numpy.random import normal
from random import random
if __name__ == "__main__":
    serversocker = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serversocker.bind(("",8080))
    serversocker.listen(1024)
    K = 1024
    sigmalist = []
    mulist = []
    for _ in range(K):
        sigmalist.append(random())
        mulist.append(random())
    while True:
        newclient ,ip = serversocker.accept()
        data = newclient.recv(1024)
        print("receive data is",data)
        data = str(data,encoding='utf-8')
        print("data is",data)
        if data == "Knum":
            serversocker.send(str(K).encode())
            print("Send Knum is",K)