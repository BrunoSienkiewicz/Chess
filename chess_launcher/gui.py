import context
import sys
from chess_launcher.chess_gamemodes import ClassicChess, FischerChess
from chess_launcher.ui_chess import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Stack.setCurrentIndex(0)


def guiMain(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
