from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Color,Rectangle
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView

class txtLabel(FloatLayout):
    def __init__(self,text='',**kwargs):
        super().__init__(**kwargs)
        self.wid=1000
        self.lab=Label(size_hint=(None,1),width=self.wid,text=text)
        self.add_widget(self.lab)
        self.bind(size=self.update,pos=self.update)
        with self.lab.canvas.before:
            Color(1,0,1,0.5)
            self.rec=Rectangle()
        self.lab.bind(size=self.labupdate,pos=self.labupdate)
    def update(self,*args):
        self.lab.pos=(self.x+(Window.width-self.wid)/2,self.y)
    def labupdate(self,*args):
        self.rec.pos=self.lab.pos
        self.rec.size=self.lab.size

class viewTxt(ScrollView):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.st=StackLayout(size_hint=(1,None))
        self.size_hint=(1,1)
        self.st.bind(minimum_height=self.st.setter('height'))
        self.st.spacing=15
        self.add_widget(self.st)
        self.staddWidget()
    def staddWidget(self):
       self.st.add_widget(txtLabel(text='hello world',size_hint=(1,None),height=Window.height*0.9))
       self.st.add_widget(txtLabel(text='hello world',size_hint=(1,None),height=Window.height*0.9))
       self.st.add_widget(txtLabel(text='hello world',size_hint=(1,None),height=Window.height*0.9)) 

class viewTxtApp(App):
    def build(self):
        Window.size=(1000,Window.height)
        return viewTxt()

if __name__=='__main__':
    viewTxtApp().run()

