from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
import copy

class fileLayout(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.bind(size=self.update)
    def update(self,*args):
        print('file layout',self.size)

class testApp(App):
    def build(self):
        file=fileLayout(orientation='horizontal')
        print('after file create')
        print(file.size)
        mfile=BoxLayout(orientation='vertical')
        img=Image(source='./pics/test.jpg')
        img1=Image(source='./pics/test.jpg')
        img2=Image(source='./pics/test.jpg')
        img3=Image(source='./pics/test.jpg')
        img4=Image(source='./pics/test.jpg')
        img5=Image(source='./pics/test.jpg')
        file.add_widget(img)
        file.add_widget(img1)
        file.add_widget(img2)
        file.add_widget(img3)
        file.add_widget(img4)
        file.add_widget(img5)
        mfile.add_widget(file)
        
        return mfile

testApp().run()