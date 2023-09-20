import arcade
import pandas as pd
from apple import Apple
from snake import Snake


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Turn and Move Example"


#  Main application class
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
        arcade.set_background_color(arcade.color.SAND)

        self.snake = Snake(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.apple = Apple(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.dataset = []

    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        self.snake.draw()
        self.apple.draw()
        
    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        data = {'w0':None,
                'w1':None,
                'w2':None,
                'w3':None,
                'a0':None,
                'a1':None,
                'a2':None,
                'a3':None,
                'b0':None,
                'b1':None,
                'b2':None,
                'b3':None,
                'direction':None }
        if self.snake.center_y > self.apple.center_y:
            self.snake.change_x = 0
            self.snake.change_y = -1
            data['direction'] = 2
        elif self.snake.center_y < self.apple.center_y:   
            self.snake.change_x = 0
            self.snake.change_y = 1 
            data['direction'] = 0
        elif self.snake.center_x > self.apple.center_x:   
            self.snake.change_x = -1
            self.snake.change_y = 0 
            data['direction'] = 3
        elif self.snake.center_x < self.apple.center_x:   
            self.snake.change_x = 1
            self.snake.change_y = 0 
            data['direction'] = 1

        if self.snake.center_x == self.apple.center_x and self.snake.center_y < self.apple.center_y:
            data['a0'] = 1  
            data['a1'] = 0 
            data['a2'] = 0
            data['a3'] = 0
        elif self.snake.center_x == self.apple.center_x and self.snake.center_y > self.apple.center_y:    
            data['a0'] = 0
            data['a1'] = 0
            data['a2'] = 1
            data['a3'] = 0
        elif self.snake.center_x < self.apple.center_x and self.snake.center_y == self.apple.center_y:
            data['a0'] = 0
            data['a1'] = 1
            data['a2'] = 0
            data['a3'] = 0
        elif self.snake.center_x > self.apple.center_x and self.snake.center_y == self.apple.center_y:    
            data['a0'] = 0
            data['a1'] = 0
            data['a2'] = 0
            data['a3'] = 1

        data['w0'] = SCREEN_HEIGHT - self.snake.center_y 
        data['w1'] = SCREEN_WIDTH - self.snake.center_x  
        data['w2'] = self.snake.center_y
        data['w3'] = self.snake.center_x


        for part in self.snake.body:
            if self.snake.center_x == part['center_x'] and self.snake.center_y < part['center_y']:
                data['b0'] = 1
                data['b1'] = 0
                data['b2'] = 0
                data['b3'] = 0
            elif self.snake.center_x == part['center_x'] and self.snake.center_y > part['center_y']:
                data['b0'] = 0
                data['b1'] = 0
                data['b2'] = 1
                data['b3'] = 0   
            elif self.snake.center_x < part['center_x'] and self.snake.center_y == part['center_y']:
                data['b0'] = 0
                data['b1'] = 1
                data['b2'] = 0
                data['b3'] = 0   
            elif self.snake.center_x > part['center_x'] and self.snake.center_y == part['center_y']:
                data['b0'] = 0
                data['b1'] = 0
                data['b2'] = 0
                data['b3'] = 1  

        self.dataset.append(data)
        self.snake.on_update(delta_time)
        self.apple.on_update()

        if arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat()
            self.apple = Apple(SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_key_release(self, symbol, modifiers: int):
         if symbol == arcade.key.Q:
             df = pd.DataFrame(self.dataset)
             df.to_csv('dataset/dataset.csv', index=False)
             arcade.close_window()
             exit(0)
             
       
if __name__ == "__main__":
    window = MyGame()
    arcade.run()
