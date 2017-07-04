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
        self.button1=PySide.QtGui.QPushButton('open_file')     
        
    def open_file(self):
        filename=PySide.QtGui.QFileDialog.getOpenFileName(self,'Open file',os.path.expanduser('~')+ '/Desktop/kikaku/')
        self.x=filename[0]
        self.picture(self.x)
        
    def establish_connection(self):
        self.ui.button1.clicked.connect(self.open_file)

    def picture(self,x):
        pixmap=PySide.QtGui.QPixmap()
        pixmap.load(self.x)
        self.scene=PySide.QtGui.QGraphicsScene(self)
        item=PySide.QtGui.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.ui.view1.setScene(self.scene)

if __name__=='__main__':
    app=PySide.QtGui.QApplication(sys.argv)
    
    # pixmap=PySide.QtGui.QPixmap()
    # pixmap.load('')

    main_form=MainForm()
    main_form.ui.show()
        
    sys.exit(app.exec_())