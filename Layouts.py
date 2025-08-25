from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivymd.uix.button import MDRaisedButton

class Principal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #self.Lista = StackLayout(size_hint = (1, None), spacing = '5dp', padding = '10dp')

        #for i in range(100):
        #    self.Lista.add_widget(MDRaisedButton(text = str(i), height = 400, size_hint_y = None))

        #self.Lista.bind(minimum_height = self.Lista.setter('height'))

        #self.Scroll = ScrollView()
        #self.Scroll.add_widget(self.Lista)

        #self.add_widget(self.Scroll)
        lista_scroll = ScrollView(size_hint = (1, 0.7), pos_hint = {"center_x": 0.5, "top": 0.88})
        lista = GridLayout(size_hint = (1, None), cols= 2, spacing = 5, padding = 5)
        for i in range(100):
            lista.add_widget(Button(text = str(i), height = 100, size_hint_y = None))

        lista.bind(minimum_height = lista.setter('height'))
        lista_scroll.add_widget(lista)
        self.add_widget(lista_scroll)


class Miapp(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(Principal(name = 'principal'))
        self.theme_cls.theme_style = 'Dark'

        return SC

Miapp().run()