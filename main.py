from player import Player
from pygame import Rect
from menu import Menu

WIDTH = 800
HEIGHT = 600

game_state = "menu"
menu = Menu()
player = Player(400, 500)
platform = Rect((100, 450), (600, 20))
sounds.fundo.play()

def update():
    global game_state
    if game_state == "playing":
        player.update(keyboard, platform)
def draw():
    screen.clear()  
    if game_state == "menu":
        menu.draw(screen)
    elif game_state == "playing":
        screen.fill((135, 206, 235))
        screen.draw.filled_rect(platform, "green")
        player.draw()
def on_mouse_down(pos):
    global game_state   
    if game_state == "menu":  
        menu.on_mouse_down(pos)      
        if menu.option == "playing":
            sounds.button_click.play()
            game_state = "playing"
            music.stop() 


