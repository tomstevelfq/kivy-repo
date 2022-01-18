from kivy.uix.stacklayout import StackLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.image import Image

class MyImage(Image):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.bind(width=self.update)
    def update(*args):
        print(*args)

class MyButton(Button):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.bind(width=self.update)
    def update(self,obj,width,*args):
        self.height=width

class MyStackLayout(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        for i in range(100):
            self.add_widget(MyButton(text=str(i),size_hint=(0.2,None)))

class TestApp(App):
    def build(self):
        mstack=MyStackLayout(size_hint=(1,None))
        mstack.bind(minimum_height=mstack.setter('height'))#必须的关键一步
        scView=ScrollView(size_hint=(1,None),size=(Window.width, Window.height))
        scView.add_widget(mstack)
        return scView

TestApp().run()