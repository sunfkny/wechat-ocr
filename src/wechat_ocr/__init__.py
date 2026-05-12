import sys
import typing


class OCRItem(typing.TypedDict):
    text: str
    left: float
    top: float
    right: float
    bottom: float
    rate: float


class OCRResult(typing.TypedDict):
    imgpath: str
    errcode: int
    width: int
    height: int
    ocr_response: list[OCRItem]


if sys.platform == "linux":
    from .linux import ocr
elif sys.platform == "win32":
    from .windows import ocr
else:
    raise RuntimeError(f"Unsupported platform: {sys.platform}")

__all__ = ["ocr"]
