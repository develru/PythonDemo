import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

import test


class TestUI:
    def __init__( self):
        self.ui = test.Ui_Form()
        self.widget = QWidget()
        self.ui.setupUi(self.widget)
        #self.ui.label.setText("Hello")
        self.ui.pushButton.clicked.connect(self.sayHello)

    def sayHello( self ):
        self.ui.label.setText("Hello " + self.ui.lineEdit.text())

if __name__ == '__main__':
    print "test"
    app = QApplication(sys.argv)
    myc = TestUI()
    myc.widget.show()
    sys.exit(app.exec_())

