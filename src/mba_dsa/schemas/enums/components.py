from enum import StrEnum


class DateTimeTypeOptions(StrEnum):
    TIMESTAMP = "timestamp"
    DATETIME = "datetime"
    STRING = "string"


class ImageButtonsType(StrEnum):
    DOWNLOAD = "download"
    SHARE = "share"
    FULLSCREEN = "fullscreen"
