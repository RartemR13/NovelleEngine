from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
from kivy.config import Config

class Container(FloatLayout):
    pass


class MainApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MainApp().run()

