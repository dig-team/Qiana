import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QMainWindow, QTextEdit, QMenuBar, QWidget, QPushButton
from PyQt6.QtWebEngineWidgets import QWebEngineView

from pipeline import basicTPTPtoHtml
import examples

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple PyQt6 Window")
        self.setGeometry(100, 100, 800, 600)

        self.menubar = _MenuBar()
        self.setMenuWidget(self.menubar)
        self.menubar.connectToWindow(self)

        self.editor = QTextEdit()
        self.display = QWebEngineView()
        self.display.setHtml("<h1>Display</h1>")
        self.layout2 = QHBoxLayout()
        self.layout2.addWidget(self.editor)
        self.layout2.addWidget(self.display)
        self.layout2.setStretch(0, 1)
        self.layout2.setStretch(1, 1)
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(self.layout2)

        self.menubar.computeHtml.clicked.connect(self.computeHtml)

    def setTPTP(self, tptp : str):
        self.editor.setPlainText(tptp)

    def computeHtml(self):
        tptp = self.editor.toPlainText()
        html = basicTPTPtoHtml(tptp)
        self.display.setHtml(html)
    

class _MenuBar(QWidget):
    def __init__(self):
        super().__init__()
        self.menus = QMenuBar()
        self.exampleMenu = self.menus.addMenu("Examples")
        self.computeHtml = QPushButton("Compute HTML")

        self.layout1 = QHBoxLayout()
        self.layout1.addWidget(self.menus)
        self.layout1.addWidget(self.computeHtml)
        self.computeHtml.setFixedSize(120, 40)
        self.setLayout(self.layout1)

    def connectToWindow(self, window : MainWindow):
        self.computeHtml.clicked.connect(window.computeHtml)
        self._fillEXamples(window)

    def _fillEXamples(self, window : MainWindow):
        example1Action = self.exampleMenu.addAction("Romeo and Juliet")
        example1Action.triggered.connect(lambda : window.setTPTP(examples.Example_RJbasic))
