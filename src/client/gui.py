import sys
import requests
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
        self.input_layout = QtWidgets.QHBoxLayout()

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
        self.input_layout.addWidget(self.submitButton)

        # Test server connection button
        self.testButton = QtWidgets.QPushButton("Test")
        self.testButton.clicked.connect(self.test)
        self.input_layout.addWidget(self.testButton)

        # Add Horizontal layout input widget
        self.input_widget = QtWidgets.QWidget()
        self.input_widget.setLayout(self.input_layout)
        self.main_layout.addWidget(self.input_widget)

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

    def test(self):
        response = requests.get("http://127.0.0.1:8000/")
        self.textEdit.append(f"Test: {response.json()}")
        

class App():
    def __init__(self):
        app = QtWidgets.QApplication([])
        window = MyWidget()
        window.resize(800, 600)
        window.show()
        sys.exit(app.exec())

