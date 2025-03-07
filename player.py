from pgzero.actor import Actor  
from ball import Ball
class Player:
    def __init__(self, x, y):
        self.animations = {
            
            "idle": ["player_idle01","player_idle02","player_idle03"],
            "walk" : ["player_walking01.png","player_walking02.png",
                      "player_walking03.png","player_walking04.png","player_walking05.png",
                      "player_walking06.png","player_walking07.png","player_walking08.png",
                      ],
            "walkL" : ["player_walking_l01.png","player_walking_l02.png",
                      "player_walking_l03.png","player_walking_l04.png","player_walking_l05.png",
                      "player_walking_l06.png","player_walking_l07.png","player_walking_l08.png",
                      ],
        }
        self.actor = Actor("player_idle01") 
        self.actor.pos = (x, y)
        self.velocity_y = 0
        self.on_ground = False
        self.current_animation = "idle"
        self.animation_index = 0
        self.animation_timer = 0 
        self.facing = 1 
        self.projectiles = [] 

    def update(self,keyboard,platform):
        if keyboard.left or keyboard.right:
           
            if keyboard.left:
                self.actor.x -= 5
                self.current_animation = "walkL"
                self.facing = -1
            if keyboard.right:
                self.actor.x += 5
                self.current_animation = "walk"
                self.facing = 1
        else:
            self.current_animation = "idle"

        self.velocity_y += 0.5
        self.actor.y += self.velocity_y
        if self.actor.y + self.actor.height // 2 >= platform.top and self.actor.x > platform.left and self.actor.x < platform.right:
            self.actor.y = platform.top - self.actor.height // 2
            self.velocity_y = 0
            self.on_ground = True
        else:
            self.on_ground = False
        if keyboard.up and self.on_ground:
            self.velocity_y = -10
        if keyboard.X:
            self.shoot()
        for ball in self.projectiles:
            ball.update()
        
        self.update_animation()
    def draw(self):
        self.actor.draw()
        for ball in self.projectiles:
            ball.draw()
    def update_animation(self):
        self.animation_timer += 1
        if self.animation_timer >= 10:  
            self.animation_timer = 0
            self.animation_index = (self.animation_index + 1) % len(self.animations[self.current_animation])
            self.actor.image = self.animations[self.current_animation][self.animation_index]
    def shoot(self):
        new_ball = Ball(self.actor.x, self.actor.y, self.facing)
        self.projectiles.append(new_ball)