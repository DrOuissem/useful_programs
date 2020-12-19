import sqlite3
import socket

BUFFER_SIZE=1024

class Enrolled_DB:
    __slots__ = ['__name','__conn','__cursor']
    def __init__(self):
        self.create_database()

    def create_database(self):
        self.__name = 'EnrolledDB'
        self.__conn = sqlite3.connect(self.__name)
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute("CREATE TABLE IF NOT EXISTS EnrolledDB (FIRSTNAME TEXT, LASTNAME TEXT, AGE INTEGER, ID INTEGER PRIMARY KEY)")
        self.__conn.commit()

    def insert(self,list):
        assert(len(list)==4)
        # add a new book
        print('insert')
        request = '''INSERT INTO {} ('FIRSTNAME','LASTNAME','AGE','ID')
                                             VALUES('{}','{}','{}','{}')
                                             '''.format(self.__name,list[0], list[1], list[2], list[3])
        try:
            print("insert")
            print(request)
            self.__cursor.execute(request)
            self.__conn.commit()
            message = "SUCCESS"
            return message
        except Exception as e:
            print("error", e)
            message = "ERROR"
            return message



s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port=('127.0.0.1',1234)
s.bind(ip_port)
s.listen()

try:
    #CREATE THE DATABASE
    db=Enrolled_DB()
    print("I'm waiting for a connection")
    client_s,addr=s.accept()
    print('Connection address:', addr)
    while 1:
        data = client_s.recv(BUFFER_SIZE)
        list = data.decode().split("---")
        if not data or (len(list)==1 and list[0]=='quit') : break
        print("received data:", data.decode())

        if (len(list)==4):
            message=db.insert(list)
            client_s.send(message.encode())

        else:
            client_s.send("Error".encode())  # echo

except KeyboardInterrupt:
    print("error")
    exit()
finally:
    client_s.close()
    s.close()