import socket
buffer_size=1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port=('127.0.0.1',1234)
s.bind(ip_port)

try:
    while True:
        print("I'm waiting for a connection")
        client_s,add=s.accept()
        message=client_s.recv(buffer_size).decode('utf-8')
        print("received message:",message)
        message="Hello I'm the server".encode('utf-8')
        client_s.send(message)
except KeyboardInterrupt:
    print("error")
finally:
    client_s.close()
    s.close()
