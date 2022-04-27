from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
from kivy.core.audio import SoundLoader, Sound

class MenuScreenApp(FloatLayout):
    Music = SoundLoader.load('forest.wav')


    def plays(self):
        if self.Music.state == 'stop':
            self.Music.play()
        else:
            self.Music.stop()


    def fs(self):
        Window.fullscreen = True


    def ws(self):
        Window.fullscreen = False