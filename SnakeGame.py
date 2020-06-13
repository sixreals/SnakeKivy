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
    def __init__(self, position, startDirection, **kwargs):
        super().__init__(**kwargs)
        self.pos = position
        self.direction = startDirection

    def move(self):
        self.pos = self.pos + self.direction.value

class SnakeGame(Widget):
    snake = ListProperty([])

    def __init__(self, **kwargs):
        super(SnakeGame, self).__init__(**kwargs)

        #set up keyboard
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)
    
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard = None

    #set velocity of paddle. acceleration is controled in paddle's move function
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        d = 1
        if keycode[1] == 'w':
            self.player1.velocity = self.player1.velocity if self.player1.velocity > d else d
        elif keycode[1] == 's':
            self.player1.velocity = self.player1.velocity if self.player1.velocity < -d else -d
        elif keycode[1] == 'd':
            self.player2.velocity = self.player2.velocity if self.player2.velocity > d else d
        elif keycode[1] == 'a':
            self.player2.velocity = self.player2.velocity if self.player1.velocity < -d else -d
        return True #return true to accept key, or it will be used by the system

    def _on_keyboard_up(self, keyboard, keycode):
        if keycode[1] == 'w' or keycode[1] == 's':
            self.player1.velocity = 0
        
        if keycode[1] == 'up' or keycode[1] == 'down':
            self.player2.velocity = 0
        
        return True

    def start(self):
        self.snake.append(BodySection(Vector(0,0), Direction.Left))

    def update(self, dt):
        #move each part
        for part in self.snake:
            part.move()
        
        #pass the direction onto each other part
        for ii in range(len(self.snake), 

class SnakeApp(App):
    def build(self):
        game = SnakeGame()
        game.start()
        #refresh game
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    SnakeApp().run()

