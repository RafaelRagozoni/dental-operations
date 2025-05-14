import sys
from PyQt6.QtWidgets import QApplication
import os
import src.btnFunctions as bf
import src.people_operations as po
import src.dentalUI as dental_ui


def start():
    print("Welcome to Dental Operations Management System!")
    pdf_folder = os.path.join(os.getcwd(), "pdfs")
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)
    app = QApplication(sys.argv)
    db = po.PersonDatabase()
    people_cpfs = db.get_all_people_names()
    actions = bf.UserInterfaceActions(db, people_cpfs)
    actions.ui.janelaPessoas.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    start()
