import socket
import threading
class RecvSendThread(threading.Thread):
    connected_clients={}
    def __init__(self,username,client):
        threading.Thread.__init__(self)
        self.username=username
        self.client=client
        RecvSendThread.connected_clients[username]=client
        self.send_new_list()
        self.start()
    def send_new_list(self):
        message="__updateList__"
        for key in RecvSendThread.connected_clients:
            message+=" "+key
        for key in RecvSendThread.connected_clients:
            RecvSendThread.connected_clients[key].send(message.encode())
    def run(self):
        while True:
            message = self.client.recv(buffer_size).decode()
            if message == "__stop__":
                self.client.close()
                del (RecvSendThread.connected_clients[self.username])
                self.send_new_list()
                break
            else:
                new_message = self.username+": "+message
                for x in RecvSendThread.connected_clients.keys():
                    if x!=self.username:
                        RecvSendThread.connected_clients[x].send(new_message.encode())



IP="127.0.0.1"
PORT=1234
buffer_size=1024
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((IP,PORT))
try:
    server_socket.listen()
    while True:
        client_socket, client_address=server_socket.accept()
        user_name=client_socket.recv(buffer_size).decode()
        RecvSendThread(user_name,client_socket)
except:
    print("there is an error")
    exit()