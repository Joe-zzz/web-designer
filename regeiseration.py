# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regeiseration.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Regiseration(object):
    def setupUi(self, Regiseration):
        Regiseration.setObjectName("Regiseration")
        Regiseration.resize(362, 347)
        self.label = QtWidgets.QLabel(Regiseration)
        self.label.setGeometry(QtCore.QRect(30, 30, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Regiseration)
        self.label_2.setGeometry(QtCore.QRect(90, 30, 91, 16))
        self.label_2.setObjectName("label_2")
        self.Firstname = QtWidgets.QLineEdit(Regiseration)
        self.Firstname.setGeometry(QtCore.QRect(220, 30, 113, 21))
        self.Firstname.setObjectName("Firstname")
        self.label_3 = QtWidgets.QLabel(Regiseration)
        self.label_3.setGeometry(QtCore.QRect(90, 60, 72, 15))
        self.label_3.setObjectName("label_3")
        self.Surname = QtWidgets.QLineEdit(Regiseration)
        self.Surname.setGeometry(QtCore.QRect(220, 60, 113, 21))
        self.Surname.setObjectName("Surname")
        self.label_4 = QtWidgets.QLabel(Regiseration)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 101, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Regiseration)
        self.lineEdit.setGeometry(QtCore.QRect(30, 190, 301, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(Regiseration)
        self.label_5.setGeometry(QtCore.QRect(70, 220, 201, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Regiseration)
        self.label_6.setGeometry(QtCore.QRect(30, 110, 72, 15))
        self.label_6.setObjectName("label_6")
        self.gender = QtWidgets.QComboBox(Regiseration)
        self.gender.setGeometry(QtCore.QRect(180, 110, 111, 22))
        self.gender.setObjectName("gender")
        self.gender.addItem("")
        self.gender.addItem("")
        self.finish = QtWidgets.QPushButton(Regiseration)
        self.finish.setGeometry(QtCore.QRect(240, 290, 93, 28))
        self.finish.setObjectName("finish")
        self.cancel = QtWidgets.QPushButton(Regiseration)
        self.cancel.setGeometry(QtCore.QRect(140, 290, 93, 28))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(Regiseration)
        QtCore.QMetaObject.connectSlotsByName(Regiseration)

    def retranslateUi(self, Regiseration):
        _translate = QtCore.QCoreApplication.translate
        Regiseration.setWindowTitle(_translate("Regiseration", "Regiseration"))
        self.label.setText(_translate("Regiseration", "Name:"))
        self.label_2.setText(_translate("Regiseration", "Firstname:"))
        self.label_3.setText(_translate("Regiseration", "Surname:"))
        self.label_4.setText(_translate("Regiseration", "Password:"))
        self.label_5.setText(_translate("Regiseration", "<html><head/><body><p align=\"center\">password must be at least<br/>7 character</p></body></html>"))
        self.label_6.setText(_translate("Regiseration", "Gender:"))
        self.gender.setItemText(0, _translate("Regiseration", "Male"))
        self.gender.setItemText(1, _translate("Regiseration", "Female"))
        self.finish.setText(_translate("Regiseration", "Finish"))
        self.cancel.setText(_translate("Regiseration", "Cancel"))

    def Check(self):
        text=self.lineEdit.text()
        if len(text)>=7 and len(text)<=16:
            return True
        else:
            return False