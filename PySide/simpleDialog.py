import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Form( QDialog ):

    def __init__( self, parent=None ):
        super( Form, self ).__init__( parent )
        self.setWindowTitle( "My Fom" )
        self.edit = QLineEdit( "Write your name here..." )
        self.edit.selectAll( )
        self.edit.setFocus(  )
        self.button = QPushButton( "Shoe greetings" )
        layout = QVBoxLayout(  )
        layout.addWidget( self.edit )
        layout.addWidget( self.button )
        self.setLayout( layout )
        self.button.clicked.connect( self.greetings )

    def greetings( self ):
        print ( "Hello %s" % self.edit.text(  ) )

if __name__ == '__main__':
    app = QApplication( sys.argv )
    form = Form(  )
    form.show(  )
    sys.exit(app.exec_(  ))

