import sys
from PySide import QtCore, QtGui
from PySide import QtUiTools, QtWebKit
import webUi

class myWebView:
    def __init__( self ):
        #self.webForm = webUi.Ui_Form(  )
        #self.widget = QtGui.QWidget( )
        #self.webForm.setupUi( self.widget )
        self.web = QtWebKit.QWebView( )
        #self.webForm.verticalLayout.addWidget( self.web )
        self.web.load( QtCore.QUrl("http://www.google.com" ))
        #self.web.load( QtCore.QUrl("test.htm") )

if __name__ == '__main__':
    app = QtGui.QApplication( sys.argv )
    webView = myWebView(  )
    webView.web.show(  )
    sys.exit( app.exec_(  ))

