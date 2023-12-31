# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'String.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_String(object):
    def setupUi(self, String):
        String.setObjectName("String")
        String.resize(599, 258)

        self.html = ''
        self.list = []
        self.len = 0
        self.textlist = []
        self.B_im = False
        self.B_label = False
        self.paragraph = 0
        self.done = False

        self.Italic = QtWidgets.QPushButton(String)
        self.Italic.setGeometry(QtCore.QRect(80, 40, 61, 31))
        self.Italic.setObjectName("Italic")
        self.Delete = QtWidgets.QPushButton(String)
        self.Delete.setGeometry(QtCore.QRect(340, 40, 41, 31))
        self.Delete.setObjectName("Delete")
        self.Small = QtWidgets.QPushButton(String)
        self.Small.setGeometry(QtCore.QRect(200, 40, 61, 31))
        self.Small.setObjectName("Small")
        self.Bold = QtWidgets.QPushButton(String)
        self.Bold.setGeometry(QtCore.QRect(30, 40, 51, 31))
        self.Bold.setObjectName("Bold")
        self.Text = QtWidgets.QTextEdit(String)
        self.Text.setGeometry(QtCore.QRect(30, 70, 541, 111))
        self.Text.setObjectName("Text")
        self.Sup = QtWidgets.QPushButton(String)
        self.Sup.setGeometry(QtCore.QRect(300, 40, 41, 31))
        self.Sup.setObjectName("Sup")
        self.Finish = QtWidgets.QPushButton(String)
        self.Finish.setGeometry(QtCore.QRect(470, 200, 93, 28))
        self.Finish.setObjectName("Finish")
        self.Mark = QtWidgets.QPushButton(String)
        self.Mark.setGeometry(QtCore.QRect(140, 40, 61, 31))
        self.Mark.setObjectName("Mark")
        self.label_31 = QtWidgets.QLabel(String)
        self.label_31.setGeometry(QtCore.QRect(30, 20, 72, 15))
        self.label_31.setObjectName("label_31")
        self.Sub = QtWidgets.QPushButton(String)
        self.Sub.setGeometry(QtCore.QRect(260, 40, 41, 31))
        self.Sub.setObjectName("Sub")
        self.Cancel = QtWidgets.QPushButton(String)
        self.Cancel.setGeometry(QtCore.QRect(360, 200, 93, 28))
        self.Cancel.setObjectName("Cancel")

        ###########################################################
        self.Bold.setCheckable(True)
        self.Italic.setCheckable(True)
        self.Sub.setCheckable(True)
        self.Sup.setCheckable(True)
        self.Small.setCheckable(True)
        self.Delete.setCheckable(True)
        self.Mark.setCheckable(True)
        #####################################################

        ####################################################3
        self.retranslateUi(String)
        QtCore.QMetaObject.connectSlotsByName(String)

    def retranslateUi(self, String):
        _translate = QtCore.QCoreApplication.translate
        String.setWindowTitle(_translate("String", "String"))
        self.Italic.setText(_translate("String", "Italic"))
        self.Delete.setText(_translate("String", "del"))
        self.Small.setText(_translate("String", "Small"))
        self.Bold.setText(_translate("String", "Bold"))
        self.Sup.setText(_translate("String", "Sup"))
        self.Finish.setText(_translate("String", "Finish"))
        self.Mark.setText(_translate("String", "Marked"))
        self.label_31.setText(_translate("String", "Text:"))
        self.Sub.setText(_translate("String", "Sub"))
        self.Cancel.setText(_translate("String", "Cancel"))
        #####################################################
        self.Text.setText("")
        self.Text.textChanged.connect(self.textWrite)
        self.Text.cursorPositionChanged.connect(self.CursorChanged)
        self.Bold.clicked.connect(self.Press)
        self.Italic.clicked.connect(self.Press)
        self.Small.clicked.connect(self.Press)
        self.Sub.clicked.connect(self.Press)
        self.Sup.clicked.connect(self.Press)
        self.Delete.clicked.connect(self.Press)
        self.Mark.clicked.connect(self.Press)




    def CursorChanged(self):
        cursor=self.Text.textCursor()##delete the selection of text
        if len(cursor.selectedText())>1:
            cursor.clearSelection()
            self.Text.setTextCursor(cursor)
            self.Text.setFocus()
    def Press(self):

        self.Text.setFocus()

    def clear(self):
        self.html = ''
        self.list = []
        self.len = 0
        self.textlist = []
        self.B_im = False
        self.B_label = False
        self.paragraph = 0
        self.done = False
        self.Text.setText("")
        self.Bold.setChecked(False)
        self.Italic.setChecked(False)
        self.Small.setChecked(False)
        self.Sub.setChecked(False)
        self.Sup.setChecked(False)
        self.Delete.setChecked(False)
        self.Mark.setChecked(False)

    def textWrite(self):
        cursor=self.Text.textCursor()
        i=cursor.position()

        if(len(self.Text.toPlainText())>self.len):

            self.len=self.len + 1
            info=[self.Bold.isChecked(),self.Italic.isChecked(),self.Mark.isChecked(),self.Small.isChecked(),self.Sub.isChecked(),self.Sup.isChecked(),self.Delete.isChecked()]
            self.list.insert(i,info)
            text = self.Text.toPlainText()
            New = text[i-1]
            TabList=[['<b>','</b>'],['<i>','</i>'],['<span style="background-color: yellow;">','</span>'],['<small>','</small>'],['<sub>','</sub>'],['<sup>','</sup>'],['<span style="text-decoration:line-through;">','</span>']]
            if(len(text)>=i and text[i - 1] == "\n"):
                New="<br>"
            else:
                for f in range(7):
                    if info[f]:
                        New=TabList[f][0]+New+TabList[f][1]

            self.textlist.insert(i-1,New)
            text=''
            for z in self.textlist:
                text+=z

            self.Text.setText(text)
            cursor=self.Text.textCursor()
            cursor.movePosition(QtGui.QTextCursor.MoveOperation.Right,n=i)
            self.Text.setTextCursor(cursor)
            self.Text.setFocus()

        elif(len(self.Text.toPlainText())<self.len):
            self.list.pop(i)
            self.textlist.pop(i)
            self.len=self.len-1
