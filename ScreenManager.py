from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDRaisedButton

class Principal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.boton1 = MDRaisedButton(text = 'Pasar a 2', pos_hint = {'center_x': 0.5, 'center_y': 0.7}, md_bg_color = (1, 0, 0, 1),
        on_press = lambda x: self.pasar_a_2())

        self.add_widget(self.boton1)

    def pasar_a_2(self):
        self.manager.transition.direction = 'left'
        self.manager. current = 'secundaria'


class Secundaria(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.boton2 = MDRaisedButton(text = 'Pasar a 1', pos_hint = {'center_x': 0.5, 'center_y': 0.2}, md_bg_color = (0, 0, 1, 1),
        on_press = lambda x: self.pasar_a_1())

        self.add_widget(self.boton2)

    def pasar_a_1(self):
        self.manager.transition.direction = 'right'
        self.manager. current = 'principal'


class Miapp(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(Principal(name = 'principal'))
        SC.add_widget(Secundaria(name = 'secundaria'))

        return SC

Miapp().run()