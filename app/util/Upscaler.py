from enum import Enum
from functools import partial
import os
from signal import signal
import sys
from argparse import ONE_OR_MORE
from typing import List

import PySide6.QtCore
from PySide6.QtCore import QObject, QProcess, QThread, Signal, Slot
from PySide6.QtWidgets import (QApplication, QMainWindow, QProgressBar,
                               QPushButton, QVBoxLayout, QWidget)
from constant.SettingEnum import SettingEnum
from util.Config import Config

class UpscaleType(Enum):
    IMAGE = 1
    COMPRESS_IMAGE = 2

class UpscalerSignal(QObject):
    upscale_state = Signal(str, bool, int, int)  # run, current, total

class Upscaler(QObject):
    signals = UpscalerSignal()

    def __init__(self, parent, id: str):
        self._parent = parent
        self.id = id
        self.p = None
        self.total = 0
        self.path = ""
        self.currentIndex = 0
        self.file_list = []
        self.config = Config()
        self._set_upscale_option()
    
    def _set_upscale_option(self):
        self._options = [ 
            "-f",
            self.config.setting[SettingEnum.FORMAT],
            "-t",
            self.config.setting[SettingEnum.TILE_SIZE].split(" ")[0],
            "-n",
            self.config.setting[SettingEnum.MODEL_NAME],
            "-s",
            str(self.config.setting[SettingEnum.UPSCALE_RATIO]),
        ]
        if self.config.setting[SettingEnum.TTA_MODE]:
            self._options.append("-x")
    
    def set(self, type: UpscaleType, files: List[str], target_path = None):
        self.upscaleType = type
        self.target_path = target_path
        self.total = len(files)
        if self.total == 0:
            return
        self.file_list = files

        self.currentIndex = 0

    def start(self):
        self.on_process_next()

    def output_filepath(self, path: str) -> str:
        return path.replace(".jpg", "-S.jpg")

    def _progress(self):
        self.p = QProcess()
        self.p.finished.connect(self.on_process_next)
        self.p.readyReadStandardOutput.connect(partial(self.onReadyReadStandardOutput))
        # self.p.readyReadStandardError.connect(self.on_state_error)

        current_file = self.file_list[self.currentIndex]
        target_file = current_file

        if self.upscaleType == UpscaleType.IMAGE:
            target_file = self.target_path

        options = ["-i", current_file, "-o", target_file] + self._options
        self.p.start("./bin/realesrgan-ncnn-vulkan", options)
    
    def onReadyReadStandardOutput(self):
        raw_bytes = self.p.readAllStandardOutput()
        text = self._decoder_stdout.toUnicode(raw_bytes)

    def on_process_next(self):
        if self.currentIndex >= self.total:
            self.signals.upscale_state.emit(
                self.id, True, self.currentIndex, self.total)
            return
        self.signals.upscale_state.emit(self.id, False, self.currentIndex, self.total)
        self.p = None
        self._progress()

        self.currentIndex += 1
    



class ProgressWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.p = None  # Default empty value.

        self.btn = QPushButton("Execute")
        self.btn.pressed.connect(self.start_process)

        self.pbar = QProgressBar(self)

        self.upscaler = Upscaler(self)
        self.upscaler.signals.upscale_state.connect(self.on_progress)

        l = QVBoxLayout()
        l.addWidget(self.btn)
        l.addWidget(self.pbar)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)

    @Slot(bool, int, int)
    def on_progress(self, complete: bool, current: int, total: int):
        progress = 0
        if current != 0:
            progress = (current / total) * 100
        self.pbar.setValue(progress)
        self.btn.setEnabled(complete)

    def start_process(self):
        self.btn.setEnabled(False)
        self.upscaler.start("./wfwf/up")

    def process_finished(self):
        self.message("Process finished.")
        self.p = None


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = ProgressWindow()
    w.show()

    app.exec_()
