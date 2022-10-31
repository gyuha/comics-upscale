from enum import Enum
from pathlib import Path
import os
import re
import shutil
import threading
import time
import zipfile
from PySide6.QtCore import QObject, QThread, Signal, Slot
from multiprocessing import cpu_count
from multiprocessing.pool import ThreadPool
from PySide6.QtCore import QObject, Signal
from multiprocessing import cpu_count
from util.Config import Config


class UnzipSignal(QObject):
    unzip_state = Signal(str, bool, int, int)


class Unzip(QThread):
    signals = UnzipSignal()

    def __init__(self, parent, file_path: str):
        QThread.__init__(self, parent)
        self._parent = parent

        self.id = file_path
        self.src_path = file_path

        self.config = Config()
        self.target_dir = Path(self.config.data["temp_dir"]).absolute()
        self.re_image = self.config.re_image_extension()

    def run(self):
        unzip_thread = threading.Thread(target=self._unzip_files)
        unzip_thread.start()
        self.signals.unzip_state.emit(self.id, False, 0, 1)
    
    def _unzip_files(self):
        print('📢[Unzip.py:41]', self.id)
        if os.path.exists(self.target_dir):
            shutil.rmtree(self.target_dir)

        os.mkdir(self.target_dir)

        zip_file = zipfile.ZipFile(self.src_path)

        total = len(zip_file.namelist())
        for idx, file in enumerate(zip_file.namelist()):
            self.signals.unzip_state.emit(self.id, False, idx + 1, total)
            zip_file.extract(file, self.target_dir)
        self.signals.unzip_state.emit(self.id, True, idx + 1, total)
        
            

