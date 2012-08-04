import sys
from PySide.QtCore import *
from PySide.QtGui import *

#Greetings
def sayHello():
    print "Hello"

app = QApplication(sys.argv)
button = QPushButton("Click me");
button.clicked.connect(sayHello);
button.show()
app.exec_()

