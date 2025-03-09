from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from ui.menu import MainMenu


class ArcanesmithGame(ShowBase):
    """
    Classe principal do jogo que gerencia a janela, cenas e estados do jogo.
    Herda de ShowBase, que é a classe base do Panda3D.
    """

    def __init__(self):
        """Inicializa o jogo e configura os elementos básicos"""
        # Inicializa a classe base do Panda3D
        ShowBase.__init__(self)

        # Desativa o controle padrão da câmera com o mouse
        self.disableMouse()

        # Configura a posição inicial da câmera
        self.camera.setPos(0, -10, 0)  # (X, Y, Z)
        self.camera.lookAt(0, 0, 0)  # Olha para o centro da cena

        # Configura a janela do jogo
        self.set_window_properties()

        # Inicializa as variáveis do menu
        self.main_menu = None

        # Cria o menu principal
        self.create_main_menu()

    def set_window_properties(self):
        """
        Configura as propriedades da janela do jogo.
        Define título, tamanho e ícone da janela.
        """
        props = WindowProperties()
        props.setTitle("Arcanesmith")
        props.setSize(1280, 720)  # Resolução da janela
        props.setIconFilename("assets/icons/game_icon.ico")
        self.win.requestProperties(props)

    def create_main_menu(self):
        """
        Cria uma nova instância do menu principal.
        """
        self.main_menu = MainMenu(self)

    def start_new_game(self):
        """
        Inicia um novo jogo.
        Remove o menu principal e inicializa o estado de jogo.
        """
        if self.main_menu:
            self.main_menu.destroy()
            self.main_menu = None
        print("Starting new game...")  # Placeholder para lógica futura

    def load_game(self):
        """Carrega um jogo salvo anteriormente"""
        print("Loading game...")  # Placeholder para lógica futura

    def show_options(self):
        """Exibe o menu de opções do jogo"""
        print("Showing options...")  # Placeholder para lógica futura

    def exit_game(self):
        """Fecha o jogo"""
        self.userExit()


# Ponto de entrada do programa
if __name__ == "__main__":
    game = ArcanesmithGame()
    game.run()  # Inicia o loop principal do jogo
