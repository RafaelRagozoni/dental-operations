import sys
import json
import os
from datetime import datetime
from PyQt6.QtWidgets import QApplication
import src.dentalUI as dental_ui
import src.people_operations as po
import src.pdf_generator as pdf_gen
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
        if self.ui.combo_box_pacientes.currentText() == "":
            self.ui.static_label_name_selected_pacient.setText("Desconhecido")
            self.ui.line_cpf.setText("")
            self.ui.line_name.setText("")
            self.ui.line_last_seen.setText("")
            self.ui.line_birthday.setText("")
            self.ui.line_phone.setText("")
            self.ui.line_number_procedure.setText("")
            return
        current_name = self.ui.combo_box_pacientes.currentText()
        current_cpf = self.people_cpfs[self.ui.combo_box_pacientes.currentText()]
        person = self.db.get_person(current_cpf)
        number_procedure = person["last_procedure_id"]
        self.ui.static_label_name_selected_pacient.setText(current_name)
        self.ui.line_cpf.setText(current_cpf)
        self.ui.line_name.setText(current_name)
        self.ui.line_last_seen.setText(person["last_seen"])
        self.ui.line_birthday.setText(person["birth_date"])
        self.ui.line_phone.setText(person["phone"])
        self.ui.line_number_procedure.setText(f"{number_procedure}")
        self.ui.btn_ver_opc.setText(
            f"Ver Operações de {self.ui.combo_box_pacientes.currentText()}"
        )
        self.ui.line_name_in_procedure.setText(current_name)
        self.ui.line_cpf_in_procedure.setText(current_cpf)

    def cadastrarNovoPaciente(self):
        self.ui.static_label_name_selected_pacient.setText(
            "Desconhecido                 "
        )
        self.ui.line_cpf.setText("")
        self.ui.line_name.setText("")
        self.ui.line_last_seen.setText("")
        self.ui.line_birthday.setText("")
        self.ui.line_phone.setText("")
        self.ui.line_number_procedure.setText("")

    def salvarNovoPaciente(self):
        cpf = self.ui.line_cpf.text()
        name = self.ui.line_name.text()
        birth_data = self.ui.line_birthday.text()
        phone_number = self.ui.line_phone.text()
        self.db.add_person(cpf, name, birth_data, phone=phone_number)
        self.ui.static_label_name_selected_pacient.setText(name)
        self.people_cpfs = self.db.get_all_people_names()
        self.names = list(self.people_cpfs.keys())
        self.cpfs = list(self.people_cpfs.values())
        self.ui.combo_box_pacientes.addItem(name)
        self.ui.combo_box_pacientes.setCurrentIndex(
            self.ui.combo_box_pacientes.count() - 1
        )

    def atualizarDadosPaciente(self):
        cpf = self.ui.line_cpf.text()
        name = self.ui.line_name.text()
        birth_data = self.ui.line_birthday.text()
        phone_number = self.ui.line_phone.text()
        self.db.update_person(cpf, name=name, birth_date=birth_data, phone=phone_number)
        self.ui.static_label_name_selected_pacient.setText(name)
        self.people_cpfs = self.db.get_all_people_names()
        self.names = list(self.people_cpfs.keys())
        self.cpfs = list(self.people_cpfs.values())

    def deletePaciente(self):
        try:
            cpf = self.ui.line_cpf.text()
            self.db.delete_person(cpf)
            self.ui.combo_box_pacientes.removeItem(
                self.ui.combo_box_pacientes.currentIndex()
            )
        except:  # noqa: E722
            print("Erro ao deletar paciente")
            pass

    def cadastrarNovaConsulta(self):
        cpf = self.ui.line_cpf_in_procedure.text()
        new_procedure_id = int(self.db.get_person(cpf)["last_procedure_id"]) + 1
        self.db.add_dental_procedure(
            cpf,
            datetime.now().strftime("%d/%m/%Y"),
            procedures={},
            notes=self.ui.line_notes.text(),
        )
        self.ui.combo_box_procedures.addItem(str(new_procedure_id))
        self.ui.combo_box_procedures.setCurrentIndex(
            self.ui.combo_box_procedures.count() - 1
        )

    def salvarConsulta(self):
        cpf = self.ui.line_cpf_in_procedure.text()
        procedure_id = self.ui.combo_box_procedures.currentText()
        teeth_operated = {}
        for teeth_id, checkBox in self.ui.check_box_dentes.items():
            if checkBox.isChecked():
                teeth_operated[teeth_id] = []

        self.db.update_dental_procedure(
            cpf,
            procedure_id,
            date=self.ui.line_date.text(),
            notes=self.ui.line_notes.text(),
            procedures=teeth_operated,
        )

    def deletarConsulta(self):
        try:
            procedures_id = self.ui.combo_box_procedures.currentText()
            cpf = self.ui.line_cpf_in_procedure.text()
            self.db.delete_dental_procedure(cpf, procedures_id)
            self.ui.combo_box_procedures.removeItem(
                self.ui.combo_box_procedures.currentIndex()
            )
            self.ui.line_notes.setText("")
            self.ui.line_date.setText("")
            self.ui.combo_box_procedures.setCurrentIndex(
                self.ui.combo_box_procedures.count() - 1
            )
        except:  # noqa: E722
            print("Erro ao deletar consulta")

    def salvarProcedimentoNoDente(self):
        cpf = self.ui.line_cpf_in_procedure.text()
        procedure_id = self.ui.combo_box_procedures.currentText()
        procedures_done = self.db.get_dental_procedure(cpf, procedure_id).get(
            "procedures", {}
        )
        print(f"procedimentos no dente {procedures_done}")
        procedures_done[f"{self.tooth_id_reference}"] = []
        for procedure_done, checkBox in self.ui.check_box_procedimentos.items():
            if checkBox.isChecked():
                procedures_done[f"{self.tooth_id_reference}"].append(procedure_done)

        print(procedures_done)
        self.db.update_dental_procedure(cpf, procedure_id, procedures=procedures_done)

    def abrir_janela_opcs(self):
        self.ui.janelaOperations.setWindowTitle(
            self.ui.combo_box_pacientes.currentText()
        )
        self.ui.janelaOperations.show()
        procedures_id = self.db.get_person_dental_procedures_id(
            self.ui.line_cpf_in_procedure.text()
        )
        self.ui.combo_box_procedures.addItems(procedures_id)
        self.ui.janelaPessoas.destroy()

    def abrir_janela_pacientes(self):
        self.ui.janelaPessoas.setWindowTitle("Pacientes do Dr. Sismoto")
        self.ui.combo_box_procedures.clear()
        self.ui.janelaPessoas.show()
        self.ui.janelaOperations.destroy()

    def abrir_janela_procedimentos(self, tooth_id, checked):
        if not checked:
            try:
                self.ui.janela_procedimentos.destroy()
            except:  # noqa: E722
                pass
            return
        self.ui.janela_procedimentos.setWindowTitle(
            f"Procedimentos no Dente {tooth_id}"
        )
        cpf = self.ui.line_cpf_in_procedure.text()
        procedure_id = self.ui.combo_box_procedures.currentText()
        procedures = self.db.get_dental_operations_on_tooth(cpf, procedure_id, tooth_id)
        print(procedures)
        for procedure in self.ui.check_box_procedimentos.keys():
            self.ui.check_box_procedimentos[procedure].setChecked(False)
        for procedure in procedures:
            self.ui.check_box_procedimentos[procedure].setChecked(True)
        self.tooth_id_reference = int(tooth_id)
        self.ui.janela_procedimentos.show()

    def abrir_janela_precos(self):
        self.procedure_mapping = {}
        procedures_id = self.ui.combo_box_procedures.currentText()
        procedure_data = self.db.get_dental_procedure(
            self.ui.line_cpf_in_procedure.text(), procedures_id
        )
        for tooth, procedures in procedure_data["procedures"].items():
            for procedure in procedures:
                if procedure not in self.procedure_mapping:
                    self.procedure_mapping[procedure] = []
                self.procedure_mapping[procedure].append(tooth)
        self.ui.inicialJanelaPrecos()
        self.ui.adicionaElementosJanelaPrecos(self.procedure_mapping)
        self.connect_btn_functions(self.ui.btn_salva_pdf, self.salvar_pdf)
        self.ui.janela_precos.show()

    def salvar_pdf(self):
        pacient_name = self.ui.line_name_in_procedure.text()
        procedures_id = self.ui.combo_box_procedures.currentText()
        procedure_data = self.db.get_dental_procedure(
            self.ui.line_cpf_in_procedure.text(), procedures_id
        )

        procedure_prices = {}
        for procedure in self.procedure_mapping.keys():
            price_text = self.ui.procedures_prices[procedure].text()
            if "," in price_text:
                price_text = price_text.replace(",", ".")
            procedure_prices[procedure] = price_text

        self.pdf.generate_pdf(
            pacient_name,
            procedures_id,
            procedure_data,
            procedure_prices,
            self.procedure_mapping,
        )

    def uncheck_itens(self):
        for procedure_id in self.ui.check_box_dentes.keys():
            self.ui.check_box_dentes[f"{procedure_id}"].setChecked(False)

    def show_operation_data(self):
        self.uncheck_itens()
        try:
            procedures_id = self.ui.combo_box_procedures.currentText()
            procedure_data = self.db.get_dental_procedure(
                self.ui.line_cpf_in_procedure.text(), procedures_id
            )
            self.check_itens(procedure_data)
            self.ui.line_notes.setText(procedure_data["notes"])
            self.ui.line_date.setText(procedure_data["date"])
        except:  # noqa: E722
            self.ui.line_notes.setText("")
            now = datetime.now().strftime("%d/%m/%Y")
            self.ui.line_date.setText(f"{now}")
            pass

    def check_itens(self, procedure_data):
        for procedure_id in procedure_data["procedures"]:
            self.ui.check_box_dentes[f"{procedure_id}"].setChecked(True)
        self.ui.janela_procedimentos.destroy()

    def add_itens_combo_box(self, comboBox, itens):
        comboBox.addItems(itens)

    def __init__(self, db, people_cpfs):
        self.db = db
        self.people_cpfs = people_cpfs
        self.names = list(people_cpfs.keys())
        self.cpfs = list(people_cpfs.values())
        self.ui = dental_ui.DentalUI()
        self.pdf = pdf_gen.PDFGenerator()
        self.connect_combo_box_functions(self.ui.combo_box_pacientes, self.showPerson)
        self.connect_combo_box_functions(
            self.ui.combo_box_procedures, self.show_operation_data
        )
        self.connect_btn_functions(self.ui.btn_ver_opc, self.abrir_janela_opcs)
        self.connect_btn_functions(self.ui.btn3, self.abrir_janela_pacientes)
        self.connect_btn_functions(
            self.ui.btn_cadastrar_novo_paciente, self.cadastrarNovoPaciente
        )
        self.connect_btn_functions(self.ui.btn_salvar_paciente, self.salvarNovoPaciente)
        self.connect_btn_functions(
            self.ui.btn_atualizar_paciente, self.atualizarDadosPaciente
        )
        self.connect_btn_functions(self.ui.btn_delete_paciente, self.deletePaciente)
        self.connect_btn_functions(
            self.ui.btn_nova_consulta, self.cadastrarNovaConsulta
        )
        self.connect_btn_functions(self.ui.btn_salvar_consulta, self.salvarConsulta)
        self.connect_btn_functions(self.ui.btn_deletar_consulta, self.deletarConsulta)
        self.connect_btn_functions(
            self.ui.btn_salvar_procedures, self.salvarProcedimentoNoDente
        )
        self.connect_btn_functions(self.ui.btn_gerar_pdf, self.abrir_janela_precos)
        self.add_itens_combo_box(self.ui.combo_box_pacientes, self.names)
        for tooth_id in self.ui.check_box_dentes.keys():
            self.ui.check_box_dentes[tooth_id].toggled.connect(
                lambda checked, key=tooth_id: self.abrir_janela_procedimentos(
                    key, checked
                )
            )


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     db = po.PersonDatabase()
#     people_cpfs = db.get_all_people_names()
#     actions = UserInterfaceActions(db, people_cpfs)
#     actions.ui.janelaPessoas.show()
#     sys.exit(app.exec())
