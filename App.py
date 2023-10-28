import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QHBoxLayout
from PyQt6.QtGui import QPalette, QColor


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class PushButton(QPushButton):
    def __innit__(self,text):
        self.setCentralWidget(QPushButton(text))

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        HBoxLayout = QHBoxLayout()


        butt1 = PushButton("Push Me1")
        butt2 = PushButton("Push Me2")
        butt3 = PushButton("Push Me3")
        butt4 = PushButton("Push Me4")

        HBoxLayout.addWidget(butt1)
        HBoxLayout.addWidget(butt2)
        HBoxLayout.addWidget(butt3)
        HBoxLayout.addWidget(butt4)

        widget = QWidget()
        widget.setLayout(HBoxLayout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()