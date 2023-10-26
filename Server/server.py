import sqlite3
from sqlite3 import Error
import socket
import os

USERTABLEID = 0
OWENERTABLEID = 1
DESIGNTABLEID = 2
CHUNKSIZE = 1024
def TransferFolder(conn,folderaddress):
    conn.sendall(folderaddress.split("\\")[-1].encode())
    for file in os.listdir(folderaddress):
        FullPath=folderaddress+"\\"+file
        fUploadFile = open(FullPath, "rb")
        filesize = os.path.getsize(FullPath)
        print(filesize)
        conn.sendall((file).encode() )
        conn.recv(1024)
        conn.sendall(str(filesize).encode())
        conn.recv(1024)
        while True:
            data = fUploadFile.read(CHUNKSIZE)
            if not data:
                break
            conn.sendall(data)
        conn.recv(1024)
    conn.send("##finish".encode())


def RecieveFolder(conn,designID):
    foldername = conn.recv(CHUNKSIZE).decode()
    if not os.path.exists(os.getcwd() + "\\{}\\".format(str(designID)) + foldername):
        os.makedirs(os.getcwd() + "\\{}\\".format(str(designID)) + foldername)
    folderPath = os.getcwd() + "\\{}\\".format(str(designID)) + foldername
    while True:
        data = conn.recv(CHUNKSIZE).decode()
        if data == "##finish": break
        FileName = data
        conn.sendall("recieve".encode())
        FileSize = int(conn.recv(CHUNKSIZE).decode())
        print(FileSize)
        conn.sendall("recieve".encode())
        path = folderPath + "\\" + FileName
        os.makedirs(os.path.dirname(path), exist_ok=True)
        f = open(path, 'wb')

        while FileSize > 0:
            Length = min(FileSize, CHUNKSIZE)
            data = conn.recv(Length)
            if not data:
                break
            f.write(data)
            FileSize -= Length
        conn.sendall("recieve".encode())
    return folderPath





def create_connection(path):
    connection = None
    try:

        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

print(os.getcwd()+"\\SQL.sqlite")
connection=create_connection(os.getcwd()+"\\SQL.sqlite")

connection.execute("PRAGMA foreign_keys = ON;")
connection.commit()
sql_text_1 = """CREATE TABLE IF NOT EXISTS User
           (FirstName TEXT NOT NULL,
            SurName TEXT NOT NULL,
            Password TEXT NOT NULL,
            Gender TEXT NOT NULL,
            UserID NUMBER NOT NULL PRIMARY KEY);"""
cursor=connection.cursor()
cursor.execute(sql_text_1)
cursor.execute("""
            CREATE TABLE IF NOT EXISTS OwnerShip(
           UserID NUMBER NOT NULL,
           DesignID NUMBER NOT NULL,
           FOREIGN KEY (UserID) REFERENCES User(UserID),
           FOREIGN KEY (DesignID) REFERENCES Design(DesignID)
           );""")

sql_text_1="""
            CREATE TABLE IF NOT EXISTS Design
           (DesignID NUMBER NOT NULL PRIMARY KEY,
           Address TEXT NOT NULL,
           DesignName TEXT NOT NULL
           );"""

cursor.execute(sql_text_1)

handle=open("Index.txt")
INDEX=handle.read().split("#")
USERID=int(INDEX[0])
DESIGNID=int(INDEX[1])
handle.close()
cursor.execute( "SELECT DesignName,Design.DesignID FROM Design,OwnerShip WHERE OwnerShip.UserID={} AND Design.DesignID=OwnerShip.DesignID".format("1"))
rows = cursor.fetchall()
print(rows)

ip_port = ('127.0.0.1', 9999)

sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sk.bind(ip_port)

sk.listen(5)

