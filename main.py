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
		self.left = 10
		self.top = 10
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
		self.piped.resize(200, 40)
		self.piped.setStyleSheet("background-color:white;")

		#Créer un bouton
		self.installer = QPushButton('Install Module', self)
		self.installer.move(30, 80)
		self.installer.setStyleSheet("background-color:white;")

		#connecter le bouton à la textbox
		self.installer.clicked.connect(self.on_click)
		self.show()
	#change color def
	def colCh(self):
		p=QPalette()
		gradient = QLinearGradient(0, 0, 0, 400)
		gradient.setColorAt(0.0, QColor(39, 85, 108))
		gradient.setColorAt(1.0, QColor(110, 146, 161))
		p.setBrush(QPalette.Window, QBrush(gradient))
		self.setPalette(p)

	@pyqtSlot()
	def on_click(self):
		myPip = self.piped.text()
		os.system('pip install ' + myPip)
		QMessageBox.question(self, 'Installé !', "Vous avez installé avec succès " + myPip, QMessageBox.Ok, QMessageBox.Ok)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
		