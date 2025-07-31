import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from menu_projetos3 import Ui_MainWindow 
import sprites 

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
