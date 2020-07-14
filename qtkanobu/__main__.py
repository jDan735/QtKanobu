import sys
from PyQt5 import QtWidgets
from qtkanobu.mainwindow import design
    
class QtKanobu(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(QtKanobu, self).__init__()
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtKanobu()
    window.show()
    app.exec_()
    
if __file__ == "__main__":
    main()
