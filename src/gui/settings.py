from PySide6.QtWidgets import QMainWindow, QWidget, QLabel

class Settings(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setGeometry(100, 100, 800, 600)
        self.setCentralWidget(QLabel("Settings"))
