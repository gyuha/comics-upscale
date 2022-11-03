import PySide6.QtCore
import os, sys

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTranslator, QLibraryInfo
from MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    translator = QTranslator()
    translator.load("ko_KR.qm", directory="./lang")
    app.installTranslator(translator)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
