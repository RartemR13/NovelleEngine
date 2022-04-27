from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
from kivy.core.audio import SoundLoader, Sound
from menuscreenapp import MenuScreenApp
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import ObjectProperty, NumericProperty

def CreateGraph():
    graph = []
    for i in range(16):
        graph.append([])
    edges = [[0, 4], [4, 8], [8, 9], [9, 5], [9, 13], [12, 13], [0, 1], [1, 2], [2, 6], [2, 3], [3, 7], [7, 11],
             [11, 10], [10, 14], [15, 14]]
    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    return graph

class Container(MenuScreenApp):
    pass

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass



class Manager(ScreenManager):
    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    #img = ObjectProperty(None)

    graph = []
    dct = {0: 4, 1: 1, 2: -1, 3: -4}

    cur_pos = 0
    fin_pos = 15

    def try_move(self, dir):
        if self.cur_pos + self.dct[dir] in self.graph[self.cur_pos]:
            self.cur_pos += self.dct[dir]
        self.screen_two.label.text = str(self.cur_pos)

        self.screen_two.forward.source = 'door.jpeg' if self.cur_pos + self.dct[0] in self.graph[
            self.cur_pos] else 'wall.jpeg'
        self.screen_two.r.source = 'door.jpeg' if self.cur_pos + self.dct[1] in self.graph[
            self.cur_pos] else 'wall.jpeg'
        self.screen_two.left.source = 'door.jpeg' if self.cur_pos + self.dct[2] in self.graph[
            self.cur_pos] else 'wall.jpeg'
        self.screen_two.back.source = 'door.jpeg' if self.cur_pos + self.dct[3] in self.graph[
            self.cur_pos] else 'wall.jpeg'
        self.screen_two.back.reload()
        return



    def __init__(self, gr, **kwargs):
        super().__init__(**kwargs)
        self.graph = gr

class MainApp(App):
    graph = []

    def __init__(self, gr):
        super().__init__()
        self.graph = gr


    def build(self):

        return Manager(self.graph, transition=NoTransition())


if __name__ == '__main__':
    MainApp(CreateGraph()).run()

