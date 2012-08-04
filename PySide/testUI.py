import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

import ui_test

class TestUI( QDialog ):
    def __init__( self, parent=None ):
        super( TestUI, self ).__init__( parent )
        self.ui = ui_test.Ui_Form(  )
        self.ui.setupUi( self )
        #self.ui.label.setText( "Hello" )
        self.ui.pushButton.clicked.connect( self.sayHello )

    def sayHello( self ):
        self.ui.label.setText( "Hello " + self.ui.lineEdit.text(  ) )

if __name__ == '__main__':
    print "test"
    app = QApplication( sys.argv )
    myc = TestUI(  )
    myc.show(  )
    #myc.myWidget.show(  )
    sys.exit( app.exec_(  ) )

