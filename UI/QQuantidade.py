# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Evaldo\workspace\MegaSena\src\UI\QQuantidade.ui'
#
# Created: Wed Dec 28 08:44:15 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QQuantidade(object):
    def setupUi(self, QQuantidade):
        QQuantidade.setObjectName(_fromUtf8("QQuantidade"))
        QQuantidade.setWindowModality(QtCore.Qt.NonModal)
        QQuantidade.resize(263, 159)
        QQuantidade.setWindowTitle(QtGui.QApplication.translate("QQuantidade", "Quantidade", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox = QtGui.QGroupBox(QQuantidade)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 191, 81))
        self.groupBox.setTitle(QtGui.QApplication.translate("QQuantidade", "Selecione", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayoutWidget = QtGui.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 28, 161, 41))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(-1, -1, 0, -1)
        self.formLayout.setHorizontalSpacing(1)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.numeroLabel = QtGui.QLabel(self.formLayoutWidget)
        self.numeroLabel.setText(QtGui.QApplication.translate("QQuantidade", "Quantidade", None, QtGui.QApplication.UnicodeUTF8))
        self.numeroLabel.setObjectName(_fromUtf8("numeroLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.numeroLabel)
        self.numeroSpinBox = QtGui.QSpinBox(self.formLayoutWidget)
        self.numeroSpinBox.setProperty("value", 10)
        self.numeroSpinBox.setObjectName(_fromUtf8("numeroSpinBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.numeroSpinBox)
        self.pushButtonOk = QtGui.QPushButton(QQuantidade)
        self.pushButtonOk.setGeometry(QtCore.QRect(90, 120, 75, 23))
        self.pushButtonOk.setText(QtGui.QApplication.translate("QQuantidade", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.action_ok = QtGui.QAction(QQuantidade)
        self.action_ok.setText(QtGui.QApplication.translate("QQuantidade", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ok.setObjectName(_fromUtf8("action_ok"))

        self.retranslateUi(QQuantidade)
        QtCore.QMetaObject.connectSlotsByName(QQuantidade)

    def retranslateUi(self, QQuantidade):
        pass

