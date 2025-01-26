import sys
from PySide6 import QtCore, QtWidgets
from models import TextToTextModel

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the model
        config = {"model": "gpt2"}  # Replace with your desired model
        self.model = TextToTextModel(config)

        # Set up the layout
        self.main_layout = QtWidgets.QVBoxLayout(self)

        # Input field
        self.inputField = QtWidgets.QLineEdit()
        self.inputField.setPlaceholderText("Type your message here...")
        self.inputField.returnPressed.connect(self.handleInput)
        self.main_layout.addWidget(self.inputField)

        # Submit button
        self.submitButton = QtWidgets.QPushButton("Send")
        self.submitButton.clicked.connect(self.handleInput)
        self.main_layout.addWidget(self.submitButton)

        # Output area
        self.textEdit = QtWidgets.QTextEdit("Chat with the model:")
        self.textEdit.setReadOnly(True)
        self.main_layout.addWidget(self.textEdit)

    def handleInput(self):
        user_input = self.inputField.text().strip()
        if user_input:
            self.textEdit.append(f"You: {user_input}")
            response = self.model.run(user_input)
            self.textEdit.append(f"Model: {response}")
            self.inputField.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

