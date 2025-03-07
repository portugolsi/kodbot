from pgzero.actor import Actor  

class Ball:
    def __init__(self, x, y, direction):
        self.actor = Actor("blue_ball")  # Substitua por um sprite adequado
        self.actor.pos = (x, y)
        self.speed = 7  # Velocidade da bola
        self.direction = direction  # Direção do tiro (1 para direita, -1 para esquerda)
        self.active = True  # Indica se a bola ainda está em jogo

    def launch(self, x, y, direction):
        """Reinicia a posição da bola e define a direção do disparo."""
        self.actor.pos = (x, y)
        self.direction = direction
        self.active = True

    def update(self):
        """Movimenta a bola na direção correta."""
        if self.active:
            self.actor.x += self.speed * self.direction
            # Remove a bola se sair da tela
            if self.actor.right < 0 or self.actor.left > 800:  
                self.active = False  

    def draw(self):
        """Desenha a bola se ela estiver ativa."""
        if self.active:
            self.actor.draw()
