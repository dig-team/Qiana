import sys
from PySide6.QtWidgets import QApplication

from gui.mainWindow import MainWindow

def startGUI():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
