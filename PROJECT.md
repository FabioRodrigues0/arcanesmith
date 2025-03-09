
# Arcanesmith - Documentação do Projeto

## Visão Geral

Arcanesmith é um jogo de RPG desenvolvido em Python utilizando o motor Panda3D. O jogo coloca o jogador no papel de um ferreiro arcano em um mundo de fantasia, onde ele pode criar itens mágicos, explorar regiões diversas, e enfrentar desafios místicos.

## Estrutura do Projeto

```
arcanesmith/
├── assets/              # Recursos gráficos e sonoros
│   ├── icons/           # Ícones do jogo
│   ├── models/          # Modelos 3D
│   ├── textures/        # Texturas
│   └── sounds/          # Efeitos sonoros e músicas
├── main.py              # Ponto de entrada do jogo
├── character.py         # Sistema de personagens
├── world.py             # Sistema de mundo e regiões
├── crafting.py          # Sistema de criação de itens
├── combat.py            # Sistema de combate
├── quest.py             # Sistema de missões
├── inventory.py         # Sistema de inventário
├── magic.py             # Sistema de magia
├── npc.py               # Sistema de personagens não-jogáveis
└── ui/                  # Interface do usuário
    ├── menu.py          # Menus do jogo
    ├── hud.py           # Interface durante o jogo
    └── dialog.py        # Sistema de diálogos
```

## Sistemas Principais

### Sistema de Personagem

O sistema de personagem permite ao jogador criar e personalizar seu próprio personagem, escolhendo entre diferentes classes, atributos e aparências. À medida que o jogo progride, o personagem pode ganhar experiência, subir de nível e melhorar suas habilidades.

### Sistema de Mundo

O mundo de Arcanesmith é dividido em várias regiões, cada uma com seu próprio clima, fauna, flora e desafios. O jogador pode viajar entre essas regiões, explorando calabouços, cidades, florestas e outros ambientes.

### Sistema de Crafting

O sistema de crafting é um dos aspectos centrais do jogo. Como um ferreiro arcano, o jogador pode coletar materiais pelo mundo e usá-los para criar armas, armaduras e itens mágicos. A qualidade dos itens depende da habilidade do ferreiro, dos materiais utilizados e do processo de criação.

### Sistema de Combate

O combate em Arcanesmith é baseado em turnos, com elementos estratégicos. O jogador pode usar diferentes armas, armaduras e feitiços para vencer seus inimigos. A posição no campo de batalha, os atributos do personagem e os itens equipados influenciam o resultado do combate.

### Sistema de Quests

O jogo conta com um sistema de missões que guia o jogador através da história principal e oferece desafios secundários. As escolhas feitas pelo jogador durante as missões podem afetar o desenrolar da história e a relação com outros personagens.

## Tecnologias Utilizadas

- **Panda3D**: Motor de jogo 3D utilizado como base para o desenvolvimento
- **Python**: Linguagem de programação principal
- **Git & GitHub**: Controle de versão e hospedagem do código-fonte
- **Semantic Release**: Gerenciamento automático de versões

## Roadmap de Desenvolvimento

### Fase 1: Estrutura Básica
- [x] Configuração do projeto e controle de versão
- [x] Implementação do loop principal do jogo
- [x] Sistema básico de personagem
- [x] Sistema básico de mundo

### Fase 2: Sistemas Principais
- [ ] Sistema completo de personagem
- [ ] Sistema de movimento e controles
- [ ] Sistema de inventário
- [ ] Interface de usuário básica

### Fase 3: Conteúdo do Jogo
- [ ] Sistema de combate
- [ ] Sistema de crafting
- [ ] Primeiro conjunto de quests
- [ ] Primeiras regiões do mundo

### Fase 4: Polimento
- [ ] Balanceamento do jogo
- [ ] Efeitos sonoros e música
- [ ] Melhorias na interface do usuário
- [ ] Testes e correção de bugs

### Fase 5: Lançamento
- [ ] Preparação para o lançamento
- [ ] Lançamento da versão 1.0
- [ ] Coleta de feedback
- [ ] Planejamento de atualizações futuras
```

Além disso, vamos criar um arquivo de estrutura inicial para permitir que o jogo seja importado como um módulo:
