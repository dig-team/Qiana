from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton

class Settings:
    """
    Static class that saves the settings globally and provides a method to open the settings window.
    """

    # TODO : timeout setting
    # TODO : write list of special restricted symbols

    _settingsWindow : '_SettingsWindow' = None
    quotedVarsNumber : int | None = None
    timeOutValue : int | None = None

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

    def setTimeOutValue(value : str):
        """
        Sets the timeout value.
        """
        try:
            Settings.timeOutValue = int(value)
        except ValueError:
            pass

    def getQuotedVarsNumber() -> int:
        """
        Returns the number of quoted variables. If the number is not set, the default value 3 is returned.
        """
        if Settings.quotedVarsNumber is None: return 3
        return Settings.quotedVarsNumber
    
    def getTimeOutValue() -> int:
        """
        Returns the timeout value. If the value is not set, the default value 5 is returned.
        """
        if Settings.timeOutValue is None: return 5
        return Settings.timeOutValue

class _SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)

        mainLayout = QVBoxLayout()
        labelDecideVariables = QLabel("Number of quoted variables:")
        self.variableNumbrField = QLineEdit()
        labelDecideTimeout = QLabel("Max proof search duration (in seconds):")
        self.timeoutNumbrFiled = QLineEdit()

        validateButton = QPushButton("Ok")
        validateButton.clicked.connect(lambda: self.close())

        mainLayout.addWidget(labelDecideVariables)
        mainLayout.addWidget(self.variableNumbrField)
        mainLayout.addWidget(labelDecideTimeout)
        mainLayout.addWidget(self.timeoutNumbrFiled)
        mainLayout.addWidget(validateButton)
        self.mainWidget.setLayout(mainLayout)

    def close(self) -> bool:
        Settings.setQuotedVarsNumber(self.variableNumbrField.text())
        Settings.setTimeOutValue(self.timeoutNumbrFiled.text())
        return super().close()


