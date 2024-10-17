from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap
import sys

class ImageDisplayWindow(QMainWindow):
    def __init__(self, image_path):
        super().__init__()
        self.setWindowTitle("Image Display")

        # Create a label widget to display the image
        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap(image_path))

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)

        # Set the central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Path to your image file
    image_path = "test/testFiles/test_gen.png"

    window = ImageDisplayWindow(image_path)
    window.show()

    sys.exit(app.exec())