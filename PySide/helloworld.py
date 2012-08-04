
import sys 
from PySide.QtCore import *
from PySide.QtGui import *

def test(valami):
    print valami

app = QApplication(sys.argv)
label = QLabel("<font color=green size=40>Hello World</font>")
label.show()
app.exec_()
sys.exit()
