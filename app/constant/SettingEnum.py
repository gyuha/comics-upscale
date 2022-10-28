from enum import Enum


class SettingEnum(str, Enum):
    SCALE = "scale"
    TITLE_SIZE = "title_size"
    MODEL_NAME = "model_name"
    TTA_MODE = "tta_mode"
    FORMAT = "format"
    JPG_OPTIMIZE = "jpg_optimize"
