from pgzero.actor import Actor

class Enemy:
    def __init__(self, x, y, speed=2, gravity=1):
        self.animations = {
            "falling": ["zombie_falling"],
            "walk": [
                "zombie_w_1","zombie_w_2","zombie_w_3",
                "zombie_w_4","zombie_w_5","zombie_w_6",
                "zombie_w_7","zombie_w_8","zombie_w_9",
                     ],
            "walkl": ["zombie_l_1","zombie_l_2","zombie_l_3",
                "zombie_l_4","zombie_l_5","zombie_l_6",
                "zombie_l_7","zombie_l_8","zombie_l_9",]
        }

        self.actor = Actor("zombie_falling")  
        self.actor.pos = (x, y)
        self.speed = speed  
        self.gravity = gravity  
        self.current_animation = "falling"
        self.animation_index = 0
        self.animation_timer = 0 
        self.ground_y =320  
        self.on_ground = False
        

    def update(self, player):
        if self.actor.y < self.ground_y:
            self.actor.y += self.gravity  
        else:
            self.actor.y = self.ground_y  

        if self.actor.y >= self.ground_y:  
            if player.actor.x > self.actor.x:
                self.current_animation = "walk"
                self.actor.x += self.speed  
            elif player.actor.x < self.actor.x:
                self.current_animation = "walkl"
                self.actor.x -= self.speed  

   

        self.update_animation()
    
    def update_animation(self):
        self.animation_timer += 1
        if self.animation_timer >= 10:  
            self.animation_timer = 0
            self.animation_index = (self.animation_index + 1) % len(self.animations[self.current_animation])
            self.actor.image = self.animations[self.current_animation][self.animation_index]


    def draw(self):
        self.actor.draw()

"""    def check_collision(bullets):
        for bullet in bullets:
           if self.actor.colliderect(bullet.actor):
               print("bala bateu no Enemy") """   