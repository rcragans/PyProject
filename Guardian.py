from random import randint
class Guardian(object):
    def __init__(self):
        self.x = 256
        self.y = 512
        self.speed = 50
        self.should_move_down = False
        self.should_move_left = False
        self.should_move_right = False
        self.should_move_up = False
    def shouldMove(self, direction, start = True):
        if direction == "right":
            self.should_move_right = start
        if direction == "left":
            self.should_move_left = start
        if direction == "up":
            self.should_move_up = start
        if direction == "down":
            self.should_move_down = start
    def draw_me(self,w,h):
        if self.should_move_right:
            if self.x <= (w - 60):
                self.x += self.speed
        elif self.should_move_left:
            if self.x >= (20):
                self.x -= self.speed
        if self.should_move_down:
            # if self.y <= (h - 60):
            self.y += self.speed
        elif self.should_move_up:
            # if self.y >= (60):
            self.y -= self.speed
    
