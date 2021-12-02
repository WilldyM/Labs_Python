# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab3_3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(367, 320)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 371, 281))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 367, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionAddToLog = QtGui.QAction(MainWindow)
        self.actionAddToLog.setObjectName(_fromUtf8("actionAddToLog"))
        self.actionView = QtGui.QAction(MainWindow)
        self.actionView.setObjectName(_fromUtf8("actionView"))
        self.menu.addAction(self.actionOpen)
        self.menu_2.addAction(self.actionExport)
        self.menu_2.addAction(self.actionAddToLog)
        self.menu_2.addAction(self.actionView)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menu.setTitle(_translate("MainWindow", "Файл", None))
        self.menu_2.setTitle(_translate("MainWindow", "Лог", None))
        self.actionOpen.setText(_translate("MainWindow", "Открыть", None))
        self.actionExport.setText(_translate("MainWindow", "Экспорт", None))
        self.actionAddToLog.setText(_translate("MainWindow", "Добавить в лог", None))
        self.actionView.setText(_translate("MainWindow", "Просмотр", None))

