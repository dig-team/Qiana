from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton

class Settings:
    """
    Static class that saves the settings globally and provides a method to open the settings window.
    """

    _settingsWindow : '_SettingsWindow' = None
    quotedVarsNumber : int | None = None

    @classmethod
    def openSettings(cls):
        """
        Opens the settings window.
        """
        cls._settingsWindow = _SettingsWindow()
        cls._settingsWindow.show()

    def setQuotedVarsNumber(number : str):
        """
        Sets the number of quoted variables.
        """
        try:
            Settings.quotedVarsNumber = int(number)
        except ValueError:
            pass

    def getQuotedVarsNumber() -> int:
        """
        Returns the number of quoted variables. If the number is not set, the default value 3 is returned.
        """
        if Settings.quotedVarsNumber is None: return 3
        return Settings.quotedVarsNumber

class _SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)

        mainLayout = QVBoxLayout()
        labelDecideVariables = QLabel("Number of quoted variables:")
        self.variableNumbrField = QLineEdit()
        validateButton = QPushButton("Ok")
        validateButton.clicked.connect(lambda: self.close())

        mainLayout.addWidget(labelDecideVariables)
        mainLayout.addWidget(self.variableNumbrField)
        mainLayout.addWidget(validateButton)
        self.mainWidget.setLayout(mainLayout)

    def close(self) -> bool:
        Settings.setQuotedVarsNumber(self.variableNumbrField.text())
        return super().close()


