import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from menu_projetos_reduzido_2 import Ui_MainWindow  # UI convertida com pyside6-uic
import sprites  # Importa os recursos (ex: imagens)

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = App()
    janela.show()
    sys.exit(app.exec())
