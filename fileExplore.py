from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from fileNaviBar import fileNaviBar
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Line,Color
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyLabel(Label):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1,0,1,1)
            self.bor=Line(width=3,rectangle=(self.x,self.y,self.width,self.height))
        self.bind(size=self.update,pos=self.update) 
    def update(self,*args):
        self.bor.rectangle=(self.x,self.y,self.width,self.height)

class tlay(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1,0,1,1)
            self.bor=Line(width=3,rectangle=(self.x,self.y,self.width,self.height)) 
        self.bind(size=self.update_rec,pos=self.update_rec)
        # self.lab=Label(text='haha')
        # self.add_widget(self.lab)
        self.lab1=MyLabel(text='haha',size_hint=(0.2,1),pos_hint={'x':0})
        self.lab2=MyLabel(text='haha',size_hint=(0.8,1),pos_hint={'x':0.2})
        self.add_widget(self.lab1)
        self.add_widget(self.lab2)
    def update_rec(self,*args):
        self.bor.rectangle=(self.x,self.y,self.width,self.height)
        self.lab1.pos=self.pos
        self.lab2.pos=self.pos

class mainInterface(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #fnavbar=fileNaviBar(size_hint=(1,None),height=100)
        self.orientation='vertical'
        self.add_widget(tlay(size_hint=(1,None),height=100))
        self.add_widget(tlay(size_hint=(1,None),height=100))
        self.bind(height=self.sety)
        # self.add_widget(tlay(size_hint=(1,None),height=100))
        # self.add_widget(tlay(size_hint=(1,None),height=100))
        #self.add_widget(tlay(size_hint=(1,None),height=500))

    def sety(self,*args):
        self.y=self.height-200
        


class fileApp(App):
    def build(self):
        return mainInterface()

if __name__=='__main__':
    fileApp().run()