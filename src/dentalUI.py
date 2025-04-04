import sys
import json
import os
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QComboBox
import people_operations as po

db = po.PersonDatabase()
people_cpfs = db.get_all_people_names()
names = list(people_cpfs.keys())
cpfs = list(people_cpfs.values())

def showPerson():
    current_name = comboBoxPacientes.currentText()
    current_cpf = people_cpfs[comboBoxPacientes.currentText()]
    person = db.get_person(current_cpf)
    number_procedure = person["last_procedure_id"]
    label_cpf.setText(current_cpf)
    label_name.setText(current_name)
    label_last_seen.setText(person["last_seen"])
    label_birthday.setText(person["birth_date"])
    label_phone.setText(person["phone"])
    label_number_procedure.setText(f"{number_procedure}")
    btnVerOpc.setText(f"Ver Operações de {comboBoxPacientes.currentText()}")

def abrir_janela_opcs():
    janelaOperations.setWindowTitle(comboBoxPacientes.currentText())
    janelaOperations.show()
    janelaPessoas.destroy()

def abrir_janela_pacientes():
    janelaPessoas.setWindowTitle("Pacientes do Dr. Sismoto")
    janelaPessoas.show()
    janelaOperations.destroy()

app = QApplication(sys.argv)

janelaPessoas = QWidget()
janelaPessoas.resize(900,500)
janelaPessoas.setWindowTitle("Operações dentais do Dr. Sismoto")

janelaOperations = QWidget()
janelaOperations.resize(1600,900)

comboBoxPacientes = QComboBox(janelaPessoas)
comboBoxPacientes.addItems(names)
comboBoxPacientes.move(20,40)
comboBoxPacientes.currentIndexChanged.connect(showPerson)

label_paciente = QLabel("Paciente", janelaPessoas)
label_paciente.move(21,10)
label_paciente.setStyleSheet('font-size:20px')

label_name = QLabel("", janelaPessoas)
label_name.move(300,220)
label_name.setStyleSheet('font-size:20px')

label_cpf = QLabel("", janelaPessoas)
label_cpf.move(300,270)
label_cpf.setStyleSheet('font-size:20px')

label_birthday = QLabel("", janelaPessoas)
label_birthday.move(300,320)
label_birthday.setStyleSheet('font-size:20px')

label_last_seen = QLabel("", janelaPessoas)
label_last_seen.move(300,370)
label_last_seen.setStyleSheet('font-size:20px')

label_phone = QLabel("", janelaPessoas)
label_phone.move(300,420)
label_phone.setStyleSheet('font-size:20px')

label_number_procedure = QLabel("", janelaPessoas)
label_number_procedure.move(300,470)
label_number_procedure.setStyleSheet('font-size:20px')

static_label_name = QLabel("Nome: ", janelaPessoas)
static_label_name.move(20,220)
static_label_name.setStyleSheet('font-size:20px')

static_label_cpf = QLabel("CPF", janelaPessoas)
static_label_cpf.move(20,270)
static_label_cpf.setStyleSheet('font-size:20px')

static_label_birthday = QLabel("Dia de nascimento", janelaPessoas)
static_label_birthday.move(20,320)
static_label_birthday.setStyleSheet('font-size:20px')

static_label_last_seen = QLabel("Data ultima consulta", janelaPessoas)
static_label_last_seen.move(20,370)
static_label_last_seen.setStyleSheet('font-size:20px')

static_label_phone = QLabel("Telefone", janelaPessoas)
static_label_phone.move(20,420)
static_label_phone.setStyleSheet('font-size:20px')

static_label_number_procedure = QLabel("Numero de Procedimentos", janelaPessoas)
static_label_number_procedure.move(20,470)
static_label_number_procedure.setStyleSheet('font-size:20px')

btnVerOpc = QPushButton("Ver Operações do paciente", janelaPessoas)
btnVerOpc.setGeometry(400,20,400,50)
btnVerOpc.clicked.connect(abrir_janela_opcs)

btn3 = QPushButton("Voltar para pacientes", janelaOperations)
btn3.setGeometry(400,20,400,50)
btn3.clicked.connect(abrir_janela_pacientes)

# btn.setStyleSheet('background-color:black;color:yellow')

showPerson()
janelaPessoas.show()

app.exec()