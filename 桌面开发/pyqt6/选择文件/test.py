from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QFileDialog,
    QVBoxLayout,
    QWidget,
    QMessageBox,
)
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("文件选择示例")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # 创建按钮
        self.pushButton_select_file = QPushButton("选择文件")
        self.pushButton_select_file.clicked.connect(self.select_file)

        self.layout.addWidget(self.pushButton_select_file)

    def select_file(self):
        # 打开文件选择对话框
        options = QFileDialog.Option.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(
            self, "选择文件", "", "所有文件 (*);;文本文件 (*.txt)", options=options
        )

        if file_name:
            # 显示选择的文件名
            QMessageBox.information(self, "选择的文件", f"您选择的文件是: {file_name}")
        else:
            QMessageBox.warning(self, "没有选择文件", "您没有选择任何文件。")


# 创建 QApplication 实例
app = QApplication(sys.argv)

# 创建主窗口并显示
window = MainWindow()
window.show()

sys.exit(app.exec())
