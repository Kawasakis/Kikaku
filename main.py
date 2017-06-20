import sys
import PySide.QtGui
import PySide.QtUiTools
import PySide.QtCore
import os.path


class MainForm(PySide.QtGui.QDialog):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.ui = PySide.QtUiTools.QUiLoader().load('./MainUI.ui')
        self.establishConnection()

    def openFile(self):
    	filename=PySide.QtGui.QFileDialog.getOpenFileName(self,'Open file',os.path.expanduser('~')+'/Desktop')


    def establishConnection(self):	
        self.ui.Open_file_button.clicked.connect(self.openFile)

if __name__ == '__main__':
    app = PySide.QtGui.QApplication(sys.argv)

    main_form = MainForm()
    main_form.ui.show()

    sys.exit(app.exec_())
