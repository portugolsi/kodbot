from pgzero.actor import Actor

class Enemy:
    def __init__(self, x, y, speed=2):

        self.animations{
            "walk":[""],
            "walkl":[""]
        }

        self.actor = Actor("enemy")  
        self.actor.pos = (x, y)
        self.speed = speed  
        self.current_animation = ""

    def update(self, player):
       
        if player.actor.x > self.actor.x:
            self.actor.x += self.speed  
        elif player.actor.x < self.actor.x:
            self.actor.x -= self.speed  
        
      

    def draw(self):
      
        self.actor.draw()
