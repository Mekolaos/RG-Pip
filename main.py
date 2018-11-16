from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os

class App(QMainWindow):
	"""docstring for App"""
	def __init__(self):
		super().__init__()
		self.title = 'RG Pip'
		self.left = 300
		self.top = 300
		self.width = 800
		self.height = 600
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.colCh()
		
		#créer une textbox
		self.piped = QLineEdit(self)
		self.piped.move(30, 20)
		self.piped.resize(210, 40)
		self.piped.setStyleSheet("background-color:white;")

		#Créer une box pour output la liste de modules
		self.pipList = QFrame(self)
		self.pipList.move(410, 40)
		self.pipList.resize(380,450)
		self.pipList.setStyleSheet("background-color:white;")
		self.listLabel = QLabel('Info  : ', self)
		self.listLabel.move(410, 10)
		self.listLabel.setStyleSheet("color : white; font-size:15px;")

		#Créer un bouton pour installation standard
		self.installer = QPushButton('Install Module', self)
		self.installer.move(30, 65)
		self.installer.setStyleSheet("background-color:white;")

		#Créer un bouton pour une installation en sudo
		self.suInstaller = QPushButton('Sudo install', self)
		self.suInstaller.move(140, 65)
		self.suInstaller.setStyleSheet("background-color:white;")

		#Bouton de liste
		self.listerPip = QPushButton('Liste des modules', self)
		self.listerPip.move(410, 495)
		self.listerPip.resize(125, 30)
		self.listerPip.setStyleSheet("background-color:white;")

		#connecter les boutons
		self.installer.clicked.connect(self.on_click)
		self.suInstaller.clicked.connect(self.sudoClick)
		self.listerPip.clicked.connect(self.showList)
		self.show()
	#change color def
	def colCh(self):
		p=QPalette()
		gradient = QLinearGradient(0, 60, 0, 800)
		gradient.setColorAt(0.0, QColor(39, 85, 108))
		gradient.setColorAt(1.0, QColor(110, 146, 161))
		p.setBrush(QPalette.Window, QBrush(gradient))
		self.setPalette(p)

	@pyqtSlot()
	def on_click(self):
		myPip = self.piped.text()
		os.system('pip install ' + myPip)
		QMessageBox.question(self, 'Installé !', "Vous avez installé " + myPip + " avec succès !" , QMessageBox.Ok, QMessageBox.Ok)

	def sudoClick(self):
		suMyPip = self.piped.text()
		os.system('sudo pip install ' + suMyPip)
		QMessageBox.question(self, 'Installé !', "Vous avez installé " + suMyPip + " avec succès !", QMessageBox.Ok, QMessageBox.Ok)

	def showList(self):
		nukeList= os.popen('pip list -u').read()
		self.labelL = QLabel(nukeList, self)
		self.labelL.move(415, 50)
		self.labelL.show()



if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
		