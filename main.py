from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.properties import ObjectProperty



class Container(GridLayout):
    text_input = ObjectProperty();
    image_screen = ObjectProperty();
    label = ObjectProperty();

    def change_text(self):
        self.label.text = self.text_input.text

    def change_pic(self, num):
        if (num == 0):
            self.image_screen.source = 'png/Trahat.jpg'
        elif (num == 1):
            self.image_screen.source = 'png/Help.jpg'
        elif (num == 2):
            self.image_screen.source = 'png/SHAD.jpg'
        else:
            raise ValueError

class MyApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    MyApp().run()