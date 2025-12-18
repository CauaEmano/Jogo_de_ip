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

```mermaid
classDiagram
    class Main {
        +run()
    }
    class Game {
        +update()
        +draw()
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
    }

    Main --> Game : Inicializa
    Game --> World : Carrega Mapa
    Game --> Core : Gerencia Sistemas
    World --> Entities : Contém
    Core ..> Entities : Renderiza/Controla