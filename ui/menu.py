from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectButton import DirectButton
from direct.gui.DirectFrame import DirectFrame


class MainMenu:
    """
    Classe responsável por gerenciar o menu principal do jogo.
    Controla todos os elementos visuais do menu, incluindo fundo, título e botões.
    """

    def __init__(self, game):
        """
        Inicializa o menu principal.

        Args:
            game: Instância principal do jogo (ArcanesmithGame)
        """
        self.game = game
        # Lista para manter registro de todos os elementos do menu para fácil limpeza
        self.elements = []
        # Configura os elementos visuais do menu
        self.setup_background()
        self.setup_title()
        self.setup_buttons()

    def setup_background(self):
        """
        Configura o painel de fundo do menu.
        Cria um frame escuro semi-transparente que cobre toda a tela.
        """
        self.background = DirectFrame(
            frameColor=(0, 0, 0, 0.8),  # Cor preta com 80% de opacidade
            frameSize=(-2, 2, -2, 2),  # Tamanho do frame (-X, +X, -Y, +Y)
            pos=(0, 0, 0),  # Posição central na tela
        )
        self.elements.append(self.background)

    def setup_title(self):
        """
        Configura o título do jogo e a informação da versão.
        Cria dois textos na tela: um para o título e outro para a versão.
        """
        # Título principal do jogo
        self.title = OnscreenText(
            text="Arcanesmith",
            style=1,  # Estilo do texto (1 = com borda)
            fg=(1, 0.8, 0, 1),  # Cor dourada (R, G, B, A)
            pos=(0, 0.7),  # Posição na tela (X, Y)
            scale=0.15,  # Tamanho do texto
            shadow=(0, 0, 0, 0.5),  # Sombra do texto (R, G, B, A)
        )
        self.elements.append(self.title)

        # Informação da versão
        self.version_info = OnscreenText(
            text="Version 1.0.0",
            style=1,
            fg=(0.7, 0.7, 0.7, 1),  # Cor cinza claro
            pos=(0, -0.95),  # Posição na parte inferior da tela
            scale=0.05,
        )
        self.elements.append(self.version_info)

    def setup_buttons(self):
        """
        Configura os botões do menu principal.
        Cria uma série de botões interativos com efeitos sonoros.
        """
        # Lista de tuplas (texto do botão, função a ser chamada)
        buttons = [
            ("New Game", self.game.start_new_game),
            ("Load Game", self.game.load_game),
            ("Options", self.game.show_options),
            ("Exit", self.game.exit_game),
        ]

        # Posição inicial Y dos botões
        button_y = 0.3

        # Cria cada botão do menu
        for text, command in buttons:
            button = DirectButton(
                text=text,
                scale=0.07,  # Escala do botão
                command=command,  # Função a ser chamada quando clicado
                pos=(0, 0, button_y),  # Posição do botão
                frameSize=(-4, 4, -0.5, 1),  # Tamanho do frame do botão
                text_fg=(1, 1, 1, 1),  # Cor do texto (branco)
                frameColor=(0.3, 0.3, 0.3, 0.8),  # Cor do fundo do botão
                relief=1,  # Tipo de relevo do botão
                # Sons de interação
                rolloverSound=self.game.loader.loadSfx("audio/button_rollover.ogg"),
                clickSound=self.game.loader.loadSfx("audio/button_click.ogg"),
            )
            self.elements.append(button)
            button_y -= 0.2  # Ajusta a posição Y para o próximo botão

    def destroy(self):
        """
        Remove todos os elementos do menu da tela.
        Chamado quando o menu precisa ser fechado.
        """
        for element in self.elements:
            element.destroy()
        self.elements.clear()
