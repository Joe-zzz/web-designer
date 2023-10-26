from PyQt5 import QtCore, QtGui, QtWidgets
from SearchingColor import Ui_SearchingColor,Color
from Function import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
BACKGROUNDDEFAULT=-1#Constant for background types
BACKGROUNDIMAGE=0
BACKGROUNDCOLOR=1
FONTSIZE1=32#Constant for font size of taggings for heading
FONTSIZE2=24
FONTSIZE3=19
FONTSIZE4=16
FONTSIZE5=13
FONTSIZE6=11

class nodes():
    def __init__(self):
        self.last = False
        self.node = False
        self.content=False
        self.next = False


class linkedList():
    def __init__(self):
        self.head = False

    def SetHead(self, head):
        self.head = head
    def add(self, node):
        if self.head==False:#if there is no head set head
            self.SetHead(node)
        else:
            temp = self.head
            while (temp.next != False):
                temp = temp.next
            temp.next = node
            node.last = temp

    def delete(self, index):
        i = 0
        temp = self.head
        while ((i < index) and (temp.next != False)):#if i is smaller than index, then run to the next node. when there is no next node it will stop
            temp = temp.next
            i += 1
        if (i < index):#if index is over
            return False
        else:
            if (index==0):

                self.head=temp.next
                if(temp.next!=False):
                    temp.next.last=False
            elif (temp.next==False):
                temp.last.next = temp.next
            else:
                temp.last.next = temp.next
                temp.next.last = temp.last
    def get(self,index):#get the node on index
        i = 0
        temp = self.head
        while ((i < index) and (temp.next != False)):
            temp = temp.next
            i += 1
        return temp
    def insert(self, index, node):#add after node of index
        i = 0
        temp = self.head
        while ((i < index) and (temp.next != False)):
            temp = temp.next
            i += 1
        if (index == -1):
            if(self.head!=False):
                temp = self.head
                self.head = node
                node.next = temp
                temp.last = node
            else:
                self.SetHead(node)
        elif (i < index):
            temp.next = node
            node.last = temp
        else:
            node.next=temp.next
            temp.next=node
            node.last=temp
    def find(self,content):#find the index by the node
        i=0
        temp=self.head
        while ((temp.content!=content) and (temp.next != False)):
            temp=temp.next
            i+=1
        if(temp.content==content):
            return i
        else:
            Warning("Content did not find")
            return -1

    def switch(self,index1,index2):#switch between 2 nodes
        temp1=self.get(index1)
        temp2=self.get(index2)
        temp1.node,temp1.content,temp2.node,temp2.content=temp2.node,temp2.content,temp1.node,temp1.content






class MyInt():
    def __init__(self,INT):#class for int allow changing value in the functions
        self.int=INT

