import kivy
import numpy as np
from kivy.app import App
from kivy.graphics import *
from kivy.graphics import Color
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

radius = np.arange(55, 100)

def to_radians(x):
    x = x * np.pi / 180
    return x

class main(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text = "First side: "))
        self.sideA = TextInput(multiline = False)
        self.add_widget(self.sideA)

        self.add_widget(Label(text = "Second side: "))
        self.sideB = TextInput(multiline = False)
        self.add_widget(self.sideB)

        self.add_widget(Label(text = "Angle between the segments: "))
        self.angleA = TextInput(multiline = False)
        self.add_widget(self.angleA)

        self.add_widget(Label(text = "Press the button when your finish to draw the triangle"))
        self.action = Button(text = "Draw triangle")
        self.action.bind(on_press = self.draw_button)
        self.add_widget(self.action)

    def draw_button(self, instance):
        sideA = self.sideA.text
        sideB = self.sideB.text
        angleA = self.angleA.text

        try:
            sideA = float(sideA)
            sideB = float(sideB)
            angleA = to_radians(float(angleA))

        except ValueError:
            self.add_widget(Label(text = "One of your inputs is not a number!"))

        else:
            while sideA not in radius or sideB not in radius:
                if sideA not in radius or sideB not in radius:
                    mean = (sideA + sideB)/2
                    difference = 75 / mean
                    sideA = sideA * difference
                    sideB = sideB * difference

            if sideA in radius and sideB in radius and angleA != 90:
               with self.canvas:
                    Color(1., 0, 0)
                    Line(points = [ 250, 250, 250 + sideA , 250, 250 + (sideB * np.cos(angleA)), 250 + (sideB * np.sin(angleA))], width = 2.5, cap = 'none', joint = 'round', close = True)

class Draw_triangle(App):
    def build(self):
        return main()


if __name__ == "__main__":
    Draw_triangle().run()
