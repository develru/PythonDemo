# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'webUi.ui'
#
# Created: Tue Jul 31 13:06:46 2012
#      by: pyside-uic 0.2.14 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(self.verticalLayoutWidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.webWidget = QtGui.QWidget(self.frame)
        self.webWidget.setGeometry(QtCore.QRect(9, 79, 361, 241))
        self.webWidget.setObjectName("webWidget")
        self.adressLEdit = QtGui.QLineEdit(self.frame)
        self.adressLEdit.setGeometry(QtCore.QRect(10, 10, 261, 20))
        self.adressLEdit.setObjectName("adressLEdit")
        self.loadButton = QtGui.QPushButton(self.frame)
        self.loadButton.setGeometry(QtCore.QRect(290, 10, 75, 23))
        self.loadButton.setObjectName("loadButton")
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.loadButton.setText(QtGui.QApplication.translate("Form", "Load", None, QtGui.QApplication.UnicodeUTF8))

