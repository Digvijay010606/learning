import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class MadLibsApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window title and size
        self.setWindowTitle("Mad Libs Generator")
        self.setGeometry(100, 100, 300, 200)

        # Create a vertical layout
        layout = QVBoxLayout()

        # Create labels and input fields
        self.label_noun = QLabel("Enter a noun:")
        self.entry_noun = QLineEdit()
        layout.addWidget(self.label_noun)
        layout.addWidget(self.entry_noun)

        self.label_verb = QLabel("Enter a verb:")
        self.entry_verb = QLineEdit()
        layout.addWidget(self.label_verb)
        layout.addWidget(self.entry_verb)

        self.label_adjective = QLabel("Enter an adjective:")
        self.entry_adjective = QLineEdit()
        layout.addWidget(self.label_adjective)
        layout.addWidget(self.entry_adjective)

        self.label_place = QLabel("Enter a place:")
        self.entry_place = QLineEdit()
        layout.addWidget(self.label_place)
        layout.addWidget(self.entry_place)

        # Create a button to generate the Mad Libs story
        self.button_generate = QPushButton("Generate Mad Libs")
        self.button_generate.clicked.connect(self.generate_mad_lib)
        layout.addWidget(self.button_generate)

        # Set the layout for the window
        self.setLayout(layout)

    def generate_mad_lib(self):
        # Get the input values from the entry widgets
        noun = self.entry_noun.text()
        verb = self.entry_verb.text()
        adjective = self.entry_adjective.text()
        place = self.entry_place.text()

        # Generate the Mad Libs story
        story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} in {place}."

        # Show the story in a message box
        QMessageBox.information(self, "Mad Libs Story", story)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MadLibsApp()
    window.show()
    sys.exit(app.exec_())