# testes da Main são realizados aqui
import ui_V1 as jn
import sys


app = jn.QtWidgets.QApplication(sys.argv)
MainWindow = jn.QtWidgets.QMainWindow()
ui = jn.Ui_MainWindow()

path = "chromedriver"

ui.setupUi(MainWindow, path)
ui.setupBrowser(path)
MainWindow.show()
sys.exit(app.exec_())