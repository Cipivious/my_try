from PyQt6.QtWidgets import QApplication
from PyQt6 import uic
import sys
from PyQt6 import QtWidgets
from PyQt6 import QtGui
import random
import time


def add_line_edits_to_line():
    line_edit: QtWidgets.QLineEdit = ui.lineEdit
    line_edit_2: QtWidgets.QLineEdit = ui.lineEdit_2
    line_edit_3: QtWidgets.QLineEdit = ui.lineEdit_3
    line_edit_3.setText(str(int(line_edit.text()) + int(line_edit_2.text())))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui: QtWidgets.QDialog = uic.loadUi("./sign_and_slot.ui")
    ui.show()

    ui.pushButton.clicked.connect(add_line_edits_to_line)

    sys.exit(app.exec())
