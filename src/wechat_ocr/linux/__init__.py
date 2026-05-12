import os
import pathlib

from wechat_ocr.lib import wcocr as _wcocr  # pyright: ignore[reportMissingModuleSource]

if os.getenv("WCOCR_USE_SYSTEM"):
    wechatocr_path = "/opt/wechat/wxocr"
    wechat_path = "/opt/wechat"
else:
    pwd = pathlib.Path(__file__).parent

    wechatocr_path = pwd / "wx/opt/wechat/wxocr"
    wechat_path = pwd / "wx/opt/wechat"

_wcocr.init(str(wechatocr_path), str(wechat_path))


def ocr(imgpath: str | pathlib.Path):
    imgpath = pathlib.Path(imgpath).absolute().as_posix()
    return _wcocr.ocr(imgpath)