class MyLabel():
    def setup(self,textinL,coding,TextList,FontSize,Font,Height,Width,B_Background,Background,Repeatx,Repeaty,TextAlign,Padding,Margin,BorderStyle,BorderWidth,BorderColor,BorderRadius,Top,Left,Right,Bottom,color):
        self.Label=QtWidgets.QLabel()
        self.textinL=textinL
        self.coding=coding
        self.originalCoding=coding
        Style = ""#style for html

        StyleSheet = "QLabel{"#style sheet for label
        self.Size=18
        if (Height != "default"):
            self.Label.setFixedHeight(int(Height))
            Style += "height:{};".format(Height + "px")

        if (Width != "default"):
            self.Label.setFixedWidth(int(Width))
            Style += "width:{};".format(Width + "px")

        StyleSheet = "QLabel{"
        if B_Background.int == BACKGROUNDCOLOR:
            StyleSheet += "background-color:{};".format(Background.html)
            Style += "background-color:{};".format(Background.html)
        elif B_Background.int == BACKGROUNDIMAGE:
            StyleSheet += 'background-image: url("{}");'.format(Background)
            Style += 'background-image: url("{}");'.format(Background.split("/")[-1])
        if (not Repeaty) and (not Repeatx):
            StyleSheet += 'background-repeat:{};'.format("no-repeat")
            Style += 'background-repeat:{};'.format("no-repeat")
        elif not Repeaty:
            StyleSheet += 'background-repeat:{};'.format("repeat-x")
            Style += 'background-repeat:{};'.format("repeat-x")
        elif not Repeatx:
            StyleSheet += 'background-repeat:{};'.format("repeat-y")
            Style += 'background-repeat:{};'.format("repeat-y")
        if color.html != "#ffffff":
            if (color.name != ""):
                StyleSheet += 'color:{};'.format(color.name)
                Style += 'color:{};'.format(color.name)
            else:

                StyleSheet += 'color:{};'.format(color.html)
                Style += 'color:{};'.format(color.html)
        if (TextAlign == "right"):
            self.Label.setAlignment(QtCore.Qt.AlignRight)
            Style += "text-align:{};".format("right")
        elif (TextAlign == "justify"):
            self.Label.setAlignment(QtCore.Qt.AlignJustify)
            Style += "text-align:{};".format("justify")
        elif (TextAlign == "Left"):
            self.Label.setAlignment(QtCore.Qt.AlignLeft)
            Style += "text-align:{};".format("left")
        elif (TextAlign == "center"):
            self.Label.setAlignment(QtCore.Qt.AlignCenter)
            Style += "text-align:{};".format("center")
        if (Padding != "default"):
            StyleSheet += 'padding:{};'.format(Padding)
            Style += 'padding:{};'.format(Padding + "px")
        if (Margin != "default"):
            StyleSheet += 'margin:{};'.format(Margin)
            Style += 'margin:{};'.format(Margin + "px")
        if (BorderStyle != "none"):
            StyleSheet += 'border-style:{};'.format(BorderStyle)
            Style += 'border-style:{};'.format(BorderStyle)
        if (BorderWidth != '0'):
            StyleSheet += 'border-width:{};'.format(BorderWidth)
            Style += 'border-width:{};'.format(BorderWidth + "px")
        if (BorderColor.html != "#ffffff"):
            if (BorderColor.name != ""):
                StyleSheet += 'border-color:{};'.format(BorderColor.name)
                Style += 'border-color:{};'.format(BorderColor.name)
            else:
                StyleSheet += 'border-color:{};'.format(BorderColor.html)
                Style += 'border-color:{};'.format(BorderColor.html)
        if (BorderRadius != '0'):
            StyleSheet += 'border-radius:{};'.format(BorderRadius)
            Style += 'border-radius:{};'.format(BorderRadius + "px")
        if (not Top) or (not Left) or (not Right) or (not Bottom):
            if (not Top):
                StyleSheet += 'border-top-width:{};'.format('0')
                Style += 'border-top-width:{};'.format('0')
            if (not Left):
                StyleSheet += 'border-left-width:{};'.format('0')
                Style += 'border-left-width:{};'.format('0')
            if (not Right):
                StyleSheet += 'border-right-width:{};'.format('0')
                Style += 'border-right-width:{};'.format('0')
            if (not Bottom):
                StyleSheet += 'border-bottom-width:{};'.format('0')
                Style += 'border-bottom-width:{};'.format('0')


        StyleSheet += "}"
        self.StyleSheet=StyleSheet
        self.Style=Style
        self.type=""
        self.link=Link()
        self.link.setup("default","")#default the link class


    def Storing(self):# ### is for gapping between widgets
        return "###"+self.type + "##@" + self.Style + "##@" + self.StyleSheet + "##@" + self.coding + "##@" + self.link.__str__() + "##@" + self.textinL+"##@"+self.originalCoding
    def Reading(self,str):# read attributes from the text
        self.Label = QtWidgets.QLabel()
        List=str.split("##@")
        self.type=List[0]
        self.Style=List[1]
        self.StyleSheet=List[2]
        self.coding=List[3]
        self.link=Link()
        self.link.Reading(List[4])
        self.textinL=List[5]
        self.Label.setText(self.textinL)
        self.Label.setStyleSheet(self.StyleSheet)
        self.originalCoding=List[6]
        if(self.link.File)and(self.link.File!="default"):#if link is getted from textfile
            self.coding='<a href="{}">'.format(self.link.text)+self.originalCoding+'</a>'



class MyParagraphLabel(MyLabel):

    def setup (self,textinL,coding,textlist,FontSize,Font,Height,Width,B_Background,Background,Repeatx,Repeaty,TextAlign,Padding,Margin,BorderStyle,BorderWidth,BorderColor,BorderRadius,Top,Left,Right,Bottom,color):

        super(MyParagraphLabel,self).setup(textinL,coding,textlist,FontSize,Font,Height,Width,B_Background,Background,Repeatx,Repeaty,TextAlign,Padding,Margin,BorderStyle,BorderWidth,BorderColor,BorderRadius,Top,Left,Right,Bottom,color)
        self.type="paragraph"
        self.Label.setText(self.textinL)
        self.Label.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Maximum)#make it won't be enlarged automatically

        if (FontSize != "default"):
            self.Style += "font-family:{};font-size:{}px;".format(Font, FontSize)
        else:
            self.Style += "font-family:{};".format(Font)
            self.Size = 18

        self.StyleSheet=self.StyleSheet[:-1]+"font-family:{};font-size:{}px;".format(Font,str(self.Size))+"}"
        self.Style = 'style=' + '"' + self.Style + '"'

        self.coding = self.coding[:2] + " " + self.Style + self.coding[2:]
        self.Label.setStyleSheet(self.StyleSheet)