print('Waiting for client connection')
while True:
    conn, address = sk.accept()
    try:
        while True:
            client_data = conn.recv(1024).decode()
            if client_data == "register":
                while True:
                    conn.sendall("recieve".encode())
                    client_data = conn.recv(1024).decode()
                    Firstname=client_data
                    conn.sendall("recieve".encode())
                    client_data = conn.recv(1024).decode()
                    Surname = client_data
                    conn.sendall("recieve".encode())
                    client_data = conn.recv(1024).decode()
                    Gender = client_data
                    conn.sendall("recieve".encode())
                    client_data = conn.recv(1024).decode()
                    password = client_data
                    if(Surname!="")and(Firstname!=""):
                        conn.sendall("True".encode())
                        client_data = conn.recv(1024).decode()
                        if client_data=="recieved":
                            cursor.execute("INSERT INTO User VALUES('{}','{}','{}','{}','{}')".format(Firstname,Surname,password,Gender,USERID))
                            conn.sendall(str(USERID).encode())
                            USERID+=1
                            break
                    else:
                        conn.sendall("False".encode())
            elif client_data =="add design":
                conn.sendall("recieve".encode())
                name=conn.recv(1024).decode()
                conn.sendall("recieve".encode())
                RecieveFolder(conn,DESIGNID)
                cursor.execute("INSERT INTO Design VALUES('{}','{}','{}')".format(str(DESIGNID),os.getcwd() + '\\{}\\{}'.format(str(DESIGNID),name),name))#store in designID so that design with the same name won't be colided
                conn.sendall(str(DESIGNID).encode())
                DESIGNID+=1
            elif client_data=="add ownership":
                conn.sendall("recieve".encode())
                DesignID= conn.recv(1024).decode()
                conn.sendall("recieve".encode())
                Try = 3
                while Try > 0:
                    client_data = conn.recv(1024).decode()
                    UserID = client_data
                    client_data = conn.recv(1024).decode()
                    Password = client_data
                    cursor.execute("SELECT Password FROM User WHERE User.UserID={}".format(UserID))
                    rows = cursor.fetchall()
                    if len(rows) == 0:
                        break
                    if rows[0][0] == Password:
                        conn.sendall("True".encode())
                        cursor.execute("SELECT UserID FROM OwnerShip WHERE OwnerShip.DesignID = {}".format (DesignID))
                        ID = cursor.fetchall()
                        BCase=True
                        if len(ID)>0:
                            for i in range(len(ID)):
                                if ID[i][0]==UserID: BCase=False
                        if BCase:
                            cursor.execute("INSERT INTO OwnerShip VALUES('{}','{}')".format(UserID,DesignID))
                            break

                    else:
                        conn.sendall("False##".encode())

                conn.close()
                break

            elif client_data =="log in":
                Try=3
                while Try>0:
                    client_data = conn.recv(1024).decode()
                    UserID=client_data
                    client_data = conn.recv(1024).decode()
                    Password = client_data
                    cursor.execute("SELECT Password FROM User WHERE User.UserID={}".format(UserID))
                    rows = cursor.fetchall()
                    if len(rows)==0:
                        break
                    if rows[0][0]==Password:
                        conn.sendall("True".encode())
                        client_data = conn.recv(1024).decode()
                        if (client_data == "exit"):
                            break
                        cursor.execute(
                            "SELECT DesignName,Design.DesignID FROM Design,OwnerShip WHERE OwnerShip.UserID={} AND Design.DesignID=OwnerShip.DesignID".format(
                                UserID))
                        rows = cursor.fetchall()
                        for i in rows:
                            conn.recv(1024)
                            conn.sendall(i[0].encode())
                        conn.sendall("finish".encode())
                        conn.recv(1024).decode()
                        client_data = conn.recv(1024).decode()
                        if (client_data == "Wrong"):
                            break
                        else:
                            index = int(client_data)
                            if (index >= len(rows)):
                                conn.sendall("out of range".encode())
                            else:

                                conn.sendall("Right".encode())
                                cursor.execute(
                                    "SELECT Address FROM Design WHERE DesignID={}".format(
                                        rows[index][1]))

                                Address = cursor.fetchall()

                                TransferFolder(conn,Address[0][0])
                                print("finish")
                                break


                    else:
                        conn.sendall("False##".encode())

                conn.close()
                break
            conn.close()
            break

    except:
        handle = open("Index.txt", "w")
        handle.write("{}#{}".format(str(USERID), str(DESIGNID)))
        handle.close()
        connection.commit()








