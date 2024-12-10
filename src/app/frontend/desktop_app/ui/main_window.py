# -*- coding: utf-8 -*-

##########################################################################
# Form generated from reading UI file 'main_window.ui'
##
# Created by: Qt User Interface Compiler version 6.7.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
##########################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from app.frontend.desktop_app.mazes.window_opengl import MazeOpenGLWidget


class UiMainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 519)
        MainWindow.setMinimumSize(QSize(774, 519))
        MainWindow.setMaximumSize(QSize(774, 519))
        MainWindow.setStyleSheet(
            "QMainWindow {background-color: rgb(194, 160, 129);}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.window_opengl = QOpenGLWidget(self.centralwidget)
        self.window_opengl = MazeOpenGLWidget(self.centralwidget)
        self.window_opengl.setObjectName("window_opengl")
        self.window_opengl.setGeometry(QRect(10, 10, 500, 500))
        self.window_opengl.setStyleSheet("")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(520, 10, 241, 501))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_choose_file = QPushButton(self.gridLayoutWidget)
        self.btn_choose_file.setObjectName("btn_choose_file")
        font = QFont()
        font.setPointSize(12)
        self.btn_choose_file.setFont(font)
        self.btn_choose_file.setStyleSheet(
            "QPushButton {background-color: rgb(255, 250, 239);border: 0px solid  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.204762 rgba(155, 155, 155, 157));\n"
            "border-radius: 20px;}QPushButton:pressed {background-color: rgb(170, 170, 145);}QPushButton:hover {background-color: rgb(170, 170, 145);}\n"
            "")

        self.verticalLayout_3.addWidget(self.btn_choose_file)

        self.btn_save_maze = QPushButton(self.gridLayoutWidget)
        self.btn_save_maze.setObjectName("btn_save_maze")
        self.btn_save_maze.setFont(font)
        self.btn_save_maze.setStyleSheet(
            "QPushButton {background-color: rgb(255, 250, 239);border: 0px solid  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.204762 rgba(155, 155, 155, 157));\n"
            "border-radius: 20px;}QPushButton:pressed {background-color: rgb(170, 170, 145);}QPushButton:hover {background-color: rgb(170, 170, 145);}\n"
            "")

        self.verticalLayout_3.addWidget(self.btn_save_maze)

        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum,
                                            QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 7, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sb_entry_y = QSpinBox(self.gridLayoutWidget)
        self.sb_entry_y.setObjectName("sb_entry_y")
        self.sb_entry_y.setMinimumSize(QSize(30, 10))
        self.sb_entry_y.setFont(font)
        self.sb_entry_y.setStyleSheet(
            "QSpinBox {qproperty-alignment: 'AlignCenter';}")
        self.sb_entry_y.setMinimum(0)
        self.sb_entry_y.setMaximum(500)
        self.sb_entry_y.setSingleStep(10)
        self.sb_entry_y.setValue(100)

        self.horizontalLayout_4.addWidget(self.sb_entry_y)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(
            QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalSpacer_2 = QSpacerItem(40, 20,
                                              QSizePolicy.Policy.Expanding,
                                              QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.sb_exit_y = QSpinBox(self.gridLayoutWidget)
        self.sb_exit_y.setObjectName("sb_exit_y")
        self.sb_exit_y.setMinimumSize(QSize(10, 10))
        self.sb_exit_y.setFont(font)
        self.sb_exit_y.setStyleSheet(
            "QSpinBox {qproperty-alignment: 'AlignCenter';}")
        self.sb_exit_y.setMinimum(0)
        self.sb_exit_y.setMaximum(500)
        self.sb_exit_y.setSingleStep(10)
        self.sb_exit_y.setValue(250)

        self.horizontalLayout_5.addWidget(self.sb_exit_y)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20,
                                              QSizePolicy.Policy.Expanding,
                                              QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)

        self.gridLayout.addLayout(self.horizontalLayout_4, 11, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum,
                                            QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 15, 0, 1, 1)

        self.btn_generate_maze = QPushButton(self.gridLayoutWidget)
        self.btn_generate_maze.setObjectName("btn_generate_maze")
        self.btn_generate_maze.setFont(font)
        self.btn_generate_maze.setStyleSheet(
            "QPushButton {background-color: rgb(255, 250, 239);border: 0px solid  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.204762 rgba(155, 155, 155, 157));\n"
            "border-radius: 20px;}QPushButton:pressed {background-color: rgb(170, 170, 145);}QPushButton:hover {background-color: rgb(170, 170, 145);}\n"
            "")

        self.gridLayout.addWidget(self.btn_generate_maze, 13, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sb_colm_maze = QSpinBox(self.gridLayoutWidget)
        self.sb_colm_maze.setObjectName("sb_colm_maze")
        self.sb_colm_maze.setMinimumSize(QSize(10, 10))
        self.sb_colm_maze.setFont(font)
        self.sb_colm_maze.setStyleSheet(
            "QSpinBox {qproperty-alignment: 'AlignCenter';}")
        self.sb_colm_maze.setMinimum(1)
        self.sb_colm_maze.setMaximum(50)

        self.horizontalLayout_2.addWidget(self.sb_colm_maze)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet(
            "QLineEdit {qproperty-alignment: 'AlignCenter';border: 4px solid green;}"
        )

        self.horizontalLayout_10.addWidget(self.lineEdit, 0,
                                           Qt.AlignmentFlag.AlignRight)

        self.horizontalSpacer_8 = QSpacerItem(40, 20,
                                              QSizePolicy.Policy.Expanding,
                                              QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet(
            "QLineEdit {qproperty-alignment: 'AlignCenter';border: 4px solid blue;}"
        )

        self.horizontalLayout_10.addWidget(self.lineEdit_2)

        self.horizontalSpacer_9 = QSpacerItem(40, 20,
                                              QSizePolicy.Policy.Expanding,
                                              QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.gridLayout.addLayout(self.horizontalLayout_10, 8, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum,
                                            QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.btn_solve_maze = QPushButton(self.gridLayoutWidget)
        self.btn_solve_maze.setObjectName("btn_solve_maze")
        self.btn_solve_maze.setFont(font)
        self.btn_solve_maze.setStyleSheet(
            "QPushButton {background-color: rgb(255, 250, 239);border: 0px solid  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.204762 rgba(155, 155, 155, 157));\n"
            "border-radius: 20px;}QPushButton:pressed {background-color: rgb(170, 170, 145);}QPushButton:hover {background-color: rgb(170, 170, 145);}\n"
            "")

        self.gridLayout.addWidget(self.btn_solve_maze, 14, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum,
                                          QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 12, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sb_entry_x = QSpinBox(self.gridLayoutWidget)
        self.sb_entry_x.setObjectName("sb_entry_x")
        self.sb_entry_x.setMinimumSize(QSize(30, 10))
        self.sb_entry_x.setFont(font)
        self.sb_entry_x.setStyleSheet(
            "QSpinBox {qproperty-alignment: 'AlignCenter';}")
        self.sb_entry_x.setMinimum(0)
        self.sb_entry_x.setMaximum(500)
        self.sb_entry_x.setSingleStep(10)
        self.sb_entry_x.setValue(250)

        self.horizontalLayout_3.addWidget(self.sb_entry_x)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20,
                                            QSizePolicy.Policy.Expanding,
                                            QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.sb_exit_x = QSpinBox(self.gridLayoutWidget)
        self.sb_exit_x.setObjectName("sb_exit_x")
        self.sb_exit_x.setMinimumSize(QSize(10, 10))
        self.sb_exit_x.setFont(font)
        self.sb_exit_x.setStyleSheet(
            "QSpinBox {qproperty-alignment: 'AlignCenter';}")
        self.sb_exit_x.setMinimum(0)
        self.sb_exit_x.setMaximum(500)
        self.sb_exit_x.setSingleStep(10)
        self.sb_exit_x.setValue(100)

        self.horizontalLayout_6.addWidget(self.sb_exit_x)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20,
                                              QSizePolicy.Policy.Expanding,
                                              QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_3.addLayout(self.horizontalLayout_6)

        self.gridLayout.addLayout(self.horizontalLayout_3, 10, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sb_rows_maze = QSpinBox(self.gridLayoutWidget)
        self.sb_rows_maze.setObjectName("sb_rows_maze")
        self.sb_rows_maze.setMinimumSize(QSize(10, 10))
        font2 = QFont()
        font2.setPointSize(11)
        self.sb_rows_maze.setFont(font2)
        self.sb_rows_maze.setStyleSheet(
            "QSpinBox {qproperty-alignment: 'AlignCenter';}")
        self.sb_rows_maze.setMinimum(1)
        self.sb_rows_maze.setMaximum(50)

        self.horizontalLayout.addWidget(self.sb_rows_maze)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum,
                                            QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_solve_maze, self.sb_rows_maze)
        QWidget.setTabOrder(self.sb_rows_maze, self.btn_generate_maze)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Mazes And Caves", None))
        self.btn_choose_file.setText(
            QCoreApplication.translate("MainWindow", "Choose file", None))
        self.btn_save_maze.setText(
            QCoreApplication.translate("MainWindow", "Save maze", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", "Y",
                                                        None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", "Y",
                                                        None))
        self.btn_generate_maze.setText(
            QCoreApplication.translate("MainWindow", "Generate maze", None))
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "The maze columns ", None))
        # if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><br/></p></body></html>',
                None,
            ))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.lineEdit.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><br/></p></body></html>',
                None,
            ))
        # endif // QT_CONFIG(whatsthis)
        self.lineEdit.setText(
            QCoreApplication.translate("MainWindow", "Entry point", None))
        self.lineEdit_2.setText(
            QCoreApplication.translate("MainWindow", "Exit point", None))
        self.btn_solve_maze.setText(
            QCoreApplication.translate("MainWindow", "Solve the maze", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "X",
                                                        None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", "X",
                                                        None))
        self.label.setText(
            QCoreApplication.translate("MainWindow", "The maze rows", None))

    # retranslateUi
