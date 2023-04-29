import os
import sys
import shutil

from fnmatch import fnmatch

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox

from main_window_design import Ui_MainWindow


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def human_read_format(n):
    if n >= 1073741824:
        return f"{round(n / 2 ** 30, 2)} гигабайт"

    if n >= 1048576:
        return f"{round(n / 2 ** 20, 2)} мегабайт"

    return f"{round(n / 1024, 2)} килобайт"


class Main_window(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.process()
        self.start_init()

    def process(self):
        user = os.listdir("/home/")[1]

        self.path_line.setText(f"/home/{user}")

        self.up_button.clicked.connect(self.set_previous_directory)

        self.archive.clicked.connect(self.archive_files)
        self.extract.clicked.connect(self.extract_files)
        self.delete_2.clicked.connect(self.delete_files)

        self.file_window.itemDoubleClicked.connect(self.open_directory_by_clicking)
        self.file_window.itemClicked.connect(self.show_selected_items)

    def keyPressEvent(self, event):
        if event.key() == 16777220 and self.path_line.hasFocus():
            self.show_content()

    def archive_files(self):
        pass

    def delete_files(self):
        for item in self.file_window.selectedItems():
            path = f"{self.path_line.text()}/{item.text()}"

            if os.path.isdir(path):
                shutil.rmtree(path)

            else:
                os.remove(path)

        self.show_content()

    def extract_files(self):
        pass

    def open_directory_by_clicking(self):
        path = f"{self.path_line.text()}/{self.file_window.selectedItems()[0].text()}"

        if os.path.isdir(path):
            self.path_line.setText(path)
            self.show_content()

    def set_previous_directory(self):
        path = "/".join(self.path_line.text().split("/")[:-1])
        self.path_line.setText(path if len(path) != 0 else "/")

        self.show_content()

    def show_selected_items(self):
        size = 0

        for item in self.file_window.selectedItems():
            size += os.path.getsize(f"{self.path_line.text()}/{item.text()}")

        self.selected_label.setText(
            f"Выделено: {len(self.file_window.selectedItems())} элементов. Общий размер: {human_read_format(size)}")

    def start_init(self):
        files = [i for i in os.listdir(self.path_line.text())]

        size = 0

        for item in files:
            size += os.path.getsize(f"{self.path_line.text()}/{item}")

        self.file_window.setRowCount(len(files))
        self.total_label.setText(f"Всего: {len(files)} элементов. Общий размер: {human_read_format(size)}")

        for i in range(len(files)):
            item = QTableWidgetItem()
            item.setText(files[i].split("/")[-1])

            if os.path.isdir(files[i]):
                item.setIcon(QIcon("icons/folder-line.png"))

            else:
                item.setIcon(QIcon("icons/file-line.png"))

            self.file_window.setItem(i, 0, item)

        self.file_window.resizeColumnsToContents()

    def show_content(self):
        path_exists = True

        try:
            files = [i for i in os.listdir(self.path_line.text())]

        except FileNotFoundError:
            QMessageBox.question(self, "Ошибка",
                                 f"Путь {self.path_line.text()} не существует",
                                 QMessageBox.Ok)
            path_exists = False

        if path_exists:
            size = 0

            for item in files:
                size += os.path.getsize(f"{self.path_line.text()}/{item}")

            self.file_window.setRowCount(len(files))
            self.total_label.setText(f"Всего: {len(files)} элементов. Общий размер: {human_read_format(size)}")

            for i in range(len(files)):
                item = QTableWidgetItem()
                item.setText(files[i].split("/")[-1])

                if os.path.isdir(files[i]):
                    item.setIcon(QIcon("icons/folder-line.png"))

                else:
                    item.setIcon(QIcon("icons/file-line.png"))

                self.file_window.setItem(i, 0, item)

            self.file_window.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_window()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
