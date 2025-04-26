import sys
import json
import os
from datetime import datetime
from PyQt6.QtWidgets import QApplication
import src.dentalUI as dental_ui
# import dentalUI as dental_ui
# import people_operations as po

class UserInterfaceActions:
    def connect_btn_functions(self, btn, function):
        btn.clicked.connect(function)      

    def connect_combo_box_functions(self, combo_box, function):
        combo_box.currentIndexChanged.connect(function)      

    def connect_check_box_functions(self, check_box, function):
        check_box.toggled.connect(function)

    def showPerson(self):
        current_name = self.ui.combo_box_pacientes.currentText()
        current_cpf = self.people_cpfs[self.ui.combo_box_pacientes.currentText()]
        person = self.db.get_person(current_cpf)
        number_procedure = person["last_procedure_id"]
        self.ui.line_cpf.setText(current_cpf)
        self.ui.line_name.setText(current_name)
        self.ui.line_last_seen.setText(person["last_seen"])
        self.ui.line_birthday.setText(person["birth_date"])
        self.ui.line_phone.setText(person["phone"])
        self.ui.line_number_procedure.setText(f"{number_procedure}")
        self.ui.btn_ver_opc.setText(f"Ver Operações de {self.ui.combo_box_pacientes.currentText()}")
        self.ui.line_name_in_procedure.setText(current_name)
        self.ui.line_cpf_in_procedure.setText(current_cpf)

    def abrir_janela_opcs(self):
        self.ui.janelaOperations.setWindowTitle(self.ui.combo_box_pacientes.currentText())
        self.ui.janelaOperations.show()
        procedures_id = self.db.get_person_dental_procedures_id(self.ui.line_cpf_in_procedure.text())
        self.ui.combo_box_procedures.addItems(procedures_id)
        self.ui.janelaPessoas.destroy()

    def abrir_janela_pacientes(self):
        self.ui.janelaPessoas.setWindowTitle("Pacientes do Dr. Sismoto")
        self.ui.combo_box_procedures.clear()
        self.ui.janelaPessoas.show()
        self.ui.janelaOperations.destroy()

    def abrir_janela_procedimentos(self, checked):
        if not checked:
            try:
                self.ui.janela_procedimentos.destroy()
            except:
                pass
            return
        self.ui.janela_procedimentos.setWindowTitle(f"Procedimentos no Dente")
        self.ui.janela_procedimentos.show()

    def uncheck_itens(self):
        for procedure_id in self.ui.check_box_dentes.keys():
            self.ui.check_box_dentes[f"{procedure_id}"].setChecked(False)

    def show_operation_data(self):
        self.uncheck_itens()
        try:
            procedures_id = self.ui.combo_box_procedures.currentText()
            procedure_data = self.db.get_dental_procedure(self.ui.line_cpf_in_procedure.text(), procedures_id)
            self.check_itens(procedure_data)
            self.ui.line_notes.setText(procedure_data["notes"])

        except:
            self.ui.line_notes.setText("")
            pass

    def check_itens(self, procedure_data):
        for procedure_id in procedure_data["procedure"]:
            self.ui.check_box_dentes[f"{procedure_id}"].setChecked(True)

    def add_itens_combo_box(self, comboBox, itens):
        comboBox.addItems(itens)

    def __init__(self, db, people_cpfs):
        self.db = db
        self.people_cpfs = people_cpfs
        self.names = list(people_cpfs.keys())
        self.cpfs = list(people_cpfs.values())  
        self.ui = dental_ui.DentalUI()
        self.connect_combo_box_functions(self.ui.combo_box_pacientes, self.showPerson)
        self.connect_combo_box_functions(self.ui.combo_box_procedures, self.show_operation_data)
        self.connect_btn_functions(self.ui.btn_ver_opc, self.abrir_janela_opcs)
        self.connect_btn_functions(self.ui.btn3, self.abrir_janela_pacientes)
        self.add_itens_combo_box(self.ui.combo_box_pacientes, self.names)
        for checkBox in self.ui.check_box_dentes.values():
            self.connect_check_box_functions(checkBox, self.abrir_janela_procedimentos)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = po.PersonDatabase()
    people_cpfs = db.get_all_people_names()
    actions = UserInterfaceActions(db,people_cpfs)
    actions.ui.janelaPessoas.show()
    sys.exit(app.exec())