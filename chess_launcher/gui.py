import context
import sys
from chess_launcher.chess_gamemodes import ClassicChess, FischerChess
from chess_classes.player import Player
from chess_launcher.ui_chess import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Stack.setCurrentIndex(0)
        (self._size, 
        self._first_player_name, self._second_player_name, 
        self._primary_color, self._secondary_color) = self._get_settings()
        self._size = int(self._size)
        self._setup_launcher()

    def _get_settings(self):
        with open("settings.txt") as file_handle:
            settings = file_handle.readline().split(",")
        return settings

    def _write_settings(self, size, first_player_name, second_player_name, primary_color, secondary_color):
        with open("settings.txt") as file_handle:
            params = (size, first_player_name, second_player_name, primary_color, secondary_color)
            settings = "".join(f"{param}," for param in params)
            file_handle.write(settings)

    def _setup_launcher(self):
        classic_chess_button = self.ui.classicChessButton_2
        fischer_chess_button = self.ui.fischerChessButton_2
        settings_button = self.ui.settingsButton
        classic_chess_button.clicked.connect(self._start_classic_chess)
        fischer_chess_button.clicked.connect(self._start_fischer_chess)
        settings_button.clicked.connect(self._go_to_settings)

    def _start_classic_chess(self):
        player1 = Player(self._first_player_name, "white")
        player2 = Player(self._second_player_name, "black")
        chess = ClassicChess(
            self._size, self._size//4, 
            player1, player2, 
            self._primary_color, self._secondary_color
        )
        chess.play()

    def _start_fischer_chess(self):
        player1 = Player(self._first_player_name, "white")
        player2 = Player(self._second_player_name, "black")
        chess = FischerChess(
            self._size, self._size//4, 
            player1, player2, 
            self._primary_color, self._secondary_color
        )
        chess.play()

    def _go_to_settings(self):
        self.ui.Stack.currentIndex(1)
        self.ui.sizeLineEdit.setPlaceholderText(self._size)
        self.ui.firstPlayerNameLineEdit.setPlaceholderText(self._first_player_name)
        self.ui.secondPlayerNameLineEdit.setPlaceholderText(self._second_player_name)
        self.ui.saveButton.clicked.connect(self._save_settings)
        self.ui.exitButton.clicked.connect(self._exit_settings)

    def _save_settings(self):
        size_line_edit = self.ui.sizeLineEdit
        first_player_name_line_edit = self.ui.firstPlayerNameLineEdit
        second_player_name_line_edit = self.ui.secondPlayerNameLineEdit
        line_edits = [
            (size_line_edit, self._size),
            (first_player_name_line_edit, self._first_player_name),
            (second_player_name_line_edit, self._second_player_name)
        ]
        for line_edit in line_edits:
            if line_edit[0].text() == "":
                continue
            self._change_setting(line_edit[0], line_edit[1])
            line_edit[0].clear()

    def _exit_settings(self):
        self.ui.Stack.currentIndex(0)

    def _change_setting(self, line_edit, setting):
        setting = line_edit.text()


def guiMain(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
