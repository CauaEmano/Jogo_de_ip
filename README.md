# Helicônia

> **Status do Projeto:** Em desenvolvimento

O jogo retrata a história de helicônia, uma guerreira indígena, abençoada por Tupã para derrotar o domínio de Anhangá.

## Equipe 💻

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/CauaEmano">
        <img src="https://github.com/CauaEmano.png" width="100px;" alt="Foto de Cauã Emanuel"/><br>
        <sub>
          <b>Cauã Emanuel</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/MarcosMorais5228">
        <img src="https://github.com/MarcosMorais5228.png" width="100px;" alt="Foto de Marcos"/><br>
        <sub>
          <b>Marcos</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Juaum-zim">
        <img src="https://github.com/Juaum-zim.png" width="100px;" alt="Foto de João Pedro"/><br>
        <sub>
          <b>João Pedro</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/allanismaia42-boop">
        <img src="https://github.com/allanismaia42-boop.png" width="100px;" alt="Foto de Allanis"/><br>
        <sub>
          <b>Allanis</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/ellesamarasllm">
        <img src="https://github.com/ellesamarasllm.png" width="100px;" alt="Foto de Elane"/><br>
        <sub>
          <b>Elane</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

---
## 🏗️ Arquitetura do Jogo

O projeto segue uma estrutura modular.

classDiagram
    class Main {
        +run()
    }
    class Game {
        +gerar_itens()
        +carregar_nivel()
    }
    class Objetos {
        +Guarana
        +Pipa
        +Raio
        +Pedra
    }
    class World {
        +Level
        +Platforms
    }
    class Entities {
        +Player
        +Enemy
    }
    class Core {
        +Camera
        +Events
        +UI
        +Game_Logic
        +Bullet
    }

    Main --> Game : Inicializa
    Game --> World : Carrega Mapa
    Game --> Core : Gerencia Sistemas
    Game --> Objetos : Gera (Spawns)
    World --> Entities : Contém
    Core ..> Entities : Renderiza/Controla

## 📂 Estrutura de Diretórios

A organização do código fonte (`src`) é dividida por responsabilidades:

```text
📂 JOGO_DE_IP
├── 📄 main.py            # Ponto de entrada (Entry Point)
├── 📂 assets             # Sprites, sons e fontes
└── 📂 src
    ├── 📂 core           # Motor do jogo
    │   ├── bullet.py     # Ataque do player
    │   ├── game.py       # Loop principal e lógica de estado
    │   ├── camera.py     # Sistema de câmera (scroll)
    │   ├── events.py     # Gerenciador de inputs
    |   ├── camera.py     # Gerencia a câmera que acompanha o player
    │   └── ui.py         # HUD e Menus
    ├── 📂 entities       # Atores do jogo
    │   ├── player.py     # Lógica do jogador
    │   └── enemy.py      # Lógica dos inimigos
    ├── 📂 world          # Ambiente
    │   ├── level.py      # Carregamento de mapas
    │   └── platforms.py  # Colisões e estruturas
    └── 📂 objects        # Itens interagíveis
        └── items.py      # Gerencia os coletáveis

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pygame](https://img.shields.io/badge/Pygame-333333?style=for-the-badge&logo=python&logoColor=2ea44f)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow?style=for-the-badge)