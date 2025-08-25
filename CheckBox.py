from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.checkbox import CheckBox
from kivymd.uix.label import MDLabel

class Principal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cb = CheckBox()
        self.cb.bind(active = self.active)
        self.add_widget(self.cb)

        self.label1 = MDLabel(text = 'No estás de acuerdo', halign = 'center', pos_hint = {'center_y': 0.2})
        self.add_widget(self.label1)

    def active(self, checkbox, valor):
        if valor:
            self.label1.text = 'Estás de acuerdo'
        else:
            self.label1.text = 'No estás de acuerdo'


class Miapp(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(Principal(name = 'principal'))
        self.theme_cls.theme_style = 'Dark'

        return SC

Miapp().run()