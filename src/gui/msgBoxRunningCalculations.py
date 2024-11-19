from PySide6 import QtWidgets, QtCore

class MsgBoxRunningCalculations(QtWidgets.QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Running Calculations")
        self.setText("Running calculations. Please wait.")
        self.setStandardButtons(QtWidgets.QMessageBox.NoButton)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        QtCore.QCoreApplication.processEvents()
        self.setModal(False)
        self.open()