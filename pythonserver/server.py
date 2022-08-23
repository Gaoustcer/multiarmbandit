import socket

if __name__ == "__main__":
    serversocker = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serversocker.bind(("",8080))
    serversocker.listen(1024)
    while True:
        newclient ,ip = serversocker.accept()
        data = newclient.recv(1024)
        print("receive data",data,int(data))
        print("int data is",int(data))
        newclient.send('server info'.encode())