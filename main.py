import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *
from des import *
import time
import asyncio
from about import *



class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.toolButton_5.clicked.connect(self.about)
        self.ui.toolButton_4.clicked.connect(self.search)
        self.ui.toolButton_3.clicked.connect(self.back)
        self.ui.toolButton.clicked.connect(self.update)
        self.ui.toolButton_2.clicked.connect(self.home)
        self.web = QWebEngineView()
        self.ui.gridLayout.addWidget(self.web, 1, 0, 1, 7)

        self.ui.toolButton.setToolTip('Обновить')
        self.ui.toolButton_2.setToolTip('Главная')
        self.ui.toolButton_3.setToolTip('Назад')
        self.ui.toolButton_4.setToolTip('Поиск')
        self.ui.toolButton_5.setToolTip('О программе')




    def home(self):
        home_page = QtCore.QUrl('https://duckduckgo.com')
        self.web.load(home_page)

    def update(self):
        self.web.reload()

    def back(self):
        self.web.back()

    def search(self):
        text = self.ui.lineEdit.text()
        if len(text) > 0:
            if not text.startswith('http'):
                text = QtCore.QUrl('https://duckduckgo.com/?q=' + text)
            else:
                text = QtCore.QUrl(text)
            self.web.load(text)

    def about(self):
        window = about_information(self)
        window.show()



class about_information(QtWidgets.QWidget):
    def __init__(self, parent=QtGui):
        super().__init__(parent, QtCore.Qt.Window)
        self.modal = Ui_Form()
        self.modal.setupUi(self)
        self.setWindowModality(2)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
