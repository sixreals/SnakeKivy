from enum import Enum
from kivy.vector import Vector

class Direction(Enum):
    #1st value is x, 2nd is y
    #East is +ve x, north is +ve y
    Up = Vector(0,1)
    Down = Vector(0,-1)
    Left = Vector(-1,0)
    Right = Vector(1,0)