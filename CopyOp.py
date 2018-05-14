from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox
import os

class CopyOp(QtCore.QThread):
    signal = QtCore.pyqtSignal()
    def __init__(self, src, dest, prog, progt,butt,lab):
        super(CopyOp, self).__init__()
        self.source = src
        self.destination = dest
        self.progressbar = prog
        self.progressTotal = progt
        self.button = butt
        self.setlabel = lab

    def run(self):
        i = 0
        totalsize = 0
        for i in range(len(self.source)):
            totalsize += os.stat(self.source[i]).st_size

        i = 0
        totalcopied = 0
        for i in range(len(self.source)):
            name = self.source[i].rsplit('/', 1)[-1]
            self.setlabel.setText(self.source[i])
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
                            self.progressbar.setValue(perct)
                            self.progressTotal.setValue(percetotal)
                            mem += 1024
                            totalcopied += 1024
                        else:
                            self.setlabel.setText('Done')
                            self.button.setEnabled(True)
                            self.progressbar.setValue(100)
                            self.progressTotal.setValue(100)
                            break
                    #f1.close()
                #f.close()
                            