# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chess.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(768, 428)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Stack = QStackedWidget(self.centralwidget)
        self.Stack.setObjectName(u"Stack")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.titleLabel = QLabel(self.page)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)

        self.classicChessButton_2 = QPushButton(self.page)
        self.classicChessButton_2.setObjectName(u"classicChessButton_2")

        self.gridLayout.addWidget(self.classicChessButton_2, 1, 0, 1, 1)

        self.settingsButton = QPushButton(self.page)
        self.settingsButton.setObjectName(u"settingsButton")

        self.gridLayout.addWidget(self.settingsButton, 3, 0, 1, 1)

        self.fischerChessButton_2 = QPushButton(self.page)
        self.fischerChessButton_2.setObjectName(u"fischerChessButton_2")

        self.gridLayout.addWidget(self.fischerChessButton_2, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.Stack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.windowSizeLabel = QLabel(self.page_2)
        self.windowSizeLabel.setObjectName(u"windowSizeLabel")
        self.windowSizeLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.windowSizeLabel)

        self.sizeLineEdit = QLineEdit(self.page_2)
        self.sizeLineEdit.setObjectName(u"sizeLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.sizeLineEdit)

        self.firstPlayerNameLabel = QLabel(self.page_2)
        self.firstPlayerNameLabel.setObjectName(u"firstPlayerNameLabel")
        self.firstPlayerNameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.firstPlayerNameLabel)

        self.firstPlayerNameLineEdit = QLineEdit(self.page_2)
        self.firstPlayerNameLineEdit.setObjectName(u"firstPlayerNameLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.firstPlayerNameLineEdit)

        self.secondPlayerNameLabel_2 = QLabel(self.page_2)
        self.secondPlayerNameLabel_2.setObjectName(u"secondPlayerNameLabel_2")
        self.secondPlayerNameLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.secondPlayerNameLabel_2)

        self.secondPlayerNameLineEdit = QLineEdit(self.page_2)
        self.secondPlayerNameLineEdit.setObjectName(u"secondPlayerNameLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.secondPlayerNameLineEdit)

        self.primaryColorLabel = QLabel(self.page_2)
        self.primaryColorLabel.setObjectName(u"primaryColorLabel")
        self.primaryColorLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.primaryColorLabel)

        self.primaryColorComboBox = QComboBox(self.page_2)
        self.primaryColorComboBox.setObjectName(u"primaryColorComboBox")
        self.primaryColorComboBox.setEditable(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.primaryColorComboBox)

        self.secondaryColorLabel = QLabel(self.page_2)
        self.secondaryColorLabel.setObjectName(u"secondaryColorLabel")
        self.secondaryColorLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.secondaryColorLabel)

        self.secondaryColorComboBox = QComboBox(self.page_2)
        self.secondaryColorComboBox.setObjectName(u"secondaryColorComboBox")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.secondaryColorComboBox)

        self.saveButton = QPushButton(self.page_2)
        self.saveButton.setObjectName(u"saveButton")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.saveButton)

        self.exitButton = QPushButton(self.page_2)
        self.exitButton.setObjectName(u"exitButton")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.exitButton)


        self.gridLayout_3.addLayout(self.formLayout, 0, 0, 1, 1)

        self.Stack.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.Stack)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 768, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Stack.setCurrentIndex(0)
        self.primaryColorComboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Chess Launcher", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"CHESS", None))
        self.classicChessButton_2.setText(QCoreApplication.translate("MainWindow", u"Classic Chess", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.fischerChessButton_2.setText(QCoreApplication.translate("MainWindow", u"Fischer Chess", None))
        self.windowSizeLabel.setText(QCoreApplication.translate("MainWindow", u"Window Size:", None))
        self.sizeLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"800", None))
        self.firstPlayerNameLabel.setText(QCoreApplication.translate("MainWindow", u"First Player Name:", None))
        self.secondPlayerNameLabel_2.setText(QCoreApplication.translate("MainWindow", u"Second Player Name:", None))
        self.secondPlayerNameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"black", None))
        self.primaryColorLabel.setText(QCoreApplication.translate("MainWindow", u"Primary Color:", None))
        self.primaryColorComboBox.setCurrentText("")
        self.secondaryColorLabel.setText(QCoreApplication.translate("MainWindow", u"Secondary Color:", None))
        self.secondaryColorComboBox.setCurrentText("")
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
    # retranslateUi