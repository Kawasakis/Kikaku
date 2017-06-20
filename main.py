import sys
import PySide.QtGui
import PySide.QtUiTools


class MainForm(PySide.QtGui.QDialog):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.ui = PySide.QtUiTools.QUiLoader().load('./MainUI.ui')

if __name__ == '__main__':
    app = PySide.QtGui.QApplication(sys.argv)

    main_form = MainForm()
    main_form.ui.show()

    sys.exit(app.exec_())
