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
from app.constant.SettingEnum import SettingEnum

import pyguetzli


class ImageOptimizeSignal(QObject):
    optimize_state = Signal(str, bool, int, int)


class ImageOptimize(QThread):
    signals = ImageOptimizeSignal()

    def __init__(self, parent):
        QThread.__init__(self, parent)
        self._parent = parent

        self.config = Config()
        self.value = int(self.config.setting[SettingEnum.JPG_OPTIMIZE].split(" ")[0])
        self.target_dir = Path(self.config.data["temp_dir"]).absolute()
        self.re_image = re.compile("\.(jpg|JPG)$")

    def run(self):
        if self.value == 100:
            self.signals.optimize_state.emit(self.id, True, 1, 1)
            return
        unzip_thread = threading.Thread(target=self._optimize_precess)
        unzip_thread.start()
        self.signals.optimize_state.emit(self.id, False, 0, 1)
    
    def _image_optimize(self, path):
        with open(path, "rb") as f:
            input_jpg = f.read()
        optimized_jpg = pyguetzli.process_jpeg_bytes(input_jpg, quality=self.value)
        with open(path, "wb") as output:
            output.write(optimized_jpg)
    
    def _optimize_precess(self):

        source = os.listdir(self.target_dir)
        total = len(source)
        for idx, file in enumerate(source):
            self.signals.optimize_state.emit(self.id, False, idx + 1, total)
            if self.re_image(file) != None:
                continue
            self._image_optimize(os.path.join(self.target_dir, file))

        self.signals.optimize_state.emit(self.id, True, idx + 1, total)
        
            

