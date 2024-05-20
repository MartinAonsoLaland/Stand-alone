# This is an example for a script with s library and a GUI for testing purposes
# Try pyinstaller on this example

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
            
        self.setWindowTitle("Color Changer")
        self.setGeometry(200, 200, 400, 300)

        self.button_green = QPushButton("Green", self)
        self.button_green.setGeometry(100, 100, 100, 50)
        self.button_green.clicked.connect(self.change_to_green)

        self.button_red = QPushButton("Red", self)
        self.button_red.setGeometry(200, 100, 100, 50)
        self.button_red.clicked.connect(self.change_to_red)

    def change_to_green(self):
        self.setStyleSheet("background-color: green;")

    def change_to_red(self):
        self.setStyleSheet("background-color: red;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