class MyHeadingLabel(MyLabel):
    def setup(self,textinL,coding,textlist,Size,Font,Height,Width,B_Background,Background,Repeatx,Repeaty,TextAlign,Padding,Margin,BorderStyle,BorderWidth,BorderColor,BorderRadius,Top,Left,Right,Bottom,color):

        super(MyHeadingLabel, self).setup(textinL,coding,textlist,Size,Font,Height,Width,B_Background,Background,Repeatx,Repeaty,TextAlign,Padding,Margin,BorderStyle,BorderWidth,BorderColor,BorderRadius,Top,Left,Right,Bottom,color)
        self.type="heading"
        self.Label.setText(self.textinL)
        self.Label.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Maximum)
        Style = ''

        if (Size == "h1"):
            self.Size = FONTSIZE1
        elif (Size == "h2"):
            self.Size = FONTSIZE2
        elif (Size == "h3"):
            self.Size = FONTSIZE3
        elif (Size == "h4"):
            self.Size = FONTSIZE4
        elif (Size == "h5"):
            self.Size = FONTSIZE5
        elif (Size == "h6"):
            self.Size = FONTSIZE6
        Style += "font-family:{};".format(Font)

        self.StyleSheet=self.StyleSheet[:-1]+"font-family:{};font-size:{}px;".format(Font,str(self.Size))+"}"


        self.Style = 'style=' + '"' + self.Style + '"'
        self.coding = self.coding[:3] + " " + self.Style + self.coding[3:]
        self.Label.setStyleSheet(self.StyleSheet)



class ClassWin(object):
    def setup(self,Name,FontSize,Font,B_Background,Background,Repeatx,Repeaty,TextAlign,Padding,Margin,BorderStyle,BorderWidth,BorderColor,BorderRadius,Top,Left,Right,Bottom,color):
        self.Name=Name
        Style = ""#class style for html coding

        self.TextAlign=TextAlign

        StyleSheet = "QLabel{"#class style for labels
        if B_Background.int == BACKGROUNDCOLOR:
            StyleSheet += "background-color:{};".format(Background.html)
            Style += "background-color:{};".format(Background.html)
        elif B_Background.int == BACKGROUNDIMAGE:
            StyleSheet += 'background-image: url("{}");'.format(Background)
            Style += 'background-image: url("{}");'.format(Background.split("/")[-1])
        if (not Repeaty) and (not Repeatx):
            StyleSheet += 'background-repeat:{};'.format("no-repeat")
            Style += 'background-repeat:{};'.format("no-repeat")
        elif not Repeaty:
            StyleSheet += 'background-repeat:{};'.format("repeat-x")
            Style += 'background-repeat:{};'.format("repeat-x")
        elif not Repeatx:
            StyleSheet += 'background-repeat:{};'.format("repeat-y")
            Style += 'background-repeat:{};'.format("repeat-y")
        if color.html != "#ffffff":
            if (color.name != ""):
                StyleSheet += 'color:{};'.format(color.name)
                Style += 'color:{};'.format(color.name)
            else:
                StyleSheet += 'color:{};'.format(color.html)
                Style += 'color:{};'.format(color.html)
        if (TextAlign == "right"):
            Style += "text-align:{};".format("right")
        elif (TextAlign == "justify"):
            Style += "text-align:{};".format("justify")
        elif (TextAlign == "Left"):
            Style += "text-align:{};".format("left")
        else :
            Style += "text-align:{};".format("center")
        if (Padding != "default"):
            StyleSheet += 'padding:{};'.format(Padding)
            Style += 'padding:{};'.format(Padding + "px")
        if (Margin != "default"):
            StyleSheet += 'margin:{};'.format(Margin)
            Style += 'margin:{};'.format(Margin + "px")
        if (BorderStyle != "none"):
            StyleSheet += 'border-style:{};'.format(BorderStyle)
            Style += 'border-style:{};'.format(BorderStyle)
        if (BorderWidth != '0'):
            StyleSheet += 'border-width:{};'.format(BorderWidth)
            Style += 'border-width:{};'.format(BorderWidth + "px")
        if (BorderColor.html != "#ffffff"):
            if (BorderColor.name != ""):
                StyleSheet += 'border-color:{};'.format(BorderColor.name)
                Style += 'border-color:{};'.format(BorderColor.name)
            else:
                StyleSheet += 'border-color:{};'.format(BorderColor.html)
                Style += 'border-color:{};'.format(BorderColor.html)
        if (BorderRadius != '0'):
            StyleSheet += 'border-radius:{};'.format(BorderRadius)
            Style += 'border-radius:{};'.format(BorderRadius + "px")
        if (not Top) or (not Left) or (not Right) or (not Bottom):
            if (not Top):
                StyleSheet += 'border-top-width:{};'.format('0')
                Style += 'border-top-width:{};'.format('0')
            if (not Left):
                StyleSheet += 'border-left-width:{};'.format('0')
                Style += 'border-left-width:{};'.format('0')
            if (not Right):
                StyleSheet += 'border-right-width:{};'.format('0')
                Style += 'border-right-width:{};'.format('0')
            if (not Bottom):
                StyleSheet += 'border-bottom-width:{};'.format('0')
                Style += 'border-bottom-width:{};'.format('0')
        StyleSheet += "}"
        self.StyleSheet = StyleSheet
        self.Style = Style
        self.coding = "." + self.Name + "{" + Style + "}"
        self.type="class"
    def Storing(self):
        return "###"+self.type+"##@"+self.Style+"##@"+self.StyleSheet+"##@"+self.coding+"##@"+self.TextAlign+"##@"+self.Name
    def Reading(self,str):
        List=str.split("##@")
        self.type=List[0]
        self.Style=List[1]
        self.StyleSheet=List[2]
        self.coding=List[3]
        self.TextAlign=List[4]
        self.Name=List[5]




