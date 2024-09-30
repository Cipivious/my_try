from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QLabel,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建初始界面
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        # 初始界面布局
        self.layout = QVBoxLayout()
        self.label = QLabel("This is the initial content.")
        self.change_button = QPushButton("Load New Content")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.change_button)
        self.main_widget.setLayout(self.layout)

        # 信号连接槽函数
        self.change_button.clicked.connect(self.load_new_content)

    def load_new_content(self):
        # 新的界面布局
        new_widget = QWidget()
        new_layout = QVBoxLayout()
        new_label = QLabel("This is the new content.")
        back_button = QPushButton("Go Back to Initial Content")

        new_layout.addWidget(new_label)
        new_layout.addWidget(back_button)
        new_widget.setLayout(new_layout)

        # 将新界面设置为中央小部件
        self.setCentralWidget(new_widget)

        # 信号连接槽函数，用于返回初始界面
        back_button.clicked.connect(self.load_initial_content)

    def load_initial_content(self):
        # 恢复初始界面
        self.setCentralWidget(self.main_widget)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
