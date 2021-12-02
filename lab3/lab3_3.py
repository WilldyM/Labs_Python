# -*- coding: utf-8 -*-
import re
import sys
import datetime
import os

from PyQt4 import QtGui, QtCore

from lab3_3ui import Ui_MainWindow

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.setCentralWidget(self.textEdit)
        self.setWindowTitle('Скрипт 18. Искатель строк')
        if not os.path.exists('script18.log'):
            self.showMess()

        self.items = []
        
        self.actionOpen.triggered.connect(self.AOpen)
        self.actionAddToLog.triggered.connect(self.ALog)
        self.actionExport.triggered.connect(self.AExport)
        self.actionView.triggered.connect(self.AView)

    def AView(self):
        reply = QtGui.QMessageBox.question(self, 'Message',
            'Вы действительно хотите открыть лог?\nДанные последних поисков будут потеряны!', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.No:
            return
        self.textEdit.clear()
        with open('script18.log', 'rt') as f:
            self.textEdit.setText(f.read())
            self.items = self.textEdit.toPlainText()
            self.textEdit.append('\n')
        self.statusbar.showMessage('Открыт лог')

    def AExport(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save as...', os.getcwd())
        if filename:
            with open(filename, 'wt') as f:
                f.writelines(self.items)
        self.statusbar.showMessage('Экспорт файла {}'.format(filename))

    def ALog(self):
        with open('script18.log', 'a') as f:
            f.writelines(self.items)
        self.statusbar.showMessage('Файл лога дописан')
            

    def showMess(self):
        self.msg = QtGui.QMessageBox()
        self.msg.setText('Файл лога не найден.\nФайл лога будет создан автоматически')
        self.msg.setWindowTitle('information')
        self.msg.show()
        open('script18.log', 'wt').close()

    def AOpen(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'openfile')
        if '.log' in filename:
            with open(filename, 'rt') as f:
                self.textEdit.append(''.join(f.readlines())+'\n')
                self.statusbar.showMessage('Открыт лог {}'.format(filename))
                return
            
        try:
            with open(filename, 'rt') as f:
                lines = f.readlines()
        except IOError as err:
            return

        now = datetime.datetime.now()
        self.textEdit.append('Файл {0} был обработан {1}:\n'.format(filename, now.strftime("%d.%m.%Y %H:%M:%S")))
        lines = list(map(lambda x: x.rstrip(), lines))
        for i,line in enumerate(lines):
            result = re.findall(r'\w+\s\w+\s=\s\d+', line)
            
            for res in result:
                if res != []:
                    self.textEdit.append('Строка {0}: найдено \'{1}\''.format(i+1,res))
    
        self.textEdit.append('')
        self.items = self.textEdit.toPlainText()
        self.statusbar.showMessage('Обработан файл {}'.format(filename))
            
        

def main():
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

main()
