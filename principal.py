import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtWidgets import QFileDialog
from pytube import YouTube



class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("mainwindow.ui", self)
        self.buttonAdd = self.findChild(QtWidgets.QPushButton, 'btnAdd') # Find the button
        self.buttonAdd.clicked.connect(self.add_song)
        self.buttonOpen = self.findChild(QtWidgets.QPushButton, 'btnOpen') # Find the button
        self.buttonOpen.clicked.connect(self.open_folder)
        self.buttonOpen = self.findChild(QtWidgets.QPushButton, 'btnDownload') # Find the button
        self.buttonOpen.clicked.connect(self.download_song)
    
    def add_song(self):      
      #print ("hello fbnnt")      
      #copiamos texto de textboxy y lo pegamos en la caja de texto grande
      text= self.lineEdit.text()
      self.listWidget.addItem(text)
      self.lineEdit.clear()
    
    def open_folder(self):
        global path
        path = QFileDialog.getExistingDirectory()
        #self.lineEdit_2.text(path)
        self.lineEdit_2.setText(path)
        
        print(path)
    
    
    def download_song(self):
        print ("descargar rola")
        if self.listWidget.count() > 0:
            print (self.listWidget.count())
            for i in range(self.listWidget.count()):
                print (self.listWidget.item(i).text())
                
                #index=self.listWidget.currentRow(i)+1
                yt = YouTube(self.listWidget.item(i).text())
                video = yt.streams.get_highest_resolution()
                #print (video)
                #print (path)
                video.download(path)
                #iterow = self.listWidget.currentRow() #not working
                #self.listWidget.takeItem(iterow)      #not working
                
                
            self.listWidget.clear()  
               
        else:
            print ("Lista vacia")
        

if __name__ == '__main__':  
   app = QtWidgets.QApplication(sys.argv)
   window = MainWindow()
   window.setFixedSize(979,474)
   window.showMaximized()
   #windows.showMaximized()
   app.exec()
   