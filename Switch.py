from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.switch import Switch

class Principal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.sw = Switch()
        self.sw.bind(active = self.activar)
        self.add_widget(self.sw)

    def activar(self, switch, valor):
        if valor:
            print('Me gusta la pizaa')
        else:
            print('No me gusta la pizza')

class Miapp(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(Principal(name = 'principal'))
        self.theme_cls.theme_style = "Dark"

        return SC

Miapp().run()