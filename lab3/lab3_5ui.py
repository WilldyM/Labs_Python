# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab3_5.ui'
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
        MainWindow.resize(402, 389)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.strokaEdit = QtGui.QLineEdit(self.centralwidget)
        self.strokaEdit.setGeometry(QtCore.QRect(70, 20, 321, 20))
        self.strokaEdit.setObjectName(_fromUtf8("strokaEdit"))
        self.checkDelWords = QtGui.QCheckBox(self.centralwidget)
        self.checkDelWords.setGeometry(QtCore.QRect(70, 60, 191, 17))
        self.checkDelWords.setObjectName(_fromUtf8("checkDelWords"))
        self.checkZamena = QtGui.QCheckBox(self.centralwidget)
        self.checkZamena.setGeometry(QtCore.QRect(70, 90, 191, 17))
        self.checkZamena.setObjectName(_fromUtf8("checkZamena"))
        self.checkProbel = QtGui.QCheckBox(self.centralwidget)
        self.checkProbel.setGeometry(QtCore.QRect(70, 120, 221, 17))
        self.checkProbel.setObjectName(_fromUtf8("checkProbel"))
        self.checkSort = QtGui.QCheckBox(self.centralwidget)
        self.checkSort.setGeometry(QtCore.QRect(70, 150, 191, 17))
        self.checkSort.setObjectName(_fromUtf8("checkSort"))
        self.radioRazmer = QtGui.QRadioButton(self.centralwidget)
        self.radioRazmer.setGeometry(QtCore.QRect(110, 180, 91, 17))
        self.radioRazmer.setObjectName(_fromUtf8("radioRazmer"))
        self.radioLeks = QtGui.QRadioButton(self.centralwidget)
        self.radioLeks.setGeometry(QtCore.QRect(110, 200, 121, 17))
        self.radioLeks.setObjectName(_fromUtf8("radioLeks"))
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(270, 58, 41, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.buttonFormat = QtGui.QPushButton(self.centralwidget)
        self.buttonFormat.setGeometry(QtCore.QRect(70, 230, 281, 41))
        self.buttonFormat.setObjectName(_fromUtf8("buttonFormat"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 310, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.resultEdit = QtGui.QLineEdit(self.centralwidget)
        self.resultEdit.setGeometry(QtCore.QRect(80, 310, 311, 20))
        self.resultEdit.setObjectName(_fromUtf8("resultEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "StringFormatter Demo", None))
        self.label.setText(_translate("MainWindow", "Строка:", None))
        self.checkDelWords.setText(_translate("MainWindow", "Удалить слова размером меньше", None))
        self.checkZamena.setText(_translate("MainWindow", "Заменить все цифры на *", None))
        self.checkProbel.setText(_translate("MainWindow", "Вставить по пробелу между символами", None))
        self.checkSort.setText(_translate("MainWindow", "Сортировать слова в строке", None))
        self.radioRazmer.setText(_translate("MainWindow", "По размеру", None))
        self.radioLeks.setText(_translate("MainWindow", "Лексиграфически", None))
        self.buttonFormat.setText(_translate("MainWindow", "Форматировать", None))
        self.label_2.setText(_translate("MainWindow", "Результат:", None))

