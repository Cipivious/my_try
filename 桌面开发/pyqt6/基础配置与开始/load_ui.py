from PyQt6.QtWidgets import QApplication
from PyQt6 import uic
import sys
from PyQt6 import QtWidgets
from PyQt6 import QtGui
import random
import time

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui: QtWidgets.QDialog = uic.loadUi("./pyqt_test.ui")
    ui.show()
    # label = ui.findChild(QtWidgets.QLabel, "label")
    # print(type(label))
    # print(label.text())
    # print(type(ui))

    # single_line_edit: QtWidgets.QLineEdit = ui.findChild(
    #     QtWidgets.QLineEdit, "lineEdit"
    # )

    # single_line_edit.setValidator(QtGui.QIntValidator())

    # text_edit: QtWidgets.QTextEdit = ui.findChild(QtWidgets.QTextEdit, "textEdit")
    # ui.show()
    # for i in range(100):
    #     text_edit.append(str(random.randint(0, 10000000000)) + "\n")
    #     QApplication.processEvents()  # 强制处理 UI 事件，立即更新显示
    #     time.sleep(0.1)

    # text_edit: QtWidgets.QTextBrowser = ui.findChild(
    #     QtWidgets.QTextBrowser, "textBrowser"
    # )
    # ui.show()
    # for i in range(100):
    #     text_edit.append(str(random.randint(0, 10000000000)) + "\n")
    #     QApplication.processEvents()  # 强制处理 UI 事件，立即更新显示
    #     time.sleep(0.1)

    push_button: QtWidgets.QPushButton = ui.findChild(
        QtWidgets.QPushButton, "pushButton"
    )

    sys.exit(app.exec())
