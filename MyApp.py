import sys
from PyQt6.QtWidgets import QApplication
from MainWindowExt import MainWindowExt

def main():
    app = QApplication(sys.argv)
    window = MainWindowExt()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()