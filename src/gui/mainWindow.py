import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QMainWindow, QTextEdit, QMenuBar, QWidget, QPushButton, QLineEdit
from PyQt6.QtWebEngineWidgets import QWebEngineView

from pipeline import basicTPTPtoHtml
import examples

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.variableNumber = None # For simplicity's sake, the number of variables decided by the user is saved within the window. If none, the default value is used.

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

    def setVariableNumber(self, number : str):
        try:
            self.variableNumber = int(number)
        except ValueError:
            pass

    def setTPTP(self, tptp : str):
        self.editor.setPlainText(tptp)

    def computeHtml(self):
        tptp = self.editor.toPlainText()
        html = basicTPTPtoHtml(tptp, self.variableNumber)
        self.display.setHtml(html)

    def expandHtml(self):
        self.display.page().runJavaScript("""
            var x = document.getElementsByTagName("details");
            var i;
            for (i = 0; i < x.length; i++) {
                x[i].setAttribute("open", "true");
            } 
           """)

    def collapseHtml(self):
        self.display.page().runJavaScript("""
            var x = document.getElementsByTagName("details");
            var i;
            for (i = 0; i < x.length; i++) {
                x[i].open = false;
            } 
           """)
    

class _MenuBar(QWidget):
    def __init__(self):
        super().__init__()
        self.menus = QMenuBar()
        self.exampleMenu = self.menus.addMenu("Examples")
        self.toolsMenu = self.menus.addMenu("Tools")
        self.computeHtml = QPushButton("Compute HTML")
        self.textFieldVariableNumber = QLineEdit("Optional: custom number of variables")
        self.setVariableNumber = QPushButton("Ok")

        self.layout1 = QHBoxLayout()
        self.layout1.addWidget(self.menus)
        self.layout1.addWidget(self.textFieldVariableNumber)
        self.layout1.addWidget(self.setVariableNumber)
        self.layout1.addWidget(self.computeHtml)
        self.computeHtml.setFixedSize(120, 40)
        self.setLayout(self.layout1)

    def connectToWindow(self, window : MainWindow):
        self.computeHtml.clicked.connect(window.computeHtml)
        self.setVariableNumber.clicked.connect(lambda : window.setVariableNumber(self.textFieldVariableNumber.text()))
        self._fillEXamples(window)
        self._fillTools(window)

    def _fillEXamples(self, window : MainWindow):
        example1Action = self.exampleMenu.addAction("Romeo and Juliet")
        example1Action.triggered.connect(lambda : window.setTPTP(examples.Example_RJbasic))

    def _fillTools(self, window : MainWindow):
        expandAction = self.toolsMenu.addAction("Expand formula tree")
        expandAction.triggered.connect(window.expandHtml)
        collapseAction = self.toolsMenu.addAction("Collapse formula tree")
        collapseAction.triggered.connect(window.collapseHtml)
