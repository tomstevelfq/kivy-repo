from kivy.app import App
from fileNaviBar import fileNaviBar
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Color,Rectangle

class mainInterface(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0.1484,0.1680,0.1836,1)
            self.rt=Rectangle()
        self.bind(size=self.update,pos=self.update)
        self.add_widget(fileNaviBar(size_hint=(1,None),height=40))
    def update(self,*args):
        self.rt.pos=self.pos
        self.rt.size=self.size

class fileApp(App):
    def build(self):
        return mainInterface()

if __name__=='__main__':
    fileApp().run()