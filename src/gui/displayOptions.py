from typing import Any

import os
import pydotplus
from PySide6.QtGui import QImage, QPixmap, QPalette
from PySide6.QtWidgets import QTabWidget, QTextEdit, QWidget, QHBoxLayout, QLabel, QScrollArea
from PySide6.QtWebEngineWidgets import QWebEngineView

class DisplayOptions(QTabWidget):
    closure : QTextEdit
    html : QWebEngineView

    def __init__(self):
        super().__init__()

        self.closure = QTextEdit()
        self.closure.setReadOnly(True)
        self.html = QWebEngineView()

        self.imageLabel = QLabel()
        self.imageLabel.setScaledContents(True)
        self.scrollAreaGraph = QScrollArea()
        self.scrollAreaGraph.setBackgroundRole(QPalette.Dark)
        self.scrollAreaGraph.setWidgetResizable(True)
        self.scrollAreaGraph.setWidget(self.imageLabel)

        self.addTab(self.html, "ProofTree")
        self.addTab(self.closure, "Closure")
        self.addTab(self.scrollAreaGraph, "Graph")

    def setClosure(self, closure : str):
        self.closure.setPlainText(closure)

    def setHtml(self, html : str):
        self.html.setHtml(html)

    def setGraph(self, dotTxt : str):
        """
        Set the graph image from the given dot file.
        """
        graph = pydotplus.graph_from_dot_data(dotTxt)
        graph.write_png("deleteme.png")
        pixmap = QPixmap("deleteme.png")
        width, height = pixmap.width(), pixmap.height()
        self.imageLabel.setPixmap(QPixmap(pixmap).scaled(width//2, height))
        os.remove("deleteme.png")

    def expandHtml(self):
        self.html.page().runJavaScript("""
            var x = document.getElementsByTagName("details");
            var i;
            for (i = 0; i < x.length; i++) {
                x[i].setAttribute("open", "true");
            } 
           """)

    def collapseHtml(self):
        self.html.page().runJavaScript("""
            var x = document.getElementsByTagName("details");
            var i;
            for (i = 0; i < x.length; i++) {
                x[i].open = false;
            } 
           """) 
