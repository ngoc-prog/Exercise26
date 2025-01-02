from PyQt6 import QtWidgets
from MainWindow import Ui_MainWindow


class MainWindowExt(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect buttons to their respective functions
        self.pushButtonInputdata.clicked.connect(self.input_data)
        self.pushButtonUppercase.clicked.connect(self.convert_uppercase)
        self.pushButtonLowercase.clicked.connect(self.convert_lowercase)
        self.pushButtonCountlowercasecharacters.clicked.connect(self.count_lowercase)
        self.pushButtonCountuppercaseletters.clicked.connect(self.count_uppercase)
        self.pushButtonPrintnumberofwordsperline.clicked.connect(self.print_words_per_line)
        self.pushButtonWordcount.clicked.connect(self.word_count)
        self.pushButtonPrintvowelsconsonants.clicked.connect(self.print_vowels_consonants)
        self.pushButtonExit.clicked.connect(self.close)

    def input_data(self):
        # Simply transfer text from input to output box for now
        input_text = self.lineEditInputdata.text()
        self.lineEditOutputdata.setText(input_text)

    def convert_uppercase(self):
        input_text = self.lineEditInputdata.text()
        self.lineEditOutputdata.setText(input_text.upper())

    def convert_lowercase(self):
        input_text = self.lineEditInputdata.text()
        self.lineEditOutputdata.setText(input_text.lower())

    def count_lowercase(self):
        input_text = self.lineEditInputdata.text()
        lowercase_count = sum(1 for char in input_text if char.islower())
        self.lineEditOutputdata.setText(f"Lowercase characters: {lowercase_count}")

    def count_uppercase(self):
        input_text = self.lineEditInputdata.text()
        uppercase_count = sum(1 for char in input_text if char.isupper())
        self.lineEditOutputdata.setText(f"Uppercase letters: {uppercase_count}")

    def print_words_per_line(self):
        input_text = self.lineEditInputdata.text()
        words = input_text.split()
        output = "\n".join([f"Line {i + 1}: {word}" for i, word in enumerate(words)])
        self.lineEditOutputdata.setText(output)

    def word_count(self):
        input_text = self.lineEditInputdata.text()
        words = input_text.split()
        self.lineEditOutputdata.setText(f"Total words: {len(words)}")

    def print_vowels_consonants(self):
        input_text = self.lineEditInputdata.text()
        vowels = 'aeiouAEIOU'

        vowel_count = sum(1 for char in input_text if char in vowels)
        consonant_count = sum(1 for char in input_text if char.isalpha() and char not in vowels)

        output = f"Vowels: {vowel_count}\nConsonants: {consonant_count}"
        self.lineEditOutputdata.setText(output)