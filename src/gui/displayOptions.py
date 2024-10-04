from PySide6.QtWidgets import QTabWidget, QTextEdit, QWidget, QHBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView

class DisplayOptions(QTabWidget):
    closure : QTextEdit
    html : QWebEngineView

    def __init__(self):
        super().__init__()

        self.closure = QTextEdit()
        self.html = QWebEngineView()

        self.addTab(self.html, "ProofTree")
        self.addTab(self.closure, "Closure")

    def setClosure(self, closure : str):
        self.closure.setPlainText(closure)

    def setHtml(self, html : str):
        self.html.setHtml(html)

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



if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = DisplayOptions()
    window.show()
    sys.exit(app.exec_())
