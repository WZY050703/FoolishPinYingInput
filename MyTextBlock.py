import pyglet as gl
class TextBlock:
    isinBlock=False
    color=[255,255,255,255]
    label=gl.text.Label()
    def __init__(self,batch,text="text",x=0,y=0,
                 font_size=36,color=[255,255,255,255]) -> None:
        self.label.text=text
        self.label.x=x
        self.label.y=y
        self.label.font_size=font_size
        self.label.color=color
        self.label.batch=batch
        self.color=color
    def mouseMove(self,x,y):
        lx=self.label.x
        ly=self.label.y
        w=self.label.content_width
        h=self.label.content_height
        if(self.isinBlock==False):
            if((lx<x and x<lx+w) and (ly<y and y<ly+h)):
                self.isinBlock=True
                self.label.color=[2, 248, 195,255]
        if(self.isinBlock==True):
            if(not((lx<x and x<lx+w) and (ly<y and y<ly+h))):
                self.isinBlock=False
                self.label.color=self.color
        #self.draw()
    def mousePress(self,x,y,button,modifiers):
        pass
