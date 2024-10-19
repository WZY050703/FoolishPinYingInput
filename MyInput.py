import pyglet as gl
import MyTextBlock as MTB
import Yin2Zi

def yuany(c):
    return (c=='a' or c=='e' or c=='i' or c=='o' or c=='u')

def CutPinYin(PinYin):
    PYs=[]
    isbg=False
    tx=''
    last=''
    for i in PinYin:
        if((not yuany(i)) and (not(yuany(last) and i=='n')) 
           and (not(last=='n' and i=='g')) and (not(last=='z' and i=='h'))
            and (not(last=='c' and i=='h'))  and (not(last=='s' and i=='h'))):
            if(isbg==False):
                isbg=True
            else:
                PYs.append(tx)
            tx=i
        else:
            tx=tx+i
        last=i
    PYs.append(tx)
    #for i in PYs:
    #    print(i)
    Yin2Zi.Y2Z(PYs)

class Input(MTB.TextBlock):
    model="Lising"
    isBgInput=False
    def mousePress(self, x, y, button, modifiers):
        if(self.isinBlock):
            self.model="GET"
            if(self.isBgInput==False):
                self.label.text=''
                self.isBgInput=True
        else:
            self.model="Lising"
            if(len(self.label.text)==0):
                self.label.text="Lising"
                self.isBgInput=False
        super().mousePress(x, y, button, modifiers)
    def KeyInput(self,button,modifiers):
        if(self.model=="GET"):
            x=button
            if(32<=x and x<=122):
                self.label.text=self.label.text+chr(button)
            if(x==65288):#backspace
                self.label.text=self.label.text[:-1]
            if(x==65535):#delete
                pass
            if(x==65289):#tab
                self.label.text=self.label.text+"    "
            if(x==65293):#enter
                CutPinYin(self.label.text)
                self.label.text=''