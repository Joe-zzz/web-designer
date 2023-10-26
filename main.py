import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainwindow import*
from regeiseration import Ui_Regiseration
from SignIn import Ui_SignIn
import pickle
import socket
from ChooseDesign import Ui_ChooseDesign
from startWin import Ui_StartWin
from selecting import Ui_SelectingFrom
from selectingMode import Ui_SelectMode
from ProjectName import Ui_ProjectName
class PName(QtWidgets.QDialog):#Get initial name of project
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.Window = Ui_ProjectName()
        self.Window.setupUi(self)
        self.done=False
        self.Window.pushButton.clicked.connect(self.Finish)
    def Finish(self):
        self.done=True
        self.hide()
    def GetName(self):
        self.show()
        self.exec_()
        if(self.done):
            return self.Window.name.text()
        else:
            return False

class MainWin(QtWidgets.QDialog):#Main window for designing windows
    def __init__(self,name):
        QtWidgets.QDialog.__init__(self)
        self.Window=Ui_MainWindow()
        self.Window.setupUi(self,name)
        self.Window.pushButton.clicked.connect(self.finish)
        self.Window.pushButton_2.clicked.connect(self.cancel)
    def finish(self):
        if not os.path.exists(os.getcwd()+"\\{}".format(self.Window.NAME)):
            os.makedirs(os.getcwd()+"\\{}".format(self.Window.NAME))
        handle=open(os.getcwd().replace("\\", "/") + "/{}/result.html".format(self.Window.NAME) ,"w")#Write HTML coding
        handle.write("<html>\n<head>\n<title>{}</title>\n".format(self.Window.Title.text()))
        handle.write("<style>\n"+OutPut(self.Window.ClassList.head)+"</style>\n</head>\n")
        handle.write("<body>\n"+OutPut(self.Window.linkedList.head)+"</body>\n"+"</html>")
        handle=open(os.getcwd().replace("\\", "/") + "/{}/result.txt".format(self.Window.NAME),"w")
        handle.write(self.Window.Title.text()+"\n")
        handle.write(Storing(self.Window.ClassList.head))#Storing this canvas in the txt file, which allow to get it next time
        handle.write(Storing(self.Window.linkedList.head))
        handle=open(os.getcwd()+"\\ProjectName.txt","a")
        Handle=open(os.getcwd()+"\\ProjectName.txt","r")
        Lines=Handle.read().split("\n")
        BCase=True
        for i in Lines:#write in the text file which have the names of the local projects and this for loop is to make sure that the same project won't be add again after second editing
            if i==self.Window.NAME: BCase=False
        if(BCase): handle.write(self.Window.NAME+"\n")#each name is gapped by \n
        Message=QtWidgets.QDialog()
        buttonReply = QtWidgets.QMessageBox.question(Message, 'PyQt5 message', "Do you want to store design in the cloud?",
                                           QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)#If answer right, then store data in the server
        Message.show()
        self.hide()
        if buttonReply == QtWidgets.QMessageBox.Yes:
            conn=GetConnection()
            conn.sendall("add design".encode())#send add design request to server
            conn.recv(1024).decode()
            conn.sendall(self.Window.NAME.encode())
            conn.recv(1024).decode()
            TransferFolder(conn,os.getcwd()+"\\{}".format(self.Window.NAME))
            DesignID=conn.recv(1024).decode()
            ownerWin=AddOwnerShip(DesignID)#add ownership
            ownerWin.show()
            ownerWin.exec_()
    def cancel(self):
        self.hide()

class Regiseration(QtWidgets.QDialog):
    def __init__(self):
        s=GetConnection()#get regist
        if (s!=False):
            QtWidgets.QDialog.__init__(self)
            self.Window = Ui_Regiseration()
            self.Window.setupUi(self)
            self.connection=s
            self.Window.finish.clicked.connect(self.finish)

    def finish(self):#regist account
        self.connection.sendall("register".encode())
        self.connection.recv(1024)
        self.connection.sendall(self.Window.Firstname.text().encode())
        self.connection.recv(1024)
        self.connection.sendall(self.Window.Surname.text().encode())
        self.connection.recv(1024)
        self.connection.sendall(self.Window.gender.currentText().encode())
        self.connection.recv(1024)
        self.connection.sendall(self.Window.lineEdit.text().encode())
        client_data = self.connection.recv(1024).decode()
        if client_data=="True":
            self.connection.sendall("recieved".encode())
            UserID = self.connection.recv(1024).decode()
            Information("Your user id is {}".format(UserID))
            self.hide()
            Select=Selecting()
            Select.show()
            Select.exec_()
        else:
            Warning("Wrong")

class SelectingMode(QtWidgets.QDialog):
    def __init__(self,connection):
        QtWidgets.QDialog.__init__(self)
        self.Window=Ui_SelectMode()
        self.Window.setupUi(self)
        self.connection=connection
        self.Window.pushButton.clicked.connect(self.ChooseLocally)
        self.Window.pushButton_2.clicked.connect(self.ChooseFromCloud)
        
    def ChooseLocally(self):
        self.connection.sendall("exit".encode())#exit from the cloud
        self.connection.close()
        self.hide()
        Select=Selecting()
        Select.show()
        Select.exec_()




    def ChooseFromCloud(self):
        recieve = ''
        projectName = []#get projects name of this account
        self.hide()
        self.connection.sendall("recieve".encode())
        while True:
            self.connection.sendall("recieve".encode())
            recieve = self.connection.recv(1024).decode()
            if recieve == "finish":
                break
            else:
                projectName.append(recieve)

        Choosing = ChoosingDesign(projectName)
        index = Choosing.GetDesign()#Get index
        if (index != -1):
            self.connection.sendall(str(index).encode())
            if self.connection.recv(1024).decode()=="Right":#recieve the project folder in the cloud
                Path = RecieveFolder(self.connection)
                ex = MainWin(Path.split("\\")[-1])
                ex.Window.Reading(Path + "\\result.txt")
                ex.show()
                ex.exec_()

            else:
                Warning("the index is out of range")
                self.close()
        else:
            self.connection.sendall("Wrong".encode())
        self.connection.close()


class Selecting(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.Window=Ui_SelectingFrom()
        self.Window.setupUi(self)
        self.Window.pushButton.clicked.connect(self.Choosing)
        self.Window.pushButton_2.clicked.connect(self.Creating)
    def Creating(self):
        self.hide()
        NameWin=PName()#get design name
        projectName=NameWin.GetName()
        ex = MainWin(projectName)
        ex.show()
        ex.exec_()
    def Choosing(self):
        handle = open(os.getcwd() + "\\" + "ProjectName.txt")#get list of projects name
        List = handle.read().split("\n")
        self.hide()
        if len(List) > 1:
            choose = ChoosingDesign(List)
            Index = choose.GetDesign()
            ex = MainWin(List[Index])

            if (os.path.exists(os.getcwd() + "\\" + List[Index])):
                ex.Window.Reading(os.getcwd() + "\\" + List[Index]+"\\result.txt")#load design
                ex.show()
                ex.exec_()
            else:
                Warning("File didn't found")
        else:
            Warning("No file found")





class Starting(QtWidgets.QMainWindow):#Start window
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.Window=Ui_StartWin()
        self.Window.setupUi(self)
        self.Window.pushButton.clicked.connect(self.click1)
        self.Window.pushButton_2.clicked.connect(self.click2)
        self.Window.pushButton_3.clicked.connect(self.click3)
    def click1(self):#choose to register
        self.hide()
        Register=Regiseration()
        Register.show()
        Register.exec_()
    def click2(self):#choose to sign in
        self.hide()
        Signing=SigningIn()
        Signing.show()
        Signing.exec_()
    def click3(self):#choose to select window
        self.hide()
        Select=Selecting()
        Select.show()
        Select.exec_()




class ChoosingDesign(QtWidgets.QDialog):#choose design index from a list of design name
    def __init__(self,name):
        QtWidgets.QDialog.__init__(self)
        self.Window = Ui_ChooseDesign()
        self.Window.setupUi(self)
        self.done=False
        self.Window.Choose.clicked.connect(self.finish)
        for i in name:
            self.Window.Design.addItem(i)
    def finish(self):
        self.done= True
        self.hide()
    def GetDesign(self):
        self.show()
        self.exec_()
        if(self.done):
            return self.Window.Design.currentIndex()
        else:
            return -1
class SigningIn(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        s = GetConnection()
        self.Window = Ui_SignIn()
        self.Window.setupUi(self)
        self.Try=2
        if (s != False):
            s.sendall("log in".encode())
            self.connection = s
            self.Window.Finish.clicked.connect(self.finish)
        else:
            self.hide()
    def finish(self):#sign in from the server
        self.connection.sendall(self.Window.UserID.text().encode())
        self.connection.sendall(self.Window.Password.text().encode())
        text=self.connection.recv(1024).decode()
        if (text=="True"):
            selecting=SelectingMode(self.connection)
            selecting.show()
            selecting.exec_()
            self.hide()
        else:
            self.Window.label_3.setText("UserID or Password is wrong <br> There are {} times left".format(str(self.Try)))
            self.Try-=1
            if(self.Try==0):
                self.hide()

class AddOwnerShip(QtWidgets.QDialog):
    def __init__(self,DesignID):
        QtWidgets.QDialog.__init__(self)

        self.Window = Ui_SignIn()
        self.Window.setupUi(self)
        self.Window.Finish.setText("add")
        self.Try=2
        self.Window.Finish.clicked.connect(self.finish)
        self.DesignID=DesignID
        self.hide()
    def finish(self):#add ownership which can be repeated again
        s = GetConnection()
        if (s==False):
            self.hide()
            return
        self.connection = s
        self.connection.sendall("add ownership".encode())
        self.connection.recv(1024).decode()
        self.connection.sendall(self.DesignID.encode())
        self.connection.recv(1024).decode()
        self.connection.sendall(self.Window.UserID.text().encode())
        self.connection.sendall(self.Window.Password.text().encode())
        text=self.connection.recv(1024).decode()
        if (text=="True"):
            self.Window.label_3.setText("It have been added to user {}".format(self.Window.UserID.text()))
            self.connection.close()
            self.Try=2
        else:
            self.Window.label_3.setText("UserID or Password is wrong <br> There are {} times left".format(str(self.Try)))
            self.Try-=1
            if(self.Try==0):
                self.hide()









def main():

    app = QApplication(sys.argv)

    Start=Starting()
    Start.show()



    app.exec_()




if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
