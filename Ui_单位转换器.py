# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '单位转换器.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(455, 264)
        Form.setStyleSheet(u".QComboBox {\n"
"	border-radius : 5%;\n"
"	border: 1px solid black;\n"
"}\n"
".QLineEdit {\n"
"	border-radius: 5%;\n"
"	border: 1px solid black;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.inputTypeComboBox2 = QComboBox(Form)
        self.inputTypeComboBox2.setObjectName(u"inputTypeComboBox2")
        self.inputTypeComboBox2.setMinimumSize(QSize(200, 40))

        self.gridLayout.addWidget(self.inputTypeComboBox2, 4, 1, 1, 1)

        self.inputDataEditLine1 = QLineEdit(Form)
        self.inputDataEditLine1.setObjectName(u"inputDataEditLine1")
        self.inputDataEditLine1.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.inputDataEditLine1, 3, 0, 1, 1)

        self.inputDataEditLine2 = QLineEdit(Form)
        self.inputDataEditLine2.setObjectName(u"inputDataEditLine2")
        self.inputDataEditLine2.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.inputDataEditLine2, 4, 0, 1, 1)

        self.inputTypeComboBox1 = QComboBox(Form)
        self.inputTypeComboBox1.setObjectName(u"inputTypeComboBox1")
        self.inputTypeComboBox1.setMinimumSize(QSize(200, 40))

        self.gridLayout.addWidget(self.inputTypeComboBox1, 3, 1, 1, 1)

        self.dataTypeComboBox = QComboBox(Form)
        self.dataTypeComboBox.setObjectName(u"dataTypeComboBox")
        self.dataTypeComboBox.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.dataTypeComboBox, 2, 0, 1, 2)

        self.transDataLabel = QLabel(Form)
        self.transDataLabel.setObjectName(u"transDataLabel")
        self.transDataLabel.setMaximumSize(QSize(600, 50))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.transDataLabel.setFont(font)

        self.gridLayout.addWidget(self.transDataLabel, 1, 0, 1, 2)

        self.originDataLabel = QLabel(Form)
        self.originDataLabel.setObjectName(u"originDataLabel")
        self.originDataLabel.setMaximumSize(QSize(600, 30))
        font1 = QFont()
        font1.setPointSize(16)
        self.originDataLabel.setFont(font1)
        self.originDataLabel.setStyleSheet(u"color: rgb(160, 160, 160)")

        self.gridLayout.addWidget(self.originDataLabel, 0, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5355\u4f4d\u6362\u7b97\u5668", None))
        self.transDataLabel.setText(QCoreApplication.translate("Form", u"0", None))
        self.originDataLabel.setText(QCoreApplication.translate("Form", u"0 = ", None))
    # retranslateUi

