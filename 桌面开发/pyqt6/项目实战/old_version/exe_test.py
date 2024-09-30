import sys
import subprocess  # 导入 subprocess 模块
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel
            | QtWidgets.QDialogButtonBox.StandardButton.Ok
        )
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)  # 关闭对话框
        self.buttonBox.rejected.connect(Dialog.reject)  # 关闭对话框
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # 连接 Ok 按钮的点击事件
        self.buttonBox.button(
            QtWidgets.QDialogButtonBox.StandardButton.Ok
        ).clicked.connect(self.run_external_program)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def run_external_program(self):
        # 替换为你想要执行的程序的路径
        program_path = r"单词训练.exe"  # 请确保路径正确
        try:
            subprocess.Popen(program_path)  # 使用 Popen 启动外部程序
        except Exception as e:
            print(f"Error occurred: {e}")  # 输出错误信息


class MyApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
