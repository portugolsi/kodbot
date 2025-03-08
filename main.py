import random
from player import Player
from pygame import Rect
from menu import Menu
from enemy import Enemy
WIDTH = 800
HEIGHT = 600

game_state = "menu"
menu = Menu()
player = Player(400, 500)
platform = Rect((100, 450), (600, 20))
enemies = []  
bullets = []

def spawn_enemy():
    if game_state == "playing":
        x = random.randint(50, WIDTH - 50)  
        new_enemy = Enemy(x, 0)  
        enemies.append(new_enemy)  
        next_spawn = random.uniform(5, 10)  
        clock.schedule(spawn_enemy, next_spawn) 

def update():
    global game_state,bullets
    if game_state == "playing":
        player.update(keyboard, platform)
        for enemy in enemies:
            enemy.update(player)  
        
    if menu.sound:
        sounds.fundo.play()
    else:
        sounds.fundo.stop()
    
    if player.actor.y > HEIGHT:
        player.actor.pos = (400,500)
        game_state = "menu"

    check_collision()

def check_collision():
    global game_state
    for enemy in enemies:
        if player.actor.colliderect(enemy.actor):  
            print("Colisão detectada!")
            game_state = "menu"
    
    for bullet in player.projectiles: 
        for enemy in enemies:
            if bullet.actor.colliderect(enemy.actor):
                print("Bala pegou no inimigo")
                enemies.remove(enemy)  
                player.projectiles.remove(bullet) 
                break  

   
"""
def check_collision():
    global game_state
    for enemy in enemies:
        if player.actor.colliderect(enemy.actor):  
        #if enemy.actor.pos == player.actor.pos:
            print("Colisao detectada!")
            game_state = "menu"
    
    for bullet in bullets:
        for enemy in enemies:
            if bullet.actor.colliderect(enemy.actor):
             print("Bala pegou no inimigo")
"""
    

def draw():
    screen.clear()  
    if game_state == "menu":
        menu.draw(screen)
    elif game_state == "playing":
        screen.fill((135, 206, 235))
        screen.draw.filled_rect(platform, "green")
        player.draw()
        for enemy in enemies:
            enemy.draw()  

def on_mouse_down(pos):
    global game_state   
    if game_state == "menu":  
        menu.on_mouse_down(pos)      
        if menu.option == "playing":
            sounds.button_click.play()
            game_state = "playing"
            music.stop() 
            enemies.clear()
            spawn_enemy()  
