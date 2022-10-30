import time
from PySide6.QtCore import QThread


import MainWindow

class ItemStateWorker(QThread):

    def __init__(self, parent: MainWindow):
        super(ItemStateWorker, self).__init__()
        self._parent = parent
        self._stop = False
    
    def run(self):
        while(True):
            if self._stop == True:
                return
            time.sleep(0.1)
    
    def stop(self):
        self._stop = True
