import yaml
import re

from lib.Singleton import Singleton


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

