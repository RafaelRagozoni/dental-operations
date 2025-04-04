import sys
import json
import os
from datetime import datetime

from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(500,400)
janela.setWindowTitle("Operações dentais do Dr. Sismoto")
janela.show()

app.exec()