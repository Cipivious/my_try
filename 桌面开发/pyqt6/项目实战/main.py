from PyQt6 import uic
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QFileDialog, QMessageBox
from words_exercise import *
from add_words_into_database import *
from PyQt6.QtGui import QFont
import queue


def get_real_path(file_path):
    # 获取当前路径
    if getattr(sys, "frozen", False):
        # 如果是打包后的应用，使用 frozen 的路径
        base_path = sys._MEIPASS
    else:
        # 否则使用脚本路径
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, file_path)


class MainWindow(QtWidgets.QWidget):  # 继承 QWidget
    def __init__(self):
        super().__init__()
        # 加载 .ui 文件
        self.ui = uic.loadUi(get_real_path("布局示例.ui"), self)
        # self.textBrowser_2.setFont(16)
        # 连接按钮的点击信号到 frameController
        self.pushButton_start_word_exercies.clicked.connect(self.start_exercise)
        self.pushButton_continue.clicked.connect(self.start_check_word)
        self.pushButton_7.clicked.connect(self.check_word)
        self.pushButton_6.clicked.connect(self.check_right)
        self.pushButton.clicked.connect(self.check_error)
        self.pushButton_4.clicked.connect(self.change_to_add_word_page)
        self.pushButton_2.clicked.connect(self.select_file)
        self.pushButton_3.clicked.connect(self.add_data_to_database)
        self.pushButton_5.clicked.connect(self.close_application)

        self.word_queue = queue.Queue()
        self.word = None
        self.example_list = None
        self.guess_word_list = None
        self.file_name = None

    def close_application(self):
        # 关闭应用程序
        QtWidgets.QApplication.quit()

    def change_to_add_word_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def add_data_to_database(self):
        word_list = split_txt(self.file_name)
        for word, translation in word_list:
            insert_word(word=word, translation=translation)
        QMessageBox.information(self, "添加单词", f"单词添加成功")

    def select_file(self):
        # 打开文件选择对话框
        options = QFileDialog.Option.DontUseNativeDialog
        self.file_name, _ = QFileDialog.getOpenFileName(
            self, "选择文件", "", "文本文件 (*.txt)", options=options
        )
        if self.file_name:
            # 显示选择的文件名
            QMessageBox.information(
                self, "选择的文件", f"您选择的文件是: {self.file_name}"
            )
            self.lineEdit: QtWidgets.QLineEdit
            self.lineEdit.setText(self.file_name)
            file_content = ""
            with open(self.file_name, "r", encoding="utf-8") as f:
                for _ in range(10):
                    file_content = file_content + f.readline()
            self.textBrowser_4.setText(file_content)
        else:
            QMessageBox.warning(self, "没有选择文件", "您没有选择任何文件。")

    def start_exercise(self):
        self.stackedWidget.setCurrentIndex(1)
        self.textBrowser_2: QtWidgets.QTextBrowser  # 指定类型
        if not os.path.exists("word_database.db"):
            self.textBrowser_2.setText("请先运行另一个程序创建数据库并向其中添加单词！")
            QApplication.processEvents()
            return
        self.guess_word_list = get_words_by_date_and_proficiency()
        word_numbers = len(self.guess_word_list)
        self.textBrowser_2.append(
            f"本次一共有{word_numbers}个单词，开始你的闯关之旅吧！"
        )
        self.textBrowser_2.append("单词概览：")
        for word in self.guess_word_list:
            self.textBrowser_2.append(" ".join(map(str, word)))
        self.textBrowser_2.append("准备好了吗？")
        QApplication.processEvents()
        threading.Thread(target=self.get_word_queue).start()

    def get_word_queue(self):
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [
                executor.submit(get_word_exmple, word, 3)
                for word in self.guess_word_list
            ]
            # 逐个获取已经完成任务的返回值
            for future in as_completed(futures):
                self.word_queue.put(future.result())
            self.word_queue.put([None, None])

    def start_check_word(self):
        self.stackedWidget.setCurrentIndex(2)
        self.pushButton_start_word_exercies.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.textBrowser_3.clear()
        self.word, self.example_list = self.word_queue.get(True)
        if not self.word:
            self.textBrowser_3.clear()
            self.pushButton_start_word_exercies.setEnabled(True)
            self.pushButton_4.setEnabled(True)
            self.pushButton_5.setEnabled(True)
            self.textBrowser_3.append(
                "你真棒，所有的单词都已经学习完成了，要继续努力啊！"
            )
            QApplication.processEvents()
        self.textBrowser_3.append(self.word[1])
        self.textBrowser_3.append("你认识这个单词吗")
        QApplication.processEvents()

    def check_word(self):
        self.pushButton_7.setEnabled(False)
        self.pushButton_6.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.textBrowser_3.clear()
        self.word, self.example_list = self.word_queue.get(True)
        if not self.word:
            self.textBrowser_3.clear()
            self.pushButton_start_word_exercies.setEnabled(True)
            self.pushButton_4.setEnabled(True)
            self.pushButton_5.setEnabled(True)
            self.textBrowser_3.append(
                "你真棒，所有的单词都已经学习完成了，要继续努力啊！"
            )
            QApplication.processEvents()
        self.textBrowser_3.append(self.word[1])
        self.textBrowser_3.append("你认识这个单词吗")
        QApplication.processEvents()

    def check_right(self):
        self.pushButton_6.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.pushButton_7.setEnabled(True)
        correct_count = self.word[5] + 1
        for example in self.example_list:
            self.textBrowser_3.append(example)
            QApplication.processEvents()
            break
        self.textBrowser_3.append("你学会了吗？")
        threading.Thread(
            target=update_word_review,
            args=(
                self.word[0],
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                correct_count,
            ),
        ).start()
        QApplication.processEvents()

    def check_error(self):
        self.pushButton_6.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.pushButton_7.setEnabled(True)
        correct_count = self.word[5]
        for example in self.example_list:
            self.textBrowser_3.append(example)
        self.textBrowser_3.append("你学会了吗？")
        threading.Thread(
            target=update_word_review,
            args=(
                self.word[0],
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                correct_count,
            ),
        ).start()
        QApplication.processEvents()


if __name__ == "__main__":
    app = QApplication([])
    font = QFont()
    font.setPointSize(16)
    app.setFont(font)
    window = MainWindow()
    window.show()
    app.exec()
