from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from fileicon import fileIcon

class FileApp(App):
    def build(self):
        return scrollFileView()

class scrollFileView(ScrollView):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.st=StackLayout(size_hint=(1,None))
        for i in range(100):
            self.st.add_widget(fileIcon(size_hint=(0.125,None)))
        self.st.bind(minimum_height=self.st.setter('height'))
        self.size_hint=(1,1)
        self.add_widget(self.st)

FileApp().run()