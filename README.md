# 🏃 Rumo aos 5K - Heading towards 5km

Um jogo 2D dinâmico desenvolvido em **Python** com a biblioteca **Pygame**, onde o jogador controla um corredor que deve evitar obstáculos enquanto corre em direção à marca de 5 quilômetros.

## 📋 Descrição

**Rumo aos 5K** é um jogo de corrida arcade desenvolvido como trabalho prático para a disciplina de **Programação Aplicada** na **UNINTER**. O objetivo é simples, mas desafiador: chegue aos 5.000 metros pulando sobre os obstáculos (buracos) que aparecem no caminho.

Quanto mais longe você corre, mais rápido os obstáculos chegam, tornando o jogo progressivamente mais difícil!

## 🎮 Mecânica do Jogo

- **Objetivo**: Atingir 5.000 metros sem colidir com os obstáculos
- **Controle**: Pressione **ESPAÇO** para pular
- **Dificuldade Progressiva**: A cada 1.000 metros, os obstáculos aumentam sua velocidade
- **Colisão**: Se o jogador colidir com um obstáculo, é Game Over
- **Vitória**: Atingir 5.000 metros com sucesso

## 📁 Estrutura do Projeto

```
Headingtowards5km/
├── main.py                 # Ponto de entrada do jogo
├── requirements.txt        # Dependências do projeto
├── main.spec              # Configuração para compilação (PyInstaller)
├── RumoAos5K.exe          # Executável compilado (Windows)
├── code/                  # Código-fonte do jogo
│   ├── Game.py           # Controlador principal com máquina de estados
│   ├── Level.py          # Gerencia a lógica de um nível
│   ├── Player.py         # Classe do jogador (corredor)
│   ├── Enemy.py          # Classe dos obstáculos (buracos)
│   ├── Background.py     # Gerencia o fundo animado
│   ├── Menu.py           # Menu inicial do jogo
│   ├── Entity.py         # Classe base para entidades do jogo
│   ├── const.py          # Constantes do jogo (cores, dimensões, estados)
│   └── __init__.py       # Inicializador do pacote
└── asset/                 # Recursos do jogo
    ├── corredor.png      # Sprite do jogador
    ├── buraco.png        # Sprite do obstáculo
    ├── trilha.wav        # Música de fundo
    └── pulo.wav          # Som do pulo
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pygame 2.6.1** - Biblioteca para desenvolvimento de jogos 2D
- **PyInstaller** - Para compilação em executável (.exe)

## 📦 Instalação e Configuração

### Pré-requisitos
- Python 3.7 ou superior instalado

### Passos para executar

1. **Clone ou baixe o repositório**:
   ```bash
   git clone https://github.com/iagofreire2/Headingtowards5km.git
   cd Headingtowards5km
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado)**:
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o jogo**:
   ```bash
   python main.py
   ```

### Executável Compilado (Windows)
Se preferir não instalar Python, você pode usar o arquivo `RumoAos5K.exe` incluído no repositório.

## 🎯 Como Jogar

1. **Menu Inicial**: Pressione **ENTER** para começar o jogo
2. **Durante o Jogo**: Pressione **ESPAÇO** para pular
3. **Evite os Obstáculos**: Não colida com os buracos que aparecem na tela
4. **Ganhe**: Atinja a marca de 5.000 metros
5. **Game Over/Vitória**: Pressione **ENTER** para voltar ao menu e jogar novamente

## 🎨 Recursos

- **Gráficos 2D**: Sprites personalizados para o jogador e obstáculos
- **Música e Sons**: Trilha sonora de fundo + efeitos sonoros
- **Máquina de Estados**: Sistema robusto para gerenciar diferentes estados do jogo (Menu, Gameplay, Game Over, Vitória)
- **Física Realista**: Sistema de gravidade para o pulo do jogador
- **Dificuldade Dinâmica**: Os obstáculos ficam progressivamente mais rápidos conforme o progresso

## 📊 Fluxo de Estados do Jogo

```
[MENU] --ENTER--> [LEVEL/GAMEPLAY] --VICTORY ou GAME OVER--> [VICTORY/GAME OVER] --ENTER--> [MENU]
```

## 📝 Notas de Desenvolvimento

- O jogo utiliza uma máquina de estados para controlar as transições entre Menu, Gameplay, Game Over e Vitória
- A dificuldade aumenta automaticamente a cada 1.000 metros percorridos
- Todos os assets (imagens e sons) estão armazenados na pasta `asset/`
- O código está bem comentado para facilitar a compreensão e futuros melhoramentos

## 🚀 Possíveis Melhorias Futuras

- Sistema de pontuação / ranking
- Múltiplos níveis com temas diferentes
- Power-ups ou bônus especiais
- Inimigos com padrões de movimento variados
- Tela de pausa
- Configuração de dificuldade inicial
- Modos de jogo alternativos (infinito, contra o tempo, etc.)

## 📄 Licença

Este projeto foi desenvolvido como trabalho acadêmico para a disciplina de Programação Aplicada na UNINTER.

## ✍️ Autor

Desenvolvido por **Iago Freire** para a UNINTER

---

**Divirta-se correndo rumo aos 5K! 🏃💨**