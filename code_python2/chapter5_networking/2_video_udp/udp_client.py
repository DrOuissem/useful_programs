import socket
buffer_size=1024
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

message="Hello I'm the client"
message_bytes=str.encode(message)

address_server=('127.0.0.1',1234)
s.sendto(message_bytes,address_server)
message_bytes,address=s.recvfrom(buffer_size)
message=message_bytes.decode()
print("received from {} : {}".format(address,message))

