from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
from kivy.config import Config
from kivy.core.audio import SoundLoader, Sound
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('main.kv')

class Container(Screen):
    Music = SoundLoader.load('forest.wav')

    # plays - function which can turn on/off music by press same button

    def plays(self):
        if Container.Music.state == 'stop':
            Container.Music.play()
        else:
            Container.Music.stop()

    # fs - function which can on fullscreen mode

    def fs(self):
        Window.fullscreen = True

    # ws - function which can on window mode

    def ws(self):
        Window.fullscreen = False



class MainApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MainApp().run()

