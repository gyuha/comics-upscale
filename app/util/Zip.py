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
from constant.SettingEnum import SettingEnum


class ZipSignal(QObject):
    zip_state = Signal(str, bool, int, int)


class Zip(QThread):
    signals = ZipSignal()

    def __init__(self, parent, id: str, file_path: str):
        QThread.__init__(self, parent)
        self._parent = parent

        self.id = id

        self.config = Config()
        self.src_path = Path(self.config.data["temp_dir"]).absolute()

        self.target_dir = self.config.replace_name(file_path)

    def run(self):
        self.zip_thread = threading.Thread(target=self._zip_files)
        self.zip_thread.start()
        self.signals.zip_state.emit(self.id, False, 0, 1)

    def _zip_files(self):
        zipf = zipfile.ZipFile(self.target_dir, "w", zipfile.ZIP_DEFLATED)
        source = os.listdir(self.src_path)
        total = len(source)
        for idx, f in enumerate(source):
            self.signals.zip_state.emit(self.id, False, idx + 1, total)
            zipf.write(os.path.join(self.src_path, f), os.path.basename(f))
        zipf.close()
        self.signals.zip_state.emit(self.id, True, total, total)
