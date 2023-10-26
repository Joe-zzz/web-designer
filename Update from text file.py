from main import ChoosingDesign,MainWin
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
app = QApplication(sys.argv)
handle = open(os.getcwd() + "\\" + "ProjectName.txt")#get list of projects name
List = handle.read().split("\n")
choose = ChoosingDesign(List)
Index = choose.GetDesign()
mainwindow=MainWin(List[Index])
if (os.path.exists(os.getcwd() + "\\" + List[Index])):
    mainwindow.Window.Reading(os.getcwd() + "\\" + List[Index] + "\\result.txt")
mainwindow.finish()