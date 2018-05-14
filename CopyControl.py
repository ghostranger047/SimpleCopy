from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from CopyUi import Ui_MainWindow
from CopyOp import CopyOp
from PyQt5.QtWidgets import QMessageBox
import sys

class CopyControl(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(CopyControl, self).__init__()
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.progressBar_2.setValue(0)
        self.copyButton.clicked.connect(self.copy)
        self.sourceloc = ''
        self.destination = ''
        self.sourceButton.clicked.connect(self.setSource)
        self.destButton.clicked.connect(self.setDest)
        self.pushButton.clicked.connect(self.stopCopy)
        self.pushButton.setEnabled(False)
        self.center()
        self.thread = None


    def initThread(self):
        self.thread = CopyOp(self.sourceloc,self.destination,self.progressBar,self.progressBar_2,self.copyButton,self.clabel)

    def copy(self):

        self.progressBar.setValue(0)
        self.progressBar_2.setValue(0)
        self.copyButton.setEnabled(False)
        self.initThread()
        self.thread.start()
        self.pushButton.setEnabled(True)

    def stopCopy(self):

        self.thread.quit()



    def setSource(self):
        self.source.setPlainText('')
        options = QtWidgets.QFileDialog.Options()
        self.sourceloc, _ = QtWidgets.QFileDialog.getOpenFileNames(None,"Select File/Files", "","All Files (*);;Python Files (*.py)", options=options)
        i = ''
        #print(self.sourceloc)
        #print(len(self.sourceloc[i]))
        for i in self.sourceloc:
            self.source.append(i+';')
            #print(i)


    def setDest(self):
        self.destination = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.destination = self.destination+'/'
        self.dest.setPlainText(self.destination)
        #print(self.destination+'/')


    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())


    def message(self, txt):
        QMessageBox.about(self, "Success", txt)





if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    form = CopyControl()
    form.show()
    form.setFixedSize(form.size())
    sys.exit(app.exec_())
