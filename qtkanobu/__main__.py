import sys
from PyQt5 import QtWidgets
from qtkanobu.mainwindow import design
from qtkanobu.result import resdesign
    
class QtKanobu(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(QtKanobu, self).__init__()
        self.setupUi(self)
        
        self.pushButton_1.clicked.connect(lambda a : self.game(num=0))
        self.pushButton_2.clicked.connect(lambda a : self.game(num=1))
        self.pushButton_3.clicked.connect(lambda a : self.game(num=2))
        
    def game(self, num):
        import random

        bot = random.randint(0, 2)

        massive = [
            [2, 0, 1],
            [1, 2, 0],
            [0, 1, 2]
        ]

        i = 0
        for key in massive[num]:

            if bot == i:

                result = Result(windowtype=i)
                    #reswindow.show()
                result.exec_()

            i += 1
        
class Result(QtWidgets.QDialog, resdesign.Ui_Dialog):
    def __init__(self, windowtype):
        super(Result, self).__init__()
        self.setupUi(self)
        
        print(windowtype)
        
        if windowtype == 0:
            pass
        
        elif windowtype == 1:
            self.label.setText("<html><head/><body><p><img src=\":/img/img/main/Misc_R.I.P.png\"/></p></body></html>")
            self.label_2.setText("You lose!")
            self.label_3.setText("Paper VS. rock")
            
        elif windowtype == 2:
            self.label.setText("<html><head/><body><p><img src=\":/img/img/main/Server_MediaAddonServer.png\"/></p></body></html>")
            self.label_2.setText("Draw!")
            self.label_3.setText("Paper VS. paper")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtKanobu()
    window.show()
    app.exec_()
    
if __file__ == "__main__":
    main()
