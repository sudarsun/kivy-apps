#!/usr/bin/env python3

from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.floatlayout import FloatLayout

class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 10.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=10)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):

    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()

        button_layout = FloatLayout(size=(500,500))

        predictbtn = Button(text='Predict', font_size=40, size_hint=(.3, .1), pos=(50,50))
        predictbtn.bind(on_release=self.clear_canvas)

        button_layout.add_widget(predictbtn)

        clearbtn = Button(text='Clear', font_size=40, size_hint=(.3, .1), pos=(220, 50))
        clearbtn.bind(on_release=self.clear_canvas)

        button_layout.add_widget(clearbtn)

        parent.add_widget(button_layout)
        parent.add_widget(self.painter)

        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


if __name__ == '__main__':
    MyPaintApp().run()