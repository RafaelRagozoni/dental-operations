import sys
import json
import os
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QComboBox


class DentalUI:
    def inicialJanelaPessoas(self):
        self.janelaPessoas = QWidget()
        self.janelaPessoas.resize(900,500)
        self.janelaPessoas.setWindowTitle("Operações dentais do Dr. Sismoto")

    def inicialJanelaOperacoes(self):
        self.janelaOperations = QWidget()
        self.janelaOperations.resize(1600,900)
        self.janelaOperations.setWindowTitle("Operações do paciente")

    def addComboBoxJanela(self, position, janela):
        comboBox = QComboBox(janela)
        comboBox.move(position[0], position[1])
        return comboBox
    
    def addLabelJanela(self, text, position, janela, font_size=20):
        label = QLabel(text, janela)
        label.move(position[0], position[1])
        label.setStyleSheet(f'font-size:{font_size}px')
        return label
    
    def addButtonJanela(self, text, geometry, janela):
        button = QPushButton(text, janela)
        button.setGeometry(geometry[0], geometry[1], geometry[2], geometry[3])
        return button

    def adicionaElementosJanelaPaciente(self):
        self.combo_box_pacientes = self.addComboBoxJanela((20, 40), self.janelaPessoas)
        self.label_paciente = self.addLabelJanela("Paciente", (21, 10), self.janelaPessoas)
        self.label_name = self.addLabelJanela("", (300,220), self.janelaPessoas)
        self.label_cpf = self.addLabelJanela("", (300,270), self.janelaPessoas)
        self.label_birthday = self.addLabelJanela("", (300,320), self.janelaPessoas)
        self.label_last_seen = self.addLabelJanela("", (300,370), self.janelaPessoas)
        self.label_phone = self.addLabelJanela("", (300,420), self.janelaPessoas)
        self.label_number_procedure = self.addLabelJanela("", (300,470), self.janelaPessoas)
        self.static_label_name = self.addLabelJanela("Nome: ", (20,220), self.janelaPessoas)
        self.static_label_cpf = self.addLabelJanela("CPF", (20,270), self.janelaPessoas) 
        self.static_label_birthday = self.addLabelJanela("Dia de nascimento", (20,320), self.janelaPessoas)
        self.static_label_last_seen = self.addLabelJanela("Data ultima consulta", (20,370), self.janelaPessoas)
        self.static_label_phone = self.addLabelJanela("Telefone", (20,420), self.janelaPessoas)
        self.static_label_number_procedure = self.addLabelJanela("Numero de Procedimentos", (20,470), self.janelaPessoas)
        self.btn_ver_opc = self.addButtonJanela("Ver Operações do paciente", (400,20,400,50), self.janelaPessoas)

    def adicionaElementosJanelaOperacoes(self):
        self.combo_box_procedures = self.addComboBoxJanela((20, 40), self.janelaOperations)
        self.static_label_name_in_procedure = self.addLabelJanela("Nome: ", (20,220), self.janelaOperations)
        self.static_label_cpf_in_procedure = self.addLabelJanela("CPF: ", (20,270), self.janelaOperations)
        self.label_name_in_procedure = self.addLabelJanela("", (300,220), self.janelaOperations)
        self.label_cpf_in_procedure = self.addLabelJanela("", (300,270), self.janelaOperations)
        self.btn3 = self.addButtonJanela("Voltar para pacientes", (400,20,400,50), self.janelaOperations)

    def __init__(self):
        self.inicialJanelaPessoas()
        self.inicialJanelaOperacoes()
        self.adicionaElementosJanelaPaciente()
        self.adicionaElementosJanelaOperacoes()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = DentalUI()
    ui.janelaPessoas.show()
    sys.exit(app.exec())