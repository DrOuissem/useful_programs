import socket
buffer_size=1024
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_port=('127.0.0.1',1234)
s.bind(ip_port)

while True:
    message_bytes,address=s.recvfrom(buffer_size)
    message=message_bytes.decode()
    print("received from {} : {}".format(address,message))
    message="Hello I'm the server"
    message_bytes=message.encode()
    s.sendto(message_bytes,address)