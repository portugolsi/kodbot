from pygame import Rect

WIDTH = 800
HEIGHT = 600
class Menu:
    def __init__(self):
        self.option = ""  
        self.play_button = Rect((WIDTH // 2 - 200, 250), (400, 50))
        self.sounds_button = Rect((WIDTH // 2 - 200,350), (400, 50))
        self.exit_button = Rect((WIDTH // 2 - 200, 450), (400, 50))
        self.sound = True
    def draw(self, screen):
        screen.clear()
        screen.fill((135,206,235))
        screen.draw.text("KodBot", (WIDTH // 2 - 150, 100), fontsize=50, color="yellow")
        screen.draw.filled_rect(self.play_button, "blue")
        screen.draw.filled_rect(self.sounds_button, "green")
        screen.draw.filled_rect(self.exit_button, "red")
        screen.draw.text("COMEÇAR JOGO", (WIDTH // 2 - 140, 260), fontsize=40, color="white")
        screen.draw.text("SONS LIGAR/DESLIGAR", (WIDTH // 2 - 140, 360), fontsize=40, color="white")
        screen.draw.text("SAÍDA", (WIDTH // 2 - 130, 460), fontsize=40, color="white")
    def on_mouse_down(self, pos):
        if self.play_button.collidepoint(pos):
            self.option = "playing"  
            print("botão foi clicado")
        elif self.sounds_button.collidepoint(pos):
            if self.sound:
                self.sound = False
            else:
                self.sound = True
        elif self.exit_button.collidepoint(pos):
            exit()  
    