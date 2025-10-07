from PyQt5.QtWidgets import QApplication
from MainWindow.clsMainWindow import clsMainWindow
import sys

app=QApplication([])
f=clsMainWindow()
f.show()
sys.exit(app.exec_())