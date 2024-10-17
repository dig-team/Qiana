from typing import Any

import os
import pydotplus
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QTabWidget, QTextEdit, QWidget, QHBoxLayout, QLabel
from PySide6.QtWebEngineWidgets import QWebEngineView

class DisplayOptions(QTabWidget):
    closure : QTextEdit
    html : QWebEngineView

    def __init__(self):
        super().__init__()

        self.closure = QTextEdit()
        self.closure.setReadOnly(True)
        self.html = QWebEngineView()
        self.graphImage = QWidget()
        self.graphLayout = QHBoxLayout(self.graphImage)
        self.imageLabel = QLabel()
        self.graphLayout.addWidget(self.imageLabel)

        self.addTab(self.html, "ProofTree")
        self.addTab(self.closure, "Closure")
        self.addTab(self.graphImage, "Graph")

    def setClosure(self, closure : str):
        self.closure.setPlainText(closure)

    def setHtml(self, html : str):
        self.html.setHtml(html)

    def setGraph(self, dotTxt : str):
        """
        Set the graph image from the given image data. Meant to be used with a raw png imgage, though other formats are implicitly supported.
        """
        graph = pydotplus.graph_from_dot_data(dotTxt)
        image = graph.write_png("deleteme.png")
        pixmap = QPixmap("deleteme.png")
        self.imageLabel.setPixmap(QPixmap(pixmap))
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
