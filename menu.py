from pygame import Rect

WIDTH = 800
HEIGHT = 600
class Menu:
    def __init__(self):
        self.option = ""  
        self.play_button = Rect((WIDTH // 2 - 100, 250), (200, 50))
        self.exit_button = Rect((WIDTH // 2 - 100, 350), (200, 50))
    def draw(self, screen):
        screen.clear()
        screen.fill((135,206,235))
        screen.draw.text("KodBot", (WIDTH // 2 - 150, 100), fontsize=50, color="yellow")
        screen.draw.filled_rect(self.play_button, "blue")
        screen.draw.filled_rect(self.exit_button, "red")
        screen.draw.text("JOGAR", (WIDTH // 2 - 40, 260), fontsize=40, color="white")
        screen.draw.text("SAIR", (WIDTH // 2 - 30, 360), fontsize=40, color="white")
    def on_mouse_down(self, pos):
        if self.play_button.collidepoint(pos):
            self.option = "playing"  
            print("botão foi clicado")
        elif self.exit_button.collidepoint(pos):
            exit()  
    
    