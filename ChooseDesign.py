# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChooseDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChooseDesign(object):
    def setupUi(self, ChooseDesign):
        ChooseDesign.setObjectName("ChooseDesign")
        ChooseDesign.resize(434, 83)
        self.Choose = QtWidgets.QPushButton(ChooseDesign)
        self.Choose.setGeometry(QtCore.QRect(320, 30, 93, 28))
        self.Choose.setObjectName("Choose")
        self.Design = QtWidgets.QComboBox(ChooseDesign)
        self.Design.setGeometry(QtCore.QRect(20, 30, 271, 21))
        self.Design.setObjectName("Design")

        self.retranslateUi(ChooseDesign)
        QtCore.QMetaObject.connectSlotsByName(ChooseDesign)

    def retranslateUi(self, ChooseDesign):
        _translate = QtCore.QCoreApplication.translate
        ChooseDesign.setWindowTitle(_translate("ChooseDesign", "Design"))
        self.Choose.setText(_translate("ChooseDesign", "Choose"))