class ClassLabel (object):
    def setup(self,textinL,coding,Class,BFile,address):

        self.Label=QtWidgets.QLabel()
        self.BFile=BFile
        self.address=address
        self.textinL=textinL
        self.coding = coding[:2] + ' class="{}"'.format(Class.Name)   + coding[2:]#set class for the html

        self.originalCoding=self.coding
        self.ClassName=Class.Name
        self.Style=Class.Style
        self.TextAlign=Class.TextAlign
        if (self.TextAlign == "right"):
            self.Label.setAlignment(QtCore.Qt.AlignRight)
        elif (self.TextAlign == "justify"):
            self.Label.setAlignment(QtCore.Qt.AlignJustify)
        elif (self.TextAlign == "Left"):
            self.Label.setAlignment(QtCore.Qt.AlignLeft)
        else :
            self.Label.setAlignment(QtCore.Qt.AlignCenter)
        self.textinL=textinL
        self.type='classLabel'
        self.Label.setText(self.textinL)
        self.link = Link()
        self.link.setup("default", "")
        self.Label.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Maximum)
        self.Label.setStyleSheet(self.Style)#set style from class to the labels

    def Storing(self):
        return "###"+self.type+"##@"+str(int(self.BFile))+"##@"+self.coding+"##@"+self.Style+"##@"+self.textinL+"##@"+self.TextAlign+"##@"+self.link.__str__()+"##@"+self.address+"##@"+self.ClassName+"##@"+self.originalCoding
    def Reading(self,str):
        List=str.split("##@")
        self.type=List[0]
        self.BFile=int(List[1])
        self.coding=List[2]
        self.Style=List[3]
        self.textinL=List[4]
        self.TextAlign=List[5]
        self.link=Link()
        self.link.Reading(List[6])
        self.address=List[7]
        self.ClassName=List[8]
        self.originalCoding=List[9]
        if(self.link.File)and(self.link.File!="default"):
            self.coding='<a href="{}">'.format(self.link.text)+self.originalCoding+'</a>'

        if(self.BFile):
            Handle=open(self.address)
            self.textinL=Handle.read().replace("\n", "<br>")
            self.coding="<p> {}</p>".format(self.textinL)
            self.coding = self.coding[:2] + ' class="{}"'.format(self.ClassName) + self.coding[2:]
        self.Label=QtWidgets.QLabel()
        self.Label.setText(self.textinL)
        if (self.TextAlign == "right"):
            self.Label.setAlignment(QtCore.Qt.AlignRight)
        elif (self.TextAlign == "justify"):
            self.Label.setAlignment(QtCore.Qt.AlignJustify)
        elif (self.TextAlign == "Left"):
            self.Label.setAlignment(QtCore.Qt.AlignLeft)
        else :
            self.Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Label.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Maximum)
        self.Label.setStyleSheet(self.Style)





