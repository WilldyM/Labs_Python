import sys
from PyQt4 import QtGui
from lab3_5ui import Ui_MainWindow
from lab3_4 import StringFormatter

class Main(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.buttonGroup = QtGui.QButtonGroup()#объединили радио баттоны
        self.buttonGroup.addButton(self.radioLeks)
        self.buttonGroup.addButton(self.radioRazmer)

        self.radioLeks.setDisabled(True)
        self.radioRazmer.setDisabled(True)

        self.checkSort.stateChanged.connect(self.SortChanged)
        self.buttonFormat.clicked.connect(self.BFormat)

    def SortChanged(self, b):
        if b == 2:
            self.radioLeks.setDisabled(False)
            self.radioRazmer.setDisabled(False)
            
        else:
            self.radioLeks.setDisabled(True)
            self.radioRazmer.setDisabled(True)

    def BFormat(self):
        string = self.strokaEdit.text()
        ss = StringFormatter(string)
        if self.checkDelWords.isChecked():
            val = int(self.spinBox.value())
            string = ss.delwords(val).__str__()
        if self.checkZamena.isChecked():
            ss = StringFormatter(string)
            string = ss.zamena().__str__()
        if self.checkProbel.isChecked():
            ss = StringFormatter(string)
            string = ss.probel().__str__()
        if self.checkSort.isChecked() and self.radioRazmer.isChecked():
            ss = StringFormatter(string)
            string = ss.sortPoRazmeru().__str__()
        elif self.checkSort.isChecked() and self.radioLeks.isChecked():
            ss = StringFormatter(string)
            string = ss.sortPoLeks().__str__()



        self.resultEdit.setText(string)
        




app = QtGui.QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())
