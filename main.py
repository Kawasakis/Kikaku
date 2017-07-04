import sys
import PySide.QtGui
import PySide.QtUiTools
import PySide.QtCore
import os.path


class MainForm(PySide.QtGui.QMainWindow,PySide.QtGui.QDialog):
    def __init__(self,parent=None):
        super(MainForm,self).__init__(parent)
        self.ui=PySide.QtUiTools.QUiLoader().load('./MainUI_2.ui')
                
        # self.scene=PySide.QtGui.QGraphicsScene(self)
        # item=PySide.QtGui.QGraphicsPixmapItem(pixmap)
        # self.scene.addItem(item)
        # self.ui.view1.setScene(self.scene)
           
        self.establish_connection()
        self.button_1=PySide.QtGui.QPushButton('open_file_1')
        self.button_2=PySide.QtGui.QPushButton('open_file_2')       
        
    def open_file_1(self):
        filename=PySide.QtGui.QFileDialog.getOpenFileName(self,'Open file',os.path.expanduser('~')+ '/Desktop/kikaku/pictures/')
        self.x=filename[0]
        self.picture_1(self.x)

    def open_file_2(self):
        filename=PySide.QtGui.QFileDialog.getOpenFileName(self,'Open file',os.path.expanduser('~')+ '/Desktop/kikaku/pictures/')
        self.y=filename[0]
        self.picture_2(self.y)
        
    def establish_connection(self):
        self.ui.button_1.clicked.connect(self.open_file_1)
        self.ui.button_2.clicked.connect(self.open_file_2)

    def picture_1(self,x):
        pixmap=PySide.QtGui.QPixmap()
        pixmap.load(self.x)
        self.scene=PySide.QtGui.QGraphicsScene(self)
        item=PySide.QtGui.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.ui.view_1.setScene(self.scene)

    def picture_2(self,y):
        pixmap=PySide.QtGui.QPixmap()
        pixmap.load(self.y)
        self.scene=PySide.QtGui.QGraphicsScene(self)
        item=PySide.QtGui.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.ui.view_2.setScene(self.scene)

if __name__=='__main__':
    app=PySide.QtGui.QApplication(sys.argv)
    
    # pixmap=PySide.QtGui.QPixmap()
    # pixmap.load('')

    main_form=MainForm()
    main_form.ui.show()
        
    sys.exit(app.exec_())