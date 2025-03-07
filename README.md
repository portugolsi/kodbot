# Projeto: KodBot - Jogo em Pygame Zero

## Descrição
KodBot é um jogo criado com Pygame Zero onde o jogador controla um personagem que pode atirar projéteis, enfrentar inimigos e explorar um mapa com câmera seguindo o personagem. 

## Como Jogar
- **Setas direcionais**: Movem o personagem
- **Barra de espaço**: Atira projéteis
- **ESC**: Sai do jogo
- **Mouse**: Para clicar nos botões do menu
- **Tecla X**: Dispara projétil

## Estrutura do Projeto
```
├── main.py        # Arquivo principal do jogo
├── menu.py        # Tela de menu
├── player.py      # Controle do jogador
├── ball.py        # Comportamento dos projéteis
├── enemy.py       # Inteligência do inimigo
├── assets/        # Pasta com sprites e áudio
└── README.md      # Documentação do projeto
```

## Instalação
1. Instale as bibliotecas necessárias para o funcionamento do game:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o jogo:
   ```bash
   pgzrun main.py
   ```

## Recursos Utilizados
- **Linguagem**: Python
- **Bibliotecas**: Pygame Zero, PyGame (Rect)

## Melhorias Futuras
- Implementar sistema de pontuação mais eficiente
- Criar diferentes tipos de projéteis
- Adicionar Juices

## Autor
- **Jonadabe Santana (Dabe)**

