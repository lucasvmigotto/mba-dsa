from enum import StrEnum


class ImageFormatType(StrEnum):
    JPEG = "jpeg"
    PNG = "png"
    WEBP = "webp"


class ImageModeType(StrEnum):
    MODE_1 = "1"
    MODE_L = "L"
    MODE_P = "P"
    MODE_RGB = "RGB"
    MODE_RGBA = "RGBA"
    MODE_CMYK = "CMYK"
    MODE_YCbCr = "YCbCr"
    MODE_LAB = "LAB"
    MODE_HSV = "HSV"
    MODE_I = "I"
    MODE_F = "F"
