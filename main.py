from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.root = Builder.load_file('main.kv')


MainApp().run()