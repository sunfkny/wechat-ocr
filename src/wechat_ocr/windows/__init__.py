import os
import pathlib
import winreg

from wechat_ocr.lib import wcocr as _wcocr  # pyright: ignore[reportMissingModuleSource]

if os.getenv("WCOCR_USE_SYSTEM"):
    APPDATA = pathlib.Path(os.environ["APPDATA"])

    wechatocr_path = next(
        APPDATA.glob(
            "Tencent\\xwechat\\XPlugin\\Plugins\\WeChatOcr\\*\\extracted\\wxocr.dll"
        )
    )
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Tencent\\Weixin") as key:
        wechat_install_path = pathlib.Path(winreg.QueryValueEx(key, "InstallPath")[0])

    wechat_path = next(
        i
        for i in wechat_install_path.iterdir()
        if i.is_dir() and i.name.startswith("4.")
    )

else:
    pwd = pathlib.Path(__file__).parent

    wechatocr_path = pwd / "wx/Plugins/WeChatOcr/wxocr.dll"
    wechat_path = pwd / "wx/Weixin/4.1.9.35"

_wcocr.init(str(wechatocr_path), str(wechat_path))


def ocr(imgpath: str | pathlib.Path):
    imgpath = pathlib.Path(imgpath).absolute().as_posix()
    return _wcocr.ocr(imgpath)
