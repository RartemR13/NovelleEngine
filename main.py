from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
MDScreen:

    FitImage:
        source: 'pic.jpeg'

    MDRaisedButton:
        text: "Артем Хуесос"
        pos_hint: {"center_x": .5, "center_y": .5}
"""


class MainApp(MDApp):
    def build(self):
        self.root = Builder.load_string(KV)


MainApp().run()