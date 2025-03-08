# Projeto: KodBot - Jogo em Pygame Zero

## Descrição
KodBot é um jogo criado com PG Zero onde o jogador controla um Robô que pode atirar projéteis para enfrentar inimigos a fim de se manter salvo.

## Como Jogar
- **Setas direcionais**: Movem o personagem
- **X**: Atira projéteis
- **Mouse**: Para clicar nos botões do menu

Mantenha-se em cima da plataforma e sem tocar nos inimigos para se manter vivo. 
Para isso, será necessário muita habilidade se desviando deles e atirando par as destuir.

## Estrutura do Projeto
```
├── main.py        # Arquivo principal do jogo
├── menu.py        # Tela de menu
├── player.py      # Controle do jogador
├── ball.py        # Comportamento dos projéteis
├── enemy.py       # Comportamento do inimigo
├── assets/        # Pasta com sprites e áudios que usei no projeto
|__ images/        # Animações dos personagens
|__ sounds/        # Música e efeitos sonoros utilizados no jogo
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
- Implementar sistema de pontuação 
- Criar diferentes tipos de projéteis
- Adicionar Gemes Juices para melhorar a experiência no jogo

## Autor
- **Jonadabe Santana (Dabe)**

