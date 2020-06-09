import socket
buffer_size=1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_port=('127.0.0.1',1234)
s.connect(ip_port)
print("client address:" ,s.getsockname())
print("server address:",s.getpeername())
message="Hello I'm the client".encode('utf-8')

s.send(message)
message=s.recv(buffer_size).decode('utf-8')
print("received message:",message)
s.close()