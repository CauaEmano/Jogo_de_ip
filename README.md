# Helicônia

> **Status do Projeto:** Em desenvolvimento

O jogo retrata a história de **Helicônia**, uma guerreira indígena abençoada por **Tupã** para derrotar o domínio de **Anhangá**.

## Equipe 💻

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/CauaEmano">
        <img src="https://github.com/CauaEmano.png" width="100px;" alt="Foto de Cauã Emanuel"/><br>
        <sub><b>Cauã Emanuel</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/MarcosMorais5228">
        <img src="https://github.com/MarcosMorais5228.png" width="100px;" alt="Foto de Marcos"/><br>
        <sub><b>Marcos</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Juaum-zim">
        <img src="https://github.com/Juaum-zim.png" width="100px;" alt="Foto de João Pedro"/><br>
        <sub><b>João Pedro</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/allanismaia42-boop">
        <img src="https://github.com/allanismaia42-boop.png" width="100px;" alt="Foto de Allanis"/><br>
        <sub><b>Allanis</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/ellesamarasllm">
        <img src="https://github.com/ellesamarasllm.png" width="100px;" alt="Foto de Elane"/><br>
        <sub><b>Elane</b></sub>
      </a>
    </td>
  </tr>
</table>

---

## 🏗️ Arquitetura do Jogo

O projeto segue uma estrutura modular.

```mermaid
graph TD
    %% Nós (Nodes)
    Main([🚀 main.py])
    
    subgraph Engine [⚙️ Core & Lógica]
        Game[🎮 Game Controller]
        CoreFiles[Camera, Events, UI, Bullet]
    end
    
    subgraph Map [🌍 Mundo]
        World[🗺️ Level & Platforms]
    end
    
    subgraph Actors [👾 Entidades]
        Player[🏃 Player]
        Enemy[💀 Enemy]
    end
    
    subgraph Items [📦 Objetos / Drops]
        Objs[⚡ Raio, 🥤 Guaraná, 🪁 Pipa, 🪨 Pedra]
    end

    %% Relações
    Main -->|Start| Game
    Game -->|Update| CoreFiles
    Game -->|Load| World
    Game -->|Spawn| Objs
    World -->|Contém| Player & Enemy
    CoreFiles -.->|Controla| Player
    
    %% Estilização (Cores)
    style Main fill:#f9f,stroke:#333,stroke-width:2px,color:black
    style Game fill:#bbf,stroke:#333,stroke-width:2px,color:black
    style Objs fill:#ff9,stroke:#e6b800,stroke-width:2px,stroke-dasharray: 5 5,color:black
    style Player fill:#bfb,stroke:#333,stroke-width:2px,color:black
    style Enemy fill:#fbb,stroke:#333,stroke-width:2px,color:black
```

## 📂 Estrutura de Diretórios

A organização do código-fonte (`src`) é dividida por responsabilidades:

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
    │   └── ui.py         # HUD e menus
    ├── 📂 entities       # Atores do jogo
    │   ├── player.py     # Lógica do jogador
    │   └── enemy.py      # Lógica dos inimigos
    ├── 📂 world          # Ambiente
    │   ├── level.py      # Carregamento de mapas
    │   └── platforms.py  # Colisões e estruturas
    └── 📂 objects        # Itens interagíveis
        └── items.py      # Gerenciamento dos coletáveis
