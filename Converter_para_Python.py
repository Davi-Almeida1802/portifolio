from PySide6.QtWidgets import QApplication, QDialog
from minha_interface import Ui_Dialog  # Ou Ui_MainWindow, depende do .ui

class MeuApp(QDialog):  # ou QMainWindow
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

app = QApplication([])
janela = MeuApp()
janela.show()
app.exec()

# pyside6-uic minha_interface.ui -o minha_interface.py ----> Execute no Terminal

# pyside6-rcc sprites/sprites.qrc -o sprites.py ----> Converter Imagens
# import sprites  # ← Isso é ESSENCIAL para Importar as Imagens
