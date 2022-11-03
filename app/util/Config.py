from functools import reduce
import os
import yaml
import re

from lib.Singleton import Singleton
from constant.SettingEnum import SettingEnum


class Config(metaclass=Singleton):
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def setting(self):
        return self.__data["setting"]

    def __init__(self):
        super(Config, self).__init__()
        self.read_data()

    def read_data(self):
        with open("config.yaml", "r", encoding="utf-8") as file:
            self.__data = yaml.load(file, Loader=yaml.FullLoader)

    def save(self):
        with open("config.yaml", "w", encoding="utf-8") as file:
            yaml.dump(self.__data, file, default_flow_style=False, allow_unicode=True)

    def re_allow_extension(self):
        return re.compile(
            "\.("
            + reduce(lambda x, y: x + "|" + y, self.data["allow_file"])
            + "|"
            + reduce(lambda x, y: x + "|" + y, self.data["allow_image"])
            + ")$"
        )

    def re_image_extension(self):
        return re.compile(
            "\.(" + reduce(lambda x, y: x + "|" + y, self.data["allow_image"]) + ")$"
        )

    def re_zip_extension(self):
        return re.compile(
            "\.(" + reduce(lambda x, y: x + "|" + y, self.data["allow_file"]) + ")$"
        )
    
    def replace_name(self, file_path: str):
        if self.setting[SettingEnum.REPLACE_ORIGIN]:
            return file_path
        base_name = os.path.basename(file_path)
        t = base_name.split(".")
        if len(t) <= 1:
            return file_path
        t[-2] = t[-2] + self.setting[SettingEnum.POST_FIX]
        base_name = ".".join(t)
        return os.path.join(os.path.dirname(file_path), base_name)
