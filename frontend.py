import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setFixedSize(400, 200)
        self.setWindowTitle("Airplanes Database")

        add_button = QPushButton('Add to database', self)
        add_button.clicked.connect(self.click_method)
        add_button.move(50, 50)

        print_button = QPushButton('Print all data', self)
        print_button.clicked.connect(self.print_method)
        print_button.move(200, 50)

    def click_method(self):
        print("Added to database")

    def print_method(self):
        print("All data selected")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