class Link():
    def setup(self,Btextfile,text):
        if(Btextfile!="default"):  #if it is not set to be default as initiallizing
            self.File=Btextfile
            self.address=""
            if(Btextfile):
                self.address=text
                file=open(text)
                self.text=file.readline()
            else:
                self.text=text
        else:
            self.File="default"

    def __str__(self):
        if self.File=="default":
            return "default"
        else:
            return str(int(self.File))+"$"+self.address+"$"+self.text
    def Reading(self,str):#read information for the link
        if str!="default":
            List=str.split("$")
            self.File=int(List[0])
            self.address=List[1]
            self.text=List[2]
            if(self.File):
                file = open(self.address)
                self.text = file.readline()

        else:
            self.File="default"



class Picture():
    def setup(self,address):
        self.address=address
        self.coding='<img src="{}">'.format(self.address.split("/")[-1])  #set html coding
        self.originalCoding=self.coding
        self.pixmap=QtGui.QPixmap(self.address)
        self.Label=QtWidgets.QLabel()
        self.Label.setPixmap(self.pixmap)
        self.Label.resize(self.pixmap.width(),
                          self.pixmap.height())
        self.Label.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Maximum)
        self.link=Link()
        self.link.setup("default","")
        self.type="picture"
    def Storing(self):
        return "###"+self.type+"##@"+self.coding+"##@"+self.address+"##@"+self.link.__str__()+"##@"+self.originalCoding
    def Reading(self,str):
        List=str.split("##@")
        self.type=List[0]
        self.coding=List[1]
        self.address=List[2]
        self.link=Link()
        self.link.Reading(List[3])
        self.originalCoding=List[4]
        if(self.link.File)and(self.link.File!="default"):
            self.coding='<a href="{}">'.format(self.link.text)+self.originalCoding+'</a>'
        self.pixmap = QtGui.QPixmap(self.address)
        self.Label = QtWidgets.QLabel()
        self.Label.setPixmap(self.pixmap)
        self.Label.resize(self.pixmap.width(),
                          self.pixmap.height())
        self.Label.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Maximum)



class Video():
    def setup(self,address):
        self.address=address
        self.coding='<video width="320" height="240" controls>\n<source src="{}" type="video/mp4">\n</video>'.format(self.address.split("/")[-1])#set html coding
        self.Label=QtWidgets.QLabel()
        self.Label.setText("video:"+address)
        self.Label.setMinimumSize(320,240)
        self.Label.setMaximumSize(320,240)
        self.Label.setStyleSheet("QLabel{border-style:solid;border-color:black;border-radius:10;border-width:4}")
        self.type="video"
    def Storing(self):
        return "###"+self.type+"##@"+self.coding+"##@"+self.address

    def Reading(self, str):
        List = str.split("##@")
        self.type = List[0]
        self.coding = List[1]
        self.address = List[2]
        self.Label = QtWidgets.QLabel()
        self.Label.setText("video:" + self.address)
        self.Label.setMinimumSize(320,240)
        self.Label.setMaximumSize(320, 240)
        self.Label.setStyleSheet("QLabel{border-style:solid;border-color:black;border-radius:10;border-width:4}")#cannot read mp4, so that label is presented insteadly

class Audio():
    def setup(self,address):
        self.address=address
        self.coding='<audio controls>\n<source src="{}" type="audio/mpeg">\n</video>'.format(self.address.split("/")[-1])   #set html coding
        self.Label=QtWidgets.QLabel()
        self.Label.setText("audio:"+address)
        self.Label.setMinimumSize(300,52)
        self.Label.setMaximumSize(300,52)
        self.Label.setStyleSheet("QLabel{border-style:solid;border-color:black;border-radius:20;border-width:4}")
        self.type="audio"
    def Storing(self):
        return "###"+self.type+"##@"+self.coding+"##@"+self.address

    def Reading(self, str):
        List = str.split("##@")
        self.type = List[0]
        self.coding = List[1]
        self.address = List[2]
        self.Label = QtWidgets.QLabel()
        self.Label.setText("audio:" + self.address)
        self.Label.setMinimumSize(300, 52)
        self.Label.setMaximumSize(300, 52)
        self.Label.setStyleSheet("QLabel{border-style:solid;border-color:black;border-radius:20;border-width:4}")







