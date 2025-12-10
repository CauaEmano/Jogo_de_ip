Projeto -> Jogo de IP (sem nome ainda)
projeto-jogo/
├── main.py                # Ponto de entrada (apenas inicia o jogo)
├── README.md              # Documentação do projeto
├── requirements.txt       # Dependências (pygame, etc.)
├── assets/                # Imagens, sons, fontes
│   ├── images/
│   └── sounds/
└── src/                   # Todo o código fonte
    ├── __init__.py        # Transforma a pasta em um pacote Python
    ├── settings.py        # Configurações globais (tamanho tela, FPS, cores)
    ├── core/              # Lógica essencial do motor do jogo
    │   ├── __init__.py
    │   ├── game.py        # Gerenciador de estados (Menu, Jogo, GameOver)
    │   └── events.py      # (Opcional) Gerenciador de inputs
    ├── entities/          # Objetos vivos do jogo
    │   ├── __init__.py
    │   ├── player.py      # Lógica do jogador
    │   └── enemy.py       # Lógica do Boss/Inimigos
    └── world/             # Cenário e fases
        ├── __init__.py
        ├── level.py       # Carregamento da fase
        └── platforms.py   # Chão e obstáculos