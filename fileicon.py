from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class fileIcon(BoxLayout):
    def __init__(self,iconpath='./pics/fileicon.png',fname='fname',**kwargs):
        super().__init__(**kwargs)
        fileimg=Image(source=iconpath,size_hint=(1,0.8))
        filename=Label(text=fname,size_hint=(1,0.2))
        self.orientation='vertical'
        self.add_widget(fileimg)
        self.add_widget(filename)
        self.bind(width=self.setter('height'))

class dirIcon(BoxLayout):
    def __init__(self,iconpath='./pics/diricon.png',fname='dirname',**kwargs):
        super().__init__(**kwargs)
        fileimg=Image(source=iconpath,size_hint=(1,0.8))
        filename=Label(text=fname,size_hint=(1,0.2))
        self.orientation='vertical'
        self.add_widget(fileimg)
        self.add_widget(filename)
        self.bind(width=self.setter('height'))

