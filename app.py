from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
import render_engine


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 470)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.setWindowIcon(QtGui.QIcon('Logos_and_icons\\app.ico'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        pixmap = QPixmap('Logos_and_icons\Image.jpg')
        self.label.setPixmap(pixmap)
        self.label.setGeometry(QtCore.QRect(100, 10,300, 250))


        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 270, 241, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        self.textlabel = QtWidgets.QLabel(self.centralwidget)
        self.textlabel.setText('File PATH:')
        self.textlabel.setGeometry(QtCore.QRect(10, 300, 380, 50))
        self.textlabel.setStyleSheet("border: 1px solid black;")

        self.textlabel2 = QtWidgets.QLabel(self.centralwidget)
        self.textlabel2.setText('IDLE')
        self.textlabel2.setGeometry(QtCore.QRect(170, 350, 380, 50))
        

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 300, 100, 50))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 400, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def getfiles(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Single File', '', '*')
        self.textlabel.setFont(QFont('Arial', 6))
        self.textlabel.setText(fileName)


    def getinformations(self):
        choice = self.comboBox.currentText()
        path=self.textlabel.text()
        path.replace('/','\\')
        if choice=='Image':
            choice=1
        else: 
            choice=2
        self.textlabel2.setText('Working!! Please Wait')
        try: 
            render_engine.interface_main(path,choice)
            self.textlabel2.setText('COMPLETED! ')
        except:
            self.textlabel2.setText('Error with File please try again!')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("ASCIIFY", "ASCIIFY"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Image"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Video"))
        
        
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.pushButton.clicked.connect(self.getfiles)
        self.pushButton_2.setText(_translate("MainWindow", "Convert"))
        self.pushButton_2.clicked.connect(self.getinformations)
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
