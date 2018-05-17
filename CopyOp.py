from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox
import os

class CopyOp(QtCore.QThread):
    signalBarSingle = QtCore.pyqtSignal(float)
    signalBarTotal = QtCore.pyqtSignal(float)
    signalFile = QtCore.pyqtSignal(str)
    signalButton = QtCore.pyqtSignal()
    def __init__(self, src, dest):
        super(CopyOp, self).__init__()
        self.source = src
        self.destination = dest
       

    def run(self):
        i = 0
        totalsize = 0
        for i in range(len(self.source)):
            totalsize += os.stat(self.source[i]).st_size

        i = 0
        totalcopied = 0
        for i in range(len(self.source)):
            name = self.source[i].rsplit('/', 1)[-1]

            #self.setlabel.setText(self.source[i])
            self.signalFile.emit(name)
            size = os.stat(self.source[i]).st_size
            with open(self.source[i], 'rb') as (f):
                with open(self.destination + name, 'wb') as (f1):
                    mem = 0
                    while True:
                        buf = f.read(1024)
                        f1.write(buf)
                        if buf:
                            perct = mem / size * 100
                            percetotal = totalcopied / totalsize * 100

                            #self.progressbar.setValue(perct)
                            self.signalBarSingle.emit(perct)

                            #self.progressTotal.setValue(percetotal)
                            self.signalBarTotal.emit(percetotal)
                            mem += 1024
                            totalcopied += 1024
                        else:
                            #self.setlabel.setText('Done')
                            self.signalFile.emit('Done')

                            #self.button.setEnabled(True)
                            self.signalButton.emit()

                            #self.progressbar.setValue(100)
                            self.signalBarSingle.emit(100.0)

                            #self.progressTotal.setValue(100)
                            self.signalBarSingle.emit(100.0)
                            break
                    #f1.close()
                #f.close()
                            