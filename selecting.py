# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selecting.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SelectingFrom(object):
    def setupUi(self, SelectingFrom):
        SelectingFrom.setObjectName("SelectingFrom")
        SelectingFrom.resize(377, 188)
        self.pushButton = QtWidgets.QPushButton(SelectingFrom)
        self.pushButton.setGeometry(QtCore.QRect(60, 30, 241, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(SelectingFrom)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 100, 241, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(SelectingFrom)
        QtCore.QMetaObject.connectSlotsByName(SelectingFrom)

    def retranslateUi(self, SelectingFrom):
        _translate = QtCore.QCoreApplication.translate
        SelectingFrom.setWindowTitle(_translate("SelectingFrom", "selecting"))
        self.pushButton.setText(_translate("SelectingFrom", "Create from existing design"))
        self.pushButton_2.setText(_translate("SelectingFrom", "Create from nothing"))
