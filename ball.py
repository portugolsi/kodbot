from pgzero.actor import Actor  

class Ball:
    def __init__(self, x, y, direction):
        self.actor = Actor("blue_ball")  
        self.actor.pos = (x, y)
        self.speed = 7  
        self.direction = direction  
        self.active = True 

    def launch(self, x, y, direction):
        self.actor.pos = (x, y)
        self.direction = direction
        self.active = True

    def update(self):
        if self.active:
            self.actor.x += self.speed * self.direction
            if self.actor.right < 0 or self.actor.left > 800:  
                self.active = False  

    def draw(self):
        if self.active:
            self.actor.draw()
