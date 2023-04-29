# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1031, 611)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(1, -1, 1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.archive = QtWidgets.QPushButton(self.horizontalFrame)
        self.archive.setMinimumSize(QtCore.QSize(140, 55))
        self.archive.setMaximumSize(QtCore.QSize(140, 55))
        self.archive.setStyleSheet("QPushButton{\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 15px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover{\n"
                                   "background-color: rgba(255, 255, 255, 70);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed{\n"
                                   "background-color: rgb(87, 227, 137);\n"
                                   "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/inbox-archive-line.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.archive.setIcon(icon)
        self.archive.setIconSize(QtCore.QSize(25, 25))
        self.archive.setAutoRepeat(False)
        self.archive.setObjectName("archive")
        self.horizontalLayout.addWidget(self.archive)
        self.extract = QtWidgets.QPushButton(self.horizontalFrame)
        self.extract.setMinimumSize(QtCore.QSize(120, 55))
        self.extract.setMaximumSize(QtCore.QSize(120, 55))
        self.extract.setStyleSheet("QPushButton{\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 15px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover{\n"
                                   "background-color: rgba(255, 255, 255, 70);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed{\n"
                                   "background-color: rgb(87, 227, 137);\n"
                                   "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/inbox-unarchive-line.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.extract.setIcon(icon1)
        self.extract.setIconSize(QtCore.QSize(25, 25))
        self.extract.setObjectName("extract")
        self.horizontalLayout.addWidget(self.extract)
        self.delete_2 = QtWidgets.QPushButton(self.horizontalFrame)
        self.delete_2.setMinimumSize(QtCore.QSize(120, 55))
        self.delete_2.setMaximumSize(QtCore.QSize(120, 55))
        self.delete_2.setStyleSheet("QPushButton{\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 15px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover{\n"
                                    "background-color: rgba(255, 255, 255, 70);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed{\n"
                                    "background-color: rgb(87, 227, 137);\n"
                                    "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/delete-bin-line.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_2.setIcon(icon2)
        self.delete_2.setIconSize(QtCore.QSize(25, 25))
        self.delete_2.setObjectName("delete_2")
        self.horizontalLayout.addWidget(self.delete_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.horizontalFrame1 = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame1.setObjectName("horizontalFrame1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.up_button = QtWidgets.QPushButton(self.horizontalFrame1)
        self.up_button.setMinimumSize(QtCore.QSize(41, 41))
        self.up_button.setStyleSheet("QPushButton{\n"
                                     "background-color: rgb(255, 255, 255);\n"
                                     "border-radius: 15px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     "background-color: rgba(255, 255, 255, 70);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed{\n"
                                     "background-color: rgb(87, 227, 137);\n"
                                     "}")
        self.up_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/corner-left-up-fill.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.up_button.setIcon(icon3)
        self.up_button.setIconSize(QtCore.QSize(30, 30))
        self.up_button.setObjectName("up_button")
        self.horizontalLayout_2.addWidget(self.up_button)
        self.path_line = QtWidgets.QLineEdit(self.horizontalFrame1)
        self.path_line.setMinimumSize(QtCore.QSize(0, 41))
        self.path_line.setMaximumSize(QtCore.QSize(16777215, 41))
        self.path_line.setStyleSheet("QLineEdit {\n"
                                     "    border-radius: 15px;\n"
                                     "    background-color: rgb(255, 255, 255);\n"
                                     "    border: 1px solid #ced4da;\n"
                                     "    padding-left: 5px;\n"
                                     "} \n"
                                     "")
        self.path_line.setObjectName("path_line")
        self.horizontalLayout_2.addWidget(self.path_line)
        self.verticalLayout.addWidget(self.horizontalFrame1)
        self.file_window = QtWidgets.QTableWidget(self.centralwidget)
        self.file_window.setStyleSheet("")
        self.file_window.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.file_window.setDragEnabled(True)
        self.file_window.setDragDropOverwriteMode(True)
        self.file_window.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.file_window.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.file_window.setAlternatingRowColors(False)
        self.file_window.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.file_window.setTextElideMode(QtCore.Qt.ElideRight)
        self.file_window.setShowGrid(False)
        self.file_window.setWordWrap(True)
        self.file_window.setCornerButtonEnabled(True)
        self.file_window.setObjectName("file_window")
        self.file_window.setColumnCount(4)
        self.file_window.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.file_window.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.file_window.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.file_window.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.file_window.setHorizontalHeaderItem(3, item)
        self.file_window.horizontalHeader().setVisible(True)
        self.file_window.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.file_window)
        self.horizontalFrame2 = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.horizontalFrame2.setObjectName("horizontalFrame2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalFrame2)
        self.horizontalLayout_5.setContentsMargins(3, 0, 0, 3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.total_label = QtWidgets.QLabel(self.horizontalFrame2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.total_label.setFont(font)
        self.total_label.setObjectName("total_label")
        self.horizontalLayout_5.addWidget(self.total_label)
        self.horizontalFrame3 = QtWidgets.QFrame(self.horizontalFrame2)
        self.horizontalFrame3.setObjectName("horizontalFrame3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.selected_label = QtWidgets.QLabel(self.horizontalFrame3)
        self.selected_label.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.selected_label.setFont(font)
        self.selected_label.setObjectName("selected_label")
        self.horizontalLayout_3.addWidget(self.selected_label, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.horizontalLayout_5.addWidget(self.horizontalFrame3)
        self.verticalLayout.addWidget(self.horizontalFrame2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1031, 30))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Archivator"))
        self.archive.setText(_translate("MainWindow", "Создать архив"))
        self.extract.setText(_translate("MainWindow", "Извлечь"))
        self.delete_2.setText(_translate("MainWindow", "Удалить"))
        item = self.file_window.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.file_window.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Размер"))
        item = self.file_window.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.file_window.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Изменён"))
        self.total_label.setText(_translate("MainWindow", "Всего:"))
        self.selected_label.setText(_translate("MainWindow", "Выделено:"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Настройки"))
