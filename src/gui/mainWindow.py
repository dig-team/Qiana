import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QMainWindow, QTextEdit, QMenuBar, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple PyQt6 Window")
        self.setGeometry(100, 100, 800, 600)
        self.editor = QTextEdit()
        self.display = QWebEngineView()
        self.menubar = QMenuBar()
        self.layout1 = QVBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout2.addWidget(self.editor)
        self.layout2.addWidget(self.display)
        self.layout1.addWidget(self.menubar)
        self.layout1.addLayout(self.layout2)
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(self.layout1)

