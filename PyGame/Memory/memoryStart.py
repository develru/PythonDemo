##############################################
#                                            #
#      Author: Richard Ruzsa (develru)       #
#      Email: develru [at] me . com          #
#                                            #
##############################################

import sys
#from PySide import QtCore
from PySide import QtGui
import memoryOO


class StartForm(QtGui.QDialog):

    def __init__(self, parent=None):
        """Init the main window"""
        super(StartForm, self).__init__(parent)
        self.setWindowTitle('Memory Game')
        self.startButton = QtGui.QPushButton('Start Game')
        self.quitButton = QtGui.QPushButton('Quit')
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.startButton)
        layout.addWidget(self.quitButton)
        self.setLayout(layout)
        self.quitButton.clicked.connect(QtGui.qApp.quit)
        self.startButton.clicked.connect(self.startGame)

    def startGame(self):
        """Start the memory game"""
        self.quitButton.setEnabled(False)
        game = memoryOO.Game()
        game.main()
        self.quitButton.setEnabled(True)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = StartForm()
    win.show()
    sys.exit(app.exec_())
