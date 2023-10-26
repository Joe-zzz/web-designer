# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'audio.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Function import*

class Ui_Audio(object):
    def setupUi(self, Audio):
        Audio.setObjectName("Audio")
        Audio.resize(405, 131)
        self.Name=''
        self.label_48 = QtWidgets.QLabel(Audio)
        self.label_48.setGeometry(QtCore.QRect(20, 30, 72, 15))
        self.label_48.setObjectName("label_48")
        self.B_SearchImage_2 = QtWidgets.QPushButton(Audio)
        self.B_SearchImage_2.setGeometry(QtCore.QRect(350, 30, 21, 28))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.B_SearchImage_2.setFont(font)
        self.B_SearchImage_2.setObjectName("B_SearchImage_2")
        self.label_47 = QtWidgets.QLabel(Audio)
        self.label_47.setGeometry(QtCore.QRect(80, 30, 191, 16))
        self.label_47.setObjectName("label_47")
        self.Finish = QtWidgets.QPushButton(Audio)
        self.Finish.setGeometry(QtCore.QRect(300, 80, 93, 28))
        self.Finish.setObjectName("Finish")
        self.Cancel = QtWidgets.QPushButton(Audio)
        self.Cancel.setGeometry(QtCore.QRect(190, 80, 93, 28))
        self.Cancel.setObjectName("Cancel")
        self.done=False
        self.retranslateUi(Audio)
        QtCore.QMetaObject.connectSlotsByName(Audio)
        self.B_SearchImage_2.clicked.connect(self.Search)

    def retranslateUi(self, Audio):
        _translate = QtCore.QCoreApplication.translate
        Audio.setWindowTitle(_translate("Audio", "Audio"))
        self.label_48.setText(_translate("Audio", "audio:"))
        self.B_SearchImage_2.setText(_translate("Audio", "⋮"))
        self.label_47.setText(_translate("Audio", "audioName"))
        self.Finish.setText(_translate("Audio", "Finish"))
        self.Cancel.setText(_translate("Audio", "Cancel"))


    def Search(self):
        self.File = searching(AUDIOINDEX,self.Name)
        if (self.File != ""):
            self.label_47.setText(self.File.split("/")[-1])

    def clear(self):
        self.File = ""
        self.label_47.setText("AudioName")
        self.done = False