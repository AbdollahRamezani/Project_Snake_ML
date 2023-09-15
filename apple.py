import random
import arcade

class Apple(arcade.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()

        self.center_x = random.randint(1, SCREEN_WIDTH) //8 * 8  # عدد رندم تولید شده مضربی از هشت است
        self.center_y = random.randint(1, SCREEN_HEIGHT) //8 * 8
        self.change_x = 0
        self.change_y = 0
        self.color = arcade.color.RED
        self.radius = 8
        self.width = 16
        self.height = 16

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)