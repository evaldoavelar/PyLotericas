# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Evaldo\workspace\MegaSena\src\UI\QfrmPrincipal.ui'
#
# Created: Wed Dec 28 08:44:14 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(823, 631)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(2, -1, -1, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(5, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.horizontalWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalWidget.setObjectName(_fromUtf8("horizontalWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Selecione a Loteria", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lblStatus = QtGui.QLabel(self.horizontalWidget)
        self.lblStatus.setText(QtGui.QApplication.translate("MainWindow", "_", None, QtGui.QApplication.UnicodeUTF8))
        self.lblStatus.setObjectName(_fromUtf8("lblStatus"))
        self.horizontalLayout.addWidget(self.lblStatus)
        self.gridLayout.addWidget(self.horizontalWidget, 1, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.listSelecionados = QtGui.QListWidget(self.centralwidget)
        self.listSelecionados.setMaximumSize(QtCore.QSize(16777215, 92))
        self.listSelecionados.setObjectName(_fromUtf8("listSelecionados"))
        self.verticalLayout.addWidget(self.listSelecionados)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(0, 1, 0, 0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnAdicionar = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAdicionar.sizePolicy().hasHeightForWidth())
        self.btnAdicionar.setSizePolicy(sizePolicy)
        self.btnAdicionar.setMaximumSize(QtCore.QSize(120, 120))
        self.btnAdicionar.setText(QtGui.QApplication.translate("MainWindow", "Adicionar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdicionar.setFlat(False)
        self.btnAdicionar.setObjectName(_fromUtf8("btnAdicionar"))
        self.horizontalLayout_2.addWidget(self.btnAdicionar)
        self.btnCopiar = QtGui.QPushButton(self.centralwidget)
        self.btnCopiar.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btnCopiar.setText(QtGui.QApplication.translate("MainWindow", "Copiar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCopiar.setObjectName(_fromUtf8("btnCopiar"))
        self.horizontalLayout_2.addWidget(self.btnCopiar)
        self.btnSalvar = QtGui.QPushButton(self.centralwidget)
        self.btnSalvar.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btnSalvar.setText(QtGui.QApplication.translate("MainWindow", "Salvar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))
        self.horizontalLayout_2.addWidget(self.btnSalvar)
        self.btnRemover = QtGui.QPushButton(self.centralwidget)
        self.btnRemover.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btnRemover.setText(QtGui.QApplication.translate("MainWindow", "Remover", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRemover.setObjectName(_fromUtf8("btnRemover"))
        self.horizontalLayout_2.addWidget(self.btnRemover)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(15, 15, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(15, 15, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuLotericas = QtGui.QMenu(self.menubar)
        self.menuLotericas.setTitle(QtGui.QApplication.translate("MainWindow", "Lotericas", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLotericas.setObjectName(_fromUtf8("menuLotericas"))
        self.menuGrid = QtGui.QMenu(self.menubar)
        self.menuGrid.setTitle(QtGui.QApplication.translate("MainWindow", "Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.menuGrid.setObjectName(_fromUtf8("menuGrid"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setBaseSize(QtCore.QSize(20, 20))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(MainWindow)
        self.toolBar_2.setEnabled(True)
        self.toolBar_2.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar_2", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.toolBar_2.setAutoFillBackground(False)
        self.toolBar_2.setMovable(True)
        self.toolBar_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar_2.setFloatable(False)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar_2)
        self.action_atualizar = QtGui.QAction(MainWindow)
        self.action_atualizar.setText(QtGui.QApplication.translate("MainWindow", "Atualizar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_atualizar.setObjectName(_fromUtf8("action_atualizar"))
        self.action_resultado_Sorteios = QtGui.QAction(MainWindow)
        self.action_resultado_Sorteios.setText(QtGui.QApplication.translate("MainWindow", "Resultado Sorteios", None, QtGui.QApplication.UnicodeUTF8))
        self.action_resultado_Sorteios.setObjectName(_fromUtf8("action_resultado_Sorteios"))
        self.action_sorteio_Por_Dezenas = QtGui.QAction(MainWindow)
        self.action_sorteio_Por_Dezenas.setText(QtGui.QApplication.translate("MainWindow", "Sorteio Por Dezenas", None, QtGui.QApplication.UnicodeUTF8))
        self.action_sorteio_Por_Dezenas.setObjectName(_fromUtf8("action_sorteio_Por_Dezenas"))
        self.action_sortear_Dezenas = QtGui.QAction(MainWindow)
        self.action_sortear_Dezenas.setText(QtGui.QApplication.translate("MainWindow", "Sortear Dezenas", None, QtGui.QApplication.UnicodeUTF8))
        self.action_sortear_Dezenas.setObjectName(_fromUtf8("action_sortear_Dezenas"))
        self.action_atualizar_Todas = QtGui.QAction(MainWindow)
        self.action_atualizar_Todas.setText(QtGui.QApplication.translate("MainWindow", "Atualizar Todas", None, QtGui.QApplication.UnicodeUTF8))
        self.action_atualizar_Todas.setObjectName(_fromUtf8("action_atualizar_Todas"))
        self.action_sair = QtGui.QAction(MainWindow)
        self.action_sair.setText(QtGui.QApplication.translate("MainWindow", "Sair", None, QtGui.QApplication.UnicodeUTF8))
        self.action_sair.setShortcut(QtGui.QApplication.translate("MainWindow", "Esc", None, QtGui.QApplication.UnicodeUTF8))
        self.action_sair.setObjectName(_fromUtf8("action_sair"))
        self.action_mega_Sena = QtGui.QAction(MainWindow)
        self.action_mega_Sena.setText(QtGui.QApplication.translate("MainWindow", "Mega Sena", None, QtGui.QApplication.UnicodeUTF8))
        self.action_mega_Sena.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+M", None, QtGui.QApplication.UnicodeUTF8))
        self.action_mega_Sena.setObjectName(_fromUtf8("action_mega_Sena"))
        self.action_quina = QtGui.QAction(MainWindow)
        self.action_quina.setText(QtGui.QApplication.translate("MainWindow", "Quina", None, QtGui.QApplication.UnicodeUTF8))
        self.action_quina.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_quina.setObjectName(_fromUtf8("action_quina"))
        self.action_loto_facil = QtGui.QAction(MainWindow)
        self.action_loto_facil.setText(QtGui.QApplication.translate("MainWindow", "Loto Facil", None, QtGui.QApplication.UnicodeUTF8))
        self.action_loto_facil.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.action_loto_facil.setObjectName(_fromUtf8("action_loto_facil"))
        self.action_loto_mania = QtGui.QAction(MainWindow)
        self.action_loto_mania.setText(QtGui.QApplication.translate("MainWindow", "Loto Mania", None, QtGui.QApplication.UnicodeUTF8))
        self.action_loto_mania.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.action_loto_mania.setObjectName(_fromUtf8("action_loto_mania"))
        self.action_dupla_sena = QtGui.QAction(MainWindow)
        self.action_dupla_sena.setText(QtGui.QApplication.translate("MainWindow", "Dupla Sena", None, QtGui.QApplication.UnicodeUTF8))
        self.action_dupla_sena.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_dupla_sena.setObjectName(_fromUtf8("action_dupla_sena"))
        self.action_time_mania = QtGui.QAction(MainWindow)
        self.action_time_mania.setText(QtGui.QApplication.translate("MainWindow", "Time Mania", None, QtGui.QApplication.UnicodeUTF8))
        self.action_time_mania.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+T", None, QtGui.QApplication.UnicodeUTF8))
        self.action_time_mania.setObjectName(_fromUtf8("action_time_mania"))
        self.action_ajustar_colunas = QtGui.QAction(MainWindow)
        self.action_ajustar_colunas.setText(QtGui.QApplication.translate("MainWindow", "Ajustar Colunas", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ajustar_colunas.setObjectName(_fromUtf8("action_ajustar_colunas"))
        self.action_ajustar_linhas = QtGui.QAction(MainWindow)
        self.action_ajustar_linhas.setText(QtGui.QApplication.translate("MainWindow", "Ajustar Linhas", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ajustar_linhas.setObjectName(_fromUtf8("action_ajustar_linhas"))
        self.action_adicionar_selecionados = QtGui.QAction(MainWindow)
        self.action_adicionar_selecionados.setText(QtGui.QApplication.translate("MainWindow", "Adicionar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_adicionar_selecionados.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_adicionar_selecionados.setObjectName(_fromUtf8("action_adicionar_selecionados"))
        self.menuLotericas.addAction(self.action_atualizar_Todas)
        self.menuLotericas.addAction(self.action_sair)
        self.menuGrid.addAction(self.action_ajustar_colunas)
        self.menuGrid.addAction(self.action_ajustar_linhas)
        self.menubar.addAction(self.menuLotericas.menuAction())
        self.menubar.addAction(self.menuGrid.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_atualizar)
        self.toolBar.addAction(self.action_resultado_Sorteios)
        self.toolBar.addAction(self.action_sorteio_Por_Dezenas)
        self.toolBar.addAction(self.action_sortear_Dezenas)
        self.toolBar_2.addAction(self.action_mega_Sena)
        self.toolBar_2.addAction(self.action_quina)
        self.toolBar_2.addAction(self.action_loto_facil)
        self.toolBar_2.addAction(self.action_loto_mania)
        self.toolBar_2.addAction(self.action_dupla_sena)
        self.toolBar_2.addAction(self.action_time_mania)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

