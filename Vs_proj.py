import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,\
QGridLayout, QPushButton, QHBoxLayout, QVBoxLayout, QButtonGroup,\
QLineEdit
from PyQt6.QtGui import QPalette, QColor


def StagesVidgets():

    HBoxLayout = QHBoxLayout()
    
    
    stg_butt_1 = PushButton("1 Stage")
    stg_butt_2= PushButton("2 Stage")
    stg_butt_3 = PushButton("3 Stage")
    stg_butt_4 = PushButton("4 Stage")
    
    HBoxLayout.addWidget(stg_butt_1)
    HBoxLayout.addWidget(stg_butt_2)
    HBoxLayout.addWidget(stg_butt_3)
    HBoxLayout.addWidget(stg_butt_4)

    return HBoxLayout


def Cell_size():

    HBoxLayout = QHBoxLayout()

    sz_butt_1 = PushButton("Cmall Sell")
    sz_butt_2 = PushButton("No cmall Sell")
    HBoxLayout.addWidget(sz_butt_1)
    HBoxLayout.addWidget(sz_butt_2)

    return HBoxLayout


def Operable_Butt():
    
    HBoxLayout = QHBoxLayout()

    op_butt_1 = PushButton("Operable")
    op_butt_2 = PushButton("Unoperable")
    HBoxLayout.addWidget(op_butt_1)
    HBoxLayout.addWidget(op_butt_2)

    return HBoxLayout


def Therapy_type():
    HBoxLayout = QHBoxLayout()

    th_butt_1 = PushButton("HLT")
    th_butt_2 = PushButton("IMMUNO")
    HBoxLayout.addWidget(th_butt_1)
    HBoxLayout.addWidget(th_butt_2)

    return HBoxLayout


def Doctor_patient_input():

    HBoxLayout = QHBoxLayout()
    doctor = QLineEdit()
    patient = QLineEdit()
    HBoxLayout.addWidget(doctor)
    HBoxLayout.addWidget(patient)
    
    return HBoxLayout


def MakeStagesHead():

    VBoxLayout = QVBoxLayout()

    stages_layout = StagesVidgets()
    size_sell_layout = Cell_size()
    operable_layout = Operable_Butt()
    therapy_layout = Therapy_type()
    doc_patient_inp = Doctor_patient_input()

    VBoxLayout.addLayout(doc_patient_inp)
    VBoxLayout.addLayout(stages_layout)
    VBoxLayout.addLayout(size_sell_layout)
    VBoxLayout.addLayout(operable_layout)
    VBoxLayout.addLayout(therapy_layout)

    return VBoxLayout


class PushButton(QPushButton):
    def __innit__(self,text):
        self.setCentralWidget(QPushButton(text))


class MainWindow(QMainWindow):


    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Lung Cancer Expert")


        stages_head = MakeStagesHead()

        widget = QWidget()
        widget.setLayout(stages_head)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
