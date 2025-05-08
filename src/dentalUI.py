import sys
import os
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QCheckBox,
    QPushButton,
    QLabel,
    QLineEdit,
    QComboBox,
)
from PyQt6.QtCore import Qt

procedimentos = [
    "Ausente (A)",
    "Extraído (E)",
    "Hígido (H)",
    "Hígido selado (Hs)",
    "Prótese parcial removível",
    "Prótese temporária",
    "Incluso (I)",
    "Prótese coronária / unitária",
    "Coroa (Co)",
    "Implante",
    "Pilar (P)",
    "Núcleo (Pino)",
    "Resto radicular (RR)",
    "Retração gengival (Rg)",
    "Cálculo dental (Cd)",
    "Extração inidicada (Ei)",
    "Selante indicado (Si)",
    "Fratura (Fr)",
    "Mancha branca ativa (M)",
    "Cariado (C)",
    "Restaurado (R)",
    "Cárie da raiz",
    "Restaurado com cárie (Rc)",
    "Raiz restaurada",
    "Necessita de tratamento endodôntico",
    "Possui lesõa de furca",
    "Tratamento endodôntico realizado",
    "Lesão de furca tratada",
]


class DentalUI:
    def inicialJanelaPessoas(self):
        self.janelaPessoas = QWidget()
        self.janelaPessoas.resize(900, 600)
        self.janelaPessoas.setWindowTitle("Operações dentais do Dr. Sismoto")

    def inicialJanelaOperacoes(self):
        self.janelaOperations = QWidget()
        self.janelaOperations.resize(1200, 900)
        self.janelaOperations.setWindowTitle("Operações do paciente")

    def inicialJanelaProcedimentos(self):
        self.janela_procedimentos = QWidget()
        self.janela_procedimentos.resize(1200, 600)
        self.janela_procedimentos.setWindowTitle("Operações do paciente")

    def addComboBoxJanela(self, position, janela):
        comboBox = QComboBox(janela)
        comboBox.move(position[0], position[1])
        return comboBox

    def addLabelJanela(self, text, position, janela, font_size=20):
        label = QLabel(text, janela)
        label.move(position[0], position[1])
        label.setStyleSheet(f"font-size:{font_size}px")
        return label

    def addButtonJanela(self, text, geometry, janela):
        button = QPushButton(text, janela)
        button.setGeometry(geometry[0], geometry[1], geometry[2], geometry[3])
        return button

    def addPixMapJanela(self, path, position, janela):
        pixmap = QPixmap(path)
        label = QLabel(janela)
        label.setPixmap(pixmap)
        label.move(position[0], position[1])
        return label

    def addCheckBoxJanela(self, position, janela, widhth=50, height=50):
        check_box = QCheckBox("", janela)
        check_box.move(position[0], position[1])
        return check_box

    def addLineEditJanela(self, position, janela):
        line = QLineEdit(janela)
        line.move(position[0], position[1])
        line.setStyleSheet("font-size:20px")
        return line

    def addTeethImages(self):
        images_path = "images"
        start_x = 100
        start_y = 400
        checkbox_y = 160
        contador = 0
        for image_file in os.listdir(images_path):
            image_path = os.path.join(images_path, image_file)
            tooth_id = image_file[:-4]
            self.addPixMapJanela(image_path, (start_x, start_y), self.janelaOperations)
            self.check_box_dentes[tooth_id] = self.addCheckBoxJanela(
                (start_x + 5, start_y + checkbox_y), self.janelaOperations
            )
            self.check_box_dentes[tooth_id].setStyleSheet(
                "QCheckBox::indicator { width: 50px; height: 50px;}"
            )
            start_x += 60
            contador += 1
            if contador == 16:
                start_x = 100
                start_y = 700
                checkbox_y = -50

    def adicionaElementosJanelaPaciente(self):
        self.combo_box_pacientes = self.addComboBoxJanela((20, 40), self.janelaPessoas)
        self.static_label_name_selected_pacient = self.addLabelJanela(
            "Desconhecido", (220, 40), self.janelaPessoas
        )
        self.label_paciente = self.addLabelJanela(
            "Paciente", (21, 10), self.janelaPessoas
        )
        self.static_label_name = self.addLabelJanela(
            "Nome: ", (20, 220), self.janelaPessoas
        )
        self.static_label_cpf = self.addLabelJanela(
            "CPF", (20, 270), self.janelaPessoas
        )
        self.static_label_birthday = self.addLabelJanela(
            "Dia de nascimento", (20, 320), self.janelaPessoas
        )
        self.static_label_phone = self.addLabelJanela(
            "Telefone", (20, 370), self.janelaPessoas
        )
        self.static_label_last_seen = self.addLabelJanela(
            "Data ultima consulta", (20, 420), self.janelaPessoas
        )
        self.static_label_number_procedure = self.addLabelJanela(
            "Numero de Procedimentos", (20, 470), self.janelaPessoas
        )
        self.line_name = self.addLineEditJanela((300, 220), self.janelaPessoas)
        self.line_cpf = self.addLineEditJanela((300, 270), self.janelaPessoas)
        self.line_birthday = self.addLineEditJanela((300, 320), self.janelaPessoas)
        self.line_phone = self.addLineEditJanela((300, 370), self.janelaPessoas)
        self.line_last_seen = self.addLabelJanela("", (300, 420), self.janelaPessoas)
        self.line_number_procedure = self.addLabelJanela(
            "", (300, 470), self.janelaPessoas
        )
        self.btn_ver_opc = self.addButtonJanela(
            "Operações do paciente", (600, 75, 250, 50), self.janelaPessoas
        )
        self.btn_cadastrar_novo_paciente = self.addButtonJanela(
            "Cadastrar novo paciente", (600, 175, 250, 50), self.janelaPessoas
        )
        self.btn_atualizar_paciente = self.addButtonJanela(
            "Atualizar dados de paciente", (600, 275, 250, 50), self.janelaPessoas
        )
        self.btn_salvar_paciente = self.addButtonJanela(
            "Salvar dados de novo paciente",
            (600, 375, 250, 50),
            self.janelaPessoas,
        )
        self.btn_delete_paciente = self.addButtonJanela(
            "Deletar paciente", (600, 475, 250, 50), self.janelaPessoas
        )

    def adicionaElementosJanelaOperacoes(self):
        self.combo_box_procedures = self.addComboBoxJanela(
            (20, 40), self.janelaOperations
        )
        self.static_label_name_in_procedure = self.addLabelJanela(
            "Nome: ", (20, 90), self.janelaOperations
        )
        self.static_label_cpf_in_procedure = self.addLabelJanela(
            "CPF: ", (20, 140), self.janelaOperations
        )
        self.static_label_date = self.addLabelJanela(
            "Data: ", (20, 190), self.janelaOperations
        )
        self.static_label_notes = self.addLabelJanela(
            "Notas: ", (20, 240), self.janelaOperations
        )
        self.line_name_in_procedure = self.addLabelJanela(
            "", (150, 90), self.janelaOperations
        )
        self.line_cpf_in_procedure = self.addLabelJanela(
            "", (150, 140), self.janelaOperations
        )
        self.line_date = self.addLabelJanela(
            "", (150, 190), self.janelaOperations
        )
        self.line_date.setFixedWidth(400)
        self.line_notes = self.addLineEditJanela((20, 270), self.janelaOperations)
        self.line_notes.setFixedSize(800, 100)
        self.line_notes.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.btn3 = self.addButtonJanela(
            "Voltar para pacientes", (400, 20, 400, 50), self.janelaOperations
        )
        self.btn_nova_consulta = self.addButtonJanela(
            "Cadastrar nova consulta", (400, 70, 400, 50), self.janelaOperations
        )
        self.btn_salvar_consulta = self.addButtonJanela(
            "Salvar/Atualizar consulta", (400, 120, 400, 50), self.janelaOperations
        )
        self.btn_deletar_consulta = self.addButtonJanela(
            "Deletar consulta", (400, 170, 400, 50), self.janelaOperations
        )
        self.check_box_dentes = {}
        self.addTeethImages()

    def adicionaElementosJanelaProcedimentos(self):
        self.btn_salvar_procedures = self.addButtonJanela(
            "Salvar", (400, 500, 400, 50), self.janela_procedimentos
        )
        self.check_box_procedimentos = {}
        start_x = 10
        start_y = 10
        for procedimento in procedimentos:
            self.check_box_procedimentos[procedimento] = self.addCheckBoxJanela(
                (start_x, start_y), self.janela_procedimentos
            )
            self.check_box_procedimentos[procedimento].setStyleSheet(
                "QCheckBox::indicator { width: 20px; height: 20px;}"
            )
            self.addLabelJanela(
                procedimento, (start_x + 30, start_y), self.janela_procedimentos
            )
            start_x += 400
            if start_x > 1200:
                start_x = 10
                start_y += 50

    def __init__(self):
        self.inicialJanelaPessoas()
        self.inicialJanelaOperacoes()
        self.inicialJanelaProcedimentos()
        self.adicionaElementosJanelaProcedimentos()
        self.adicionaElementosJanelaPaciente()
        self.adicionaElementosJanelaOperacoes()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = DentalUI()
    ui.janelaPessoas.show()
    sys.exit(app.exec())
