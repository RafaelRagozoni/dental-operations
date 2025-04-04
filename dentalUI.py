import sys
import json
import os
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QComboBox

def func():
    labelSelec.setText(comboBoxTeste.currentText())
    labelSelec.adjustSize()

def abrir_janela2():
    janela2.setWindowTitle(comboBoxTeste.currentText())
    janela2.show()
    janela.destroy()

def abrir_janela1():
    janela.setWindowTitle(comboBoxTeste.currentText())
    janela.show()
    janela2.destroy()

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(500,400)
janela.setWindowTitle("Operações dentais do Dr. Sismoto")

janela2 = QWidget()
janela2.resize(500,400)

labelOpc = QLabel("Opção:", janela)
labelOpc.move(0,200)
labelOpc.setStyleSheet('font-size:20px')

labelSelec = QLabel("", janela)
labelSelec.move(10,220)
labelSelec.setStyleSheet('font-size:20px')


btn = QPushButton("Botao 1", janela)
btn.setGeometry(400,0,100,50)
btn.clicked.connect(func)

btn2 = QPushButton("next janela", janela)
btn2.setGeometry(400,200,100,50)
btn2.clicked.connect(abrir_janela2)

btn3 = QPushButton("next janela", janela2)
btn3.setGeometry(400,200,100,50)
btn3.clicked.connect(abrir_janela1)

# btn.setStyleSheet('background-color:black;color:yellow')

comboBoxTeste = QComboBox(janela)
lista = ["Java","Python","C++","JavaScript","Rust","Golang","Pearl","Julia"]
comboBoxTeste.addItems(lista)
comboBoxTeste.move(0,0)

janela.show()

app.exec()