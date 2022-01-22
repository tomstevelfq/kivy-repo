from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.metrics import Metrics
from kivy.graphics import Line,Color
from tools import MyImage

class fileNaviBar(FloatLayout):
    length=35
    fsize=15
    gap1=70
    gap2=40
    zoom_attr=1
    def __init__(self,zoom_attr=1,**kwargs):
        super(fileNaviBar,self).__init__(**kwargs)
        with self.canvas:
           Color(1,0,1,1)
           self.bor=Line(width=3,rectangle=(self.x,self.y,0,0)) 
        self.bind(size=self.update_border,pos=self.update_border)
        self.apply_zoom(zoom_attr)
        img=MyImage(source='./pics/option.png',size_hint=(None,None),size=(self.length,self.length))
        self.orientation='horizontal'
        self.add_widget(img)
        self.lab=Label(padding=[10,0],halign='left',valign='center',text='hello world',font_size=self.fsize,size_hint=(None,None),height=self.length)
        self.add_widget(self.lab)
        with self.lab.canvas:
            Color(1,1,1,1)
            self.line=Line(width=1,rectangle=(self.lab.x,self.lab.y,0,0))
        self.bind(size=self.update_lab,pos=self.update_lab)
        self.lab.bind(size=self.update_lab,pos=self.update_lab)
        self.serimg=MyImage(source='./pics/search.png',size_hint=(None,None),size=(self.length,self.length))
        self.opt1img=MyImage(source='./pics/option1.png',size_hint=(None,None),size=(self.length,self.length))
        self.add_widget(self.serimg)
        self.add_widget(self.opt1img)
        self.bind(size=self.updateimg)
    
    def apply_zoom(self,zoom_attr):
        self.zoom_attr=zoom_attr
        self.length*=zoom_attr
        self.fsize*=zoom_attr
        self.gap1*=zoom_attr
        self.gap2*=zoom_attr
    def update_lab(self,*args,**kwargs):
        self.lab.width=self.width-(130*self.zoom_attr)
        self.lab.text_size=self.lab.size
        self.line.rectangle=(self.lab.x,self.lab.y,self.lab.width,self.lab.height)
    
    def updateimg(self,*args,**kwargs):
        self.serimg.pos=(self.width-self.gap1,self.y)
        self.opt1img.pos=(self.width-self.gap2,self.y)
        self.lab.pos=(self.gap2,self.y)
    
    def update_border(self,size,*args):
        self.bor.rectangle=(self.x,self.y,self.width,self.height)


class test(App):
    def build(self):
        return fileNaviBar(zoom_attr=1)

if __name__=='__main__':
    test().run()