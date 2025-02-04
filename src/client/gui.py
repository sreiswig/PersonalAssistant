import sys
from PySide6 import QtCore, QtWidgets
from text_to_voice_model import TextToVoiceModel
from voice_to_text_model import VoiceToTextModel

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the model
        self.available_models = ["google/gemma-2-2b", "NovaSky-AI/Sky-T1-32B-Preview"]
        self.current_model_name = self.available_models[0]

        # Set up the layout
        self.main_layout = QtWidgets.QVBoxLayout(self)

        # Model selector dropdown
        self.model_selector = QtWidgets.QComboBox()
        self.model_selector.addItems(self.available_models)
        self.model_selector.currentTextChanged.connect(self.changeModel)
        self.main_layout.addWidget(self.model_selector)

        # Input Field
        self.textEdit = QtWidgets.QTextEdit()
        self.textEdit.setReadOnly(True)
        self.main_layout.addWidget(self.textEdit)

        # Input field
        self.inputField = QtWidgets.QLineEdit()
        self.inputField.setPlaceholderText("Type your message here...")
        self.inputField.returnPressed.connect(self.handleInput)
        self.main_layout.addWidget(self.inputField)

        # Submit button
        self.submitButton = QtWidgets.QPushButton("Send")
        self.submitButton.clicked.connect(self.handleInput)
        self.main_layout.addWidget(self.submitButton)

    def handleInput(self):
        user_input = self.inputField.text().strip()
        if user_input:
            self.textEdit.append(f"You: {user_input}")
            self.inputField.clear()

    def changeModel(self, model_name):
        self.textEdit.append(f"Changing model to: {model_name}")
        self.current_model_name = model_name
        try:
            self.textEdit.append(f"Successfully switched to {model_name}")
        except Exception as e:
            self.textEdit.append(f"Error initializing model {model_name}")

class App():
    def __init__(self):
        app = QtWidgets.QApplication([])
        widget = MyWidget()
        widget.resize(800, 600)
        widget.show()
        sys.exit(app.exec())

