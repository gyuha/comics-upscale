from enum import Enum


class SettingEnum(str, Enum):
    UPSCALE_RATIO = "upscale_ratio"
    TILE_SIZE = "tile_size"
    MODEL_NAME = "model_name"
    TTA_MODE = "tta_mode"
    FORMAT = "format"
    JPG_OPTIMIZE = "jpg_optimize"
    REPLACE_ORIGIN = "replace_origin"
    POST_FIX = "post_fix"
    PRE_FIX = "pre_fix"
