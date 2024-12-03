import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
ui_file = "ui\\cadastrar_livro.ui"

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__()
        uic.loadUi(ui_file, self)

print(ui_file)

if __name__ == "__main__": 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())