import sqlite3
import socket
import threading

HEADER_LENGTH=1024
class MyThread (threading.Thread):
    def __init__(self,client):
        threading.Thread.__init__(self)
        self.client = client
        self.start()



    def run(self):
        self.conn = sqlite3.connect("books.db")
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS Books (TITLE TEXT, AUTHOR TEXT, RELEASE INTEGER, PRICE INTEGER)")
        self.conn.commit()
        label_text = ["Title", "Author", "Release", "Price"]
        try:
            while True:
                message = self.client.recv(HEADER_LENGTH).decode()
                print ("received: ",message)
                 #insert
                # --- used as delimiter
                list=message.split("---")
                if len(list)==2:
                    #search and return the result
                    request = "SELECT * FROM Books WHERE " + list[0] + "='" + list[1] + "'"
                    try:
                        self.c.execute(request)
                        results = self.c.fetchall()
                        if len(results) == 0:
                            message = "no books in the table".encode()
                            self.client.send(message)
                        else:
                            message=''
                            for row in results:
                                for x in range(4):
                                    message = message + "{}  :  {}     ".format(label_text[x], row[x])
                                message = message + "\n"
                            self.client.send(message.encode())
                    except Exception as e:
                        print("error",e)

                elif len(list)==4:
                    #add a new book
                    print('insert')
                    request = '''INSERT INTO Books ('TITLE','AUTHOR','RELEASE','PRICE')
                                     VALUES('{}','{}','{}','{}')
                                     '''.format(list[0], list[1], list[2], list[3])
                    try:
                        print("insert")
                        print(request)
                        self.c.execute(request)
                        self.conn.commit()
                        message = "new book added successfully".encode()
                        self.client.send(message)
                    except Exception as e:
                        print("error", e)
                        message = "Error".encode()
                        self.client.send(message)
                else:
                    print("error")
        except:
            print("error")
        finally:
            self.client.close()
            exit()


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port=('127.0.0.1',1234)
s.bind(ip_port)
s.listen()
try:
    while True:
        print("I'm waiting for a connection")
        client_s,add=s.accept()
        th=MyThread(client_s)

except KeyboardInterrupt:
    print("error")
    exit()
finally:
    client_s.close()
    s.close()