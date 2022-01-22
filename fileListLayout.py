from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from fileicon import fileIcon,dirIcon
from kivy.uix.label import Label
import os

for root,dirs,files in os.walk(os.getcwd()):
    break

class FileApp(App):
    def build(self):
        return scrollFileView(root,dirs,files)

class scrollFileView(ScrollView):
    def __init__(self,root,dirs,files,**kwargs):
        print(root,dirs,files)
        super().__init__(**kwargs)
        self.st=StackLayout(size_hint=(1,None),spacing=10)
        for i in dirs:
            self.st.add_widget(dirIcon(fname=i,size_hint=(0.125,None)))
        for i in files:
            self.st.add_widget(fileIcon(fname=i,size_hint=(0.125,None)))
        self.st.bind(minimum_height=self.st.setter('height'))
        self.size_hint=(1,1)
        self.add_widget(self.st)

if __name__=='__main__':
    FileApp(title=root).run()