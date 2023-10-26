# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'textWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from Function import *
import shutil
from Class import*
from ClassWin import*

class Ui_TextWin(object):
    def setupUi(self, TextWin,Window):
        TextWin.setObjectName("TextWin")
        TextWin.resize(393, 166)

        self.done=False
        self.Window=Window
        self.TextFile=""
        self.text=""
        self.Name=''

        self.label = QtWidgets.QLabel(TextWin)
        self.label.setGeometry(QtCore.QRect(20, 80, 72, 15))
        self.label.setObjectName("label")
        self.TextName = QtWidgets.QLabel(TextWin)
        self.TextName.setGeometry(QtCore.QRect(120, 80, 141, 16))
        self.TextName.setObjectName("TextName")
        self.search = QtWidgets.QPushButton(TextWin)
        self.search.setGeometry(QtCore.QRect(260, 80, 93, 28))
        self.search.setObjectName("search")
        self.class_2 = QtWidgets.QComboBox(TextWin)
        self.class_2.setGeometry(QtCore.QRect(120, 30, 121, 22))
        self.class_2.setObjectName("class_2")
        self.label_3 = QtWidgets.QLabel(TextWin)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 72, 15))
        self.label_3.setObjectName("label_3")
        self.add = QtWidgets.QPushButton(TextWin)
        self.add.setGeometry(QtCore.QRect(260, 30, 93, 28))
        self.add.setObjectName("add")
        self.Cancel = QtWidgets.QPushButton(TextWin)
        self.Cancel.setGeometry(QtCore.QRect(170, 120, 93, 28))
        self.Cancel.setObjectName("Cancel")
        self.Finish = QtWidgets.QPushButton(TextWin)
        self.Finish.setGeometry(QtCore.QRect(280, 120, 93, 28))
        self.Finish.setObjectName("Finish")
        self.GetClass()
        self.retranslateUi(TextWin)
        QtCore.QMetaObject.connectSlotsByName(TextWin)

        self.search.clicked.connect(self.Search)
        self.add.clicked.connect(self.addClass)

    def retranslateUi(self, TextWin):
        _translate = QtCore.QCoreApplication.translate
        TextWin.setWindowTitle(_translate("TextWin", "TextWin"))
        self.label.setText(_translate("TextWin", "textfile:"))
        self.TextName.setText(_translate("TextWin", "TextFileName"))
        self.search.setText(_translate("TextWin", "Search"))
        self.label_3.setText(_translate("TextWin", "Class:"))
        self.add.setText(_translate("TextWin", "add"))
        self.Cancel.setText(_translate("TextWin", "Cancel"))
        self.Finish.setText(_translate("TextWin", "Finish"))

    def GetClass(self):
        self.class_2.clear()
        temp=self.Window.ClassList.head
        while(temp!=False):
            self.class_2.addItem(temp.node.Name)
            temp=temp.next
    def Search(self):
        self.TextFile=searching(TEXTFILEINDEX,self.Name)
        if(self.TextFile!=""):
            self.TextName.setText(self.TextFile.split("/")[-1])
            TextHandle=open(self.TextFile)
            self.text=TextHandle.read().replace("\n","<br>")




    def addClass(self):
        self.Window.classWin.Window.clear()
        Class = self.Window.classWin.GetClassNode()
        if Class!=False:
            node = nodes()
            node.node = Class
            node.content = Class
            node.next = False
            self.Window.ClassList.add(node)
            self.Window.listWidget.addItem(Class.Name)
            self.class_2.addItem(Class.Name)
    def clear(self):
        self.done = False
        self.TextFile = ""
        self.text = ""
        self.TextName.setText("TextFileName")
        self.GetClass()



