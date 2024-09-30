from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("four_pages_example.ui", self)  # 加载 .ui 文件

        # 连接按钮到控制函数
        self.pushButton_1.clicked.connect(self.frameController)
        self.pushButton_2.clicked.connect(self.frameController)
        self.pushButton_3.clicked.connect(self.frameController)
        self.pushButton_4.clicked.connect(self.frameController)

    def frameController(self):
        sender = self.sender()  # 获取发送信号的按钮
        index = {
            self.pushButton_1: 0,  # 对应 page_0
            self.pushButton_2: 1,  # 对应 page_1
            self.pushButton_3: 2,  # 对应 page_2
            self.pushButton_4: 3,  # 对应 page_3
        }
        self.stackedWidget.setCurrentIndex(index[sender])  # 根据按钮设置页面


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