```

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge\&logo=python\&logoColor=ffdd54)
![Pygame](https://img.shields.io/badge/Pygame-333333?style=for-the-badge\&logo=python\&logoColor=2ea44f)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow?style=for-the-badge)

<div align="center">
  <h3>📸 Gameplay</h3>
  <img src="assets/demo.gif" width="700px" />
</div>

## 🛠️ Ferramentas Utilizadas

Abaixo estão listadas as tecnologias, bibliotecas e serviços utilizados no desenvolvimento do projeto, bem como a motivação para a escolha de cada uma.

|  Categoria | Ferramenta                                                                                                                        | Justificativa                                                                                            |
| :--------: | :-------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| **Código** | <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" width="100px">              | Linguagem base do projeto, escolhida pela simplicidade e legibilidade.                                   |
| **Engine** | <img src="https://img.shields.io/badge/Pygame-333333?style=for-the-badge&logo=python&logoColor=2ea44f" width="100px">             | Biblioteca robusta para renderização 2D e gerenciamento do loop de jogo.                                 |
| **Lógica** | `random` (lib)                                                                                                                    | Essencial para a geração procedural de inimigos e spawns de itens, garantindo variabilidade ao gameplay. |
|   **IDE**  | <img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" width="100px"> | Suporte excelente a Python (via extensões) e terminal integrado.                                         |
| **Assets** | **Ludo.ai**                                                                                                                       | Ferramenta de IA utilizada para acelerar a geração criativa de sprites e conceitos visuais.              |
| **Edição** | **Ezgif**                                                                                                                         | Utilizado para manipulação, conversão e otimização de sprites e GIFs animados.                           |
| **Gestão** | <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white" width="100px">              | Centralização da documentação, brainstorms e organização das tarefas (Kanban) da equipe.                 |
|   **Git**  | <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" width="100px">              | Repositório central para versionamento de código e colaboração entre os membros.                         |


## 🤝 Squad & Atribuições

| Membro | Foco Principal | Contribuições Detalhadas |
| :--- | :--- | :--- |
| **Cauã** | ![Manager](https://img.shields.io/badge/Gestão_%26_Gameplay-blueviolet?style=flat-square) | Gerenciamento do projeto, roteiro, criação de inimigos menores, sistema de coletáveis (inventário) e colisões simples. |
| **Marcos** | ![Core](https://img.shields.io/badge/Engine_%26_Level-blue?style=flat-square) | Núcleo do sistema, construção de cenário (chão/plataformas), Menu Principal e sistema de vida/dano. |
| **João** | ![Player](https://img.shields.io/badge/Player_%26_Física-green?style=flat-square) | Desenvolvimento completo da classe `Player`, física de colisão, movimentação e polimento visual de assets. |
| **Allanis** | ![Design](https://img.shields.io/badge/Lead_Design_%26_AI-ff69b4?style=flat-square) | Direção de arte/design principal e implementação da lógica do Sub-Boss. |
| **Elane** | ![Creative](https://img.shields.io/badge/Story_%26_Boss-orange?style=flat-square) | Roteiro do jogo, desenvolvimento do Boss Principal e suporte na criação de sprites/design. |

## 🧠 Conceitos Acadêmicos Aplicados

Abaixo, detalhamos como os conceitos estudados na disciplina foram materializados no código do jogo.

| Conceito | Aplicação Prática | Onde Encontrar (Exemplos) |
| :--- | :--- | :--- |
| **Programação Orientada a Objetos (POO)** | Todo o jogo é baseado em classes. O Player, Inimigos e o próprio Jogo são objetos com atributos (vida, velocidade) e métodos (andar, atacar). | `src/entities/player.py`<br>`src/core/game.py` |
| **Herança** | Utilizamos classes base para criar variações. `Player` e `Enemy` herdam de uma classe `pygame.sprite.Sprite`. | `class Player(Entity): ...`<br>`class Enemy(Entity): ...` |
| **Estruturas de Repetição (Loops)** | O "Game Loop" é o coração do projeto, mantendo o jogo rodando quadro a quadro enquanto a condição for verdadeira. | `while self.running:` em `main.py` |
| **Estruturas de Dados (Listas/Grupos/Dicionários)** | Uso de Listas (ou Groups do Pygame) para gerenciar múltiplos inimigos, projéteis e plataformas simultaneamente. | `pygame.sprite.Group()`<br>`self.all_sprites` |
| **Modularização** | Divisão do código em múltiplos arquivos e pastas para facilitar a manutenção e separar responsabilidades. | Pastas `src/core`, `src/world`, `src/entities` |
| **Condicionais e Lógica Booleana** | Verificação de colisões (Se player toca no inimigo -> perde vida) e inputs de teclado. | `if event.type == QUIT:`<br>`if collision:` |