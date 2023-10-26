import tkinter
from tkinter import filedialog
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from SearchingColor import Color
from Class import*
import shutil
import socket
IMAGETYPE=[("IMAGE",".gif .jpg .png")]#for the root of files dependent on the type
TEXTFILETYPE=[("Text",".txt")]
VIDEOFILETYPE=[("VIDEO",".mp4")]
AUDIOFILETYPE=[("AUDIO",".mp3")]
IMAGEINDEX=0
TEXTFILEINDEX=1
VIDEOINDEX=2
AUDIOINDEX=3
CHUNKSIZE=1024
global NAME
NAME=''

def Warning(str):#for warning window
    error_dialog = QtWidgets.QErrorMessage()
    error_dialog.showMessage(str)
    error_dialog.exec_()

def Information(str):#for information window
    information_dialog=QtWidgets.QMessageBox()
    information_dialog.setText(str)
    information_dialog.show()
    information_dialog.exec_()


def partition(arr,value, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[value[high]]  # pivot

    for j in range(low, high):
        if arr[value[j]] <= pivot:
            i = i + 1
            value[i], value[j] = value[j], value[i]

    value[i + 1], value[high] = value[high], value[i + 1]
    return (i + 1)

def quickSort(arr,value, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr,value, low, high)
        quickSort(arr,value, low, pi - 1)
        quickSort(arr,value, pi + 1, high)

def HtmlCoding(Text,Buttonlist):
    New = ''
    length = len(Text)
    if length==0:
        return ''
    list=Buttonlist#<b><i>i</i><i>i</i></b>
    Statelist = [[], [], [], [], [], [], []]#store the indexs of two ends of the range of continuous chars having one tap
    TapList = ["<b>", "<i>", "<mark>", "<small>", "<sub>", "<sup>", "<del>"]
    for i in range(length):
        if (i == 0):
            for z in range(7):
                if list[0][z]:#if the first char have a tap on z add 0 to statelist[z]
                    Statelist[z].append(0)
        elif (i == length - 1):
            for z in range(7):
                if list[i][z]:#if the last char have a tap on z add the last index as the end of the range of continuous chars having one tap
                    Statelist[z].append(i)
        else:
            for z in range(7):
                if list[i][z] != list[i + 1][z]:#if the tap state is changed, then add this index in the statelist
                    if list[i][z]:
                        Statelist[z].append(i)
                    else:
                        Statelist[z].append(i + 1)
    # &lt;&gt;
    LastList = [0, 0, 0, 0, 0, 0, 0]#have the index of last end of each taps
    NextList = [0, 0, 0, 0, 0, 0, 0]#have the index of next end of each taps
    for i in range(length):
        Left = []#have all the indexs of tap where a range of continuous char stops
        Right = []#have all the indexs of tap where a range of continuous char stops
        for z in range(7):
            if (len(Statelist[z]) >= 1 and Statelist[z][0] == i):

                if (len(Statelist[z]) % 2):#if length of statelist is odd, then the first index in statelist is the end of some thing so that add index in right
                    Right.append(z)
                else:#if length of statelist is even, then the first index in statelist is the start of some thing so that add index in left
                    Left.append(z)
                    NextList[z] = Statelist[z][1]
                    LastList[z] = i
                    if (Statelist[z][1] == Statelist[z][0]):
                        Right.append(z)
        quickSort(LastList, Right,0,len(Right)-1)#range them by the priority of starting index of this range of continuous chars having the same tap attributes

        quickSort(NextList, Left,0,len(Left)-1)#range them by the priority of ending index of this range of continuous chars having the same tap attributes

        for k in Left:
            New = New + TapList[k]
            LastList[k] = Statelist[k].pop(0)
        char = Text[i]
        if char == "<":
            New = New + "&lt;"
        elif char == ">":
            New = New + "&gt;"
        elif char == "\n":
            New = New + "<br>"
        else:
            New = New + char
        for k in range(len(Right) - 1, -1, -1):
            New = New + TapList[Right[k]][0] + "/" + TapList[Right[k]][1:]
            Statelist[Right[k]].pop(0)
    return (New)
def addLink(Class,link):
    if(Class.node.link.File=="default"):
        Class.node.link=link
        Class.node.coding='<a href="{}">'.format(link.text)+Class.node.coding+'</a>'

def searching(index,name):#searching files
    root = tkinter.Tk()
    root.withdraw()  # use to hide tkinter window

    currdir = os.getcwd()
    if index==IMAGEINDEX:
        tempdir = filedialog.askopenfilename(parent=root,filetypes=IMAGETYPE,  initialdir=currdir,title='Please select a directory')
    elif index==AUDIOINDEX:
        tempdir = filedialog.askopenfilename(parent=root, filetypes=AUDIOFILETYPE, initialdir=currdir,
                                             title='Please select a directory')
    elif index==TEXTFILEINDEX:
        tempdir = filedialog.askopenfilename(parent=root, filetypes=TEXTFILETYPE, initialdir=currdir,
                                             title='Please select a directory')
    elif index==VIDEOINDEX:
        tempdir = filedialog.askopenfilename(parent=root, filetypes=VIDEOFILETYPE, initialdir=currdir,
                                             title='Please select a directory')
    if(len(tempdir)>0):
        if not os.path.exists(os.getcwd()+"\\{}".format(name)):
            os.makedirs(os.getcwd()+"\\{}".format(name))
        if not os.path.exists(os.getcwd().replace("\\","/")+"/{}/".format(name)+tempdir.split("/")[-1]):#if there is no the same file
            originPostion=""+tempdir
            toPosition=os.getcwd().replace("\\","/")+"/{}/".format(name)+tempdir.split("/")[-1]#store the files used in result folder
            shutil.copyfile(originPostion,toPosition)
        return "{}/".format(name)+tempdir.split("/")[-1]
    return ""
def openColorDialog():#window for choosing supsific color
    color = QtWidgets.QColorDialog.getColor()
    New=Color()
    New.name=""
    New.html=color.name()
    if color.isValid():
        return New
    else:
        return False

def OutPut(node):#output the coding of a linked list
    if(node==False):
        return "\n"
    else:
        return node.node.coding+"\n"+OutPut(node.next)

def Storing(node):#storing the text for widgets in a linked list
    if (node == False):
        return "\n"
    else:
        return node.node.Storing() + "\n" + Storing(node.next)

def GetConnection():#get connection to the server
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 9999))
        return s
    except:
        Warning("server cannot be connected")
        return False


def TransferFolder(conn,folderaddress):#transfer datas
    conn.sendall(folderaddress.split("\\")[-1].encode())
    for file in os.listdir(folderaddress):
        FullPath=folderaddress+"\\"+file
        fUploadFile = open(FullPath, "rb")
        filesize = os.path.getsize(FullPath)
        conn.sendall((file).encode() )
        conn.recv(1024)#data transferring may be collided together and consist of a big packet and arrive the same time, so that this is to stop it
        conn.sendall(str(filesize).encode())
        conn.recv(1024)#data transferring may be collided together and consist of a big packet and arrive the same time, so that this is to stop it
        while True:
            data = fUploadFile.read(CHUNKSIZE)
            if not data:
                break
            conn.sendall(data)
        conn.recv(1024)
    conn.send("##finish".encode())


def RecieveFolder(conn):
    foldername = conn.recv(CHUNKSIZE).decode()
    if not os.path.exists(os.getcwd() + "\\" + foldername):
        os.makedirs(os.getcwd() + "\\" + foldername)
    folderPath = os.getcwd() + "\\" + foldername
    while True:
        data = conn.recv(CHUNKSIZE).decode()
        if data == "##finish": break
        FileName = data
        conn.sendall("recieve".encode())
        FileSize = int(conn.recv(CHUNKSIZE).decode())
        conn.sendall("recieve".encode())
        path = folderPath + "\\" + FileName
        os.makedirs(os.path.dirname(path), exist_ok=True)
        f = open(path, 'wb')

        while FileSize > 0:#if the file size left is bigger than 0
            Length = min(FileSize, CHUNKSIZE)
            data = conn.recv(Length)
            if not data:
                break
            f.write(data)#write it in the file
            FileSize -= Length#decrease file size by the written length
        conn.sendall("recieve".encode())
    return folderPath



