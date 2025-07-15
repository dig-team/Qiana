import sys
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QMainWindow, QTextEdit, QMenuBar, QWidget, QPushButton, QLineEdit
from PySide6.QtWebEngineWidgets import QWebEngineView

from qiana.pipeline import QianaPipeline

import qiana.examples as examples
from qiana.gui import DisplayOptions, Settings

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Qiana")
        self.setGeometry(100, 100, 800, 600)

        self.menubar = _MenuBar()
        self.setMenuWidget(self.menubar)
        self.menubar.connectToWindow(self)

        self.editor = QTextEdit()
        self.display = DisplayOptions()
        self.layout2 = QHBoxLayout()
        self.layout2.addWidget(self.editor)
        self.layout2.addWidget(self.display)
        self.layout2.setStretch(0, 1)
        self.layout2.setStretch(1, 2)
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(self.layout2)

    def setVariableNumber(self, number : str):
        self.variableNumber = number

    def setTPTP(self, tptp : str):
        self.editor.setPlainText(tptp)

    def getClosure(self):
        tptp = self.editor.toPlainText()
        pipeline = QianaPipeline()
        pipeline.compute_qiana_closure(tptp)
        self.display.setClosure(pipeline.get_qiana_closure())

    def run(self):
        tptp = self.editor.toPlainText()
        pipeline = QianaPipeline()
        pipeline.runCompute_GUI(tptp)
        self.display.setHtml(pipeline.getHtmlTree())
        self.display.setClosure(pipeline.get_qiana_closure())
        self.display.setGraph(pipeline.get_graphdot())

    def expandHtml(self):
        self.display.expandHtml()

    def collapseHtml(self):
        self.display.collapseHtml()    
    
    def openSettings(self):
        Settings.openSettings()

class _MenuBar(QWidget):
    def __init__(self):
        super().__init__()
        self.menus = QMenuBar()
        self.exampleMenu = self.menus.addMenu("Examples")
        self.toolsMenu = self.menus.addMenu("Tools")
        self.closureButton = QPushButton("Get Closure")
        self.runButton = QPushButton("Run")

        self.layout1 = QHBoxLayout()
        self.layout1.addWidget(self.menus)
        self.layout1.addWidget(self.closureButton)
        self.layout1.addWidget(self.runButton)
        self.closureButton.setFixedSize(120, 40)
        self.runButton.setFixedSize(120, 40)
        self.setLayout(self.layout1)

    def connectToWindow(self, window : MainWindow):
        self.closureButton.clicked.connect(window.getClosure)
        self.runButton.clicked.connect(window.run)
        self._fillEXamples(window)
        self._fillTools(window)

    def _fillEXamples(self, window : MainWindow):
        example1Action = self.exampleMenu.addAction("Romeo and Juliet")
        example1Action.triggered.connect(lambda : window.setTPTP(examples.Example_RJbasic))
        example2Action = self.exampleMenu.addAction("Signature Test")
        example2Action.triggered.connect(lambda : window.setTPTP(examples.Example_SingatureTest))
        example3Action = self.exampleMenu.addAction("Simple Romeo and Juliet")
        example3Action.triggered.connect(lambda : window.setTPTP(examples.Example_RJsimple))

    def _fillTools(self, window : MainWindow):
        expandAction = self.toolsMenu.addAction("Expand formula tree")
        expandAction.triggered.connect(window.expandHtml)
        collapseAction = self.toolsMenu.addAction("Collapse formula tree")
        collapseAction.triggered.connect(window.collapseHtml)
        openSettings = self.toolsMenu.addAction("Settings")
        openSettings.triggered.connect(window.openSettings)

