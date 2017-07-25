import sys
import PyQt4.QtGui
import PyQt4.uic
import PyQt4.QtCore
import os.path
import random
import glob
from PIL import Image
import numpy as np



class MainForm(PyQt4.QtGui.QMainWindow):
    def __init__(self,filelist=[],parent=None):
        super(MainForm,self).__init__(parent)
        PyQt4.uic.loadUi('./MainUI_2.ui', self)
        self.filelist=glob.glob('/home/kanglab/Desktop/kikaku/pictures/*.jpg')                 
        self.establish_connection()
    
        
    def open_file_1(self):
        filename=PyQt4.QtGui.QFileDialog.getOpenFileName(self,'Open file',os.path.expanduser('~')+ '/Desktop/kikaku/pictures/')
        self.x=filename
        self.picture_1()

    def open_file_2(self):
        # filelist=glob.glob('/home/kanglab/Desktop/kikaku/pictures/*.jpg')
        self.y=self.filelist[random.randint(0,3)]
        self.picture_2()
        
    def establish_connection(self):
        self.button_1.clicked.connect(self.open_file_1)
        self.button_2.clicked.connect(self.open_file_2)

    def picture_1(self):      
        pixmap_1=PyQt4.QtGui.QPixmap(self.x)
        pixmap_re_1=pixmap_1.scaled(205,255)
        self.scene=PyQt4.QtGui.QGraphicsScene()
        item=PyQt4.QtGui.QGraphicsPixmapItem(pixmap_re_1)
        self.scene.addItem(item)
        self.view_1.setScene(self.scene)

    def picture_2(self):
        pixmap_2=PyQt4.QtGui.QPixmap(self.y)
        pixmap_re_2=pixmap_2.scaled(205,255)
        self.scene=PyQt4.QtGui.QGraphicsScene()
        item=PyQt4.QtGui.QGraphicsPixmapItem(pixmap_re_2)
        self.scene.addItem(item)    
        self.view_2.setScene(self.scene)

if __name__=='__main__':
    app=PyQt4.QtGui.QApplication(sys.argv)

    main_form=MainForm()
    main_form.show()
        
    sys.exit(app.exec_())