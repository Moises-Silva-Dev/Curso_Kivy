from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle, Ellipse, Line

class Principal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Color(1, 0, 0, 0.8)
            self.rect = Rectangle(pos = self.center, size = (200, 100))

            Color(0, 0, 1, 1)
            self.ellips = Ellipse(pos = (200, 200), size = (50, 100))

            Color(1, 1, 1, 1)
            self.linea1 = Line(points = (0, 0, self.width/2, self.height, self.width, 0), width = 2)

            Color(0, 1, 0, 1)
            self.linea2 = Line(circle = (200, 300, 50), width = 3)

            Color(1, 1, 1 ,1)
            self.linea3 = Line(rectangle = (500, 300, 100, 50), width = 2.5)

    def on_size(self, *args):
        self.rect.pos = (self.center_x-(self.rect.size[0]/2),self.center_y-(self.rect.size[1]/2))
        self.linea1.points = (0, 0, self.width/2, self.height, self.width, 0)

class Miapp(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(Principal(name = 'principal'))
        self.theme_cls.theme_style = "Dark"

        return SC

Miapp().run()