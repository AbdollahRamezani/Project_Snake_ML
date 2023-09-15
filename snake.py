import arcade

class Snake(arcade.Sprite):
    """
    Sprite that turns and moves
    """
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()

        self.speed = 8
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2
        self.change_x = 1
        self.change_y = 0
        self.width = 16
        self.height = 16

        self.color1 = arcade.color.GREEN
        self.color2 = arcade.color.DARK_GREEN
        self.r = 8
        self.body = []
        self.body_size = 0

    def draw(self):
        for i, part in enumerate(self.body):
            if i % 2 == 0:
                arcade.draw_circle_filled(part['center_x'], part['center_y'], self.r, self.color2)
            else:
                arcade.draw_circle_filled(part['center_x'], part['center_y'], self.r, self.color1)
                
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color1)

    def eat(self):
            self.body_size += 1

    def on_update(self, delta_time: float = 1/60):
        self.body.append({'center_x': self.center_x, 'center_y': self.center_y})
        if len(self.body) > self.body_size:
            self.body.pop(0)
        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y