from kivy.app import App
from kivy.uix.widget import Widget
#properties automatically bind to their references in their kv code
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
#for keyboard; documentation: https://kivy.org/doc/stable/api-kivy.core.window.html
from kivy.core.window import Window
from random import randint
from Utilities.Direction import Direction

class BodySection(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        this.position = Vector(0, 0)
        this.direction = Direction.Left