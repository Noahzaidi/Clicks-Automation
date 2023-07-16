from PyQt5.QtWidgets import QApplication
import sys
from GUI.GUI import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    sys.exit(app.exec_())