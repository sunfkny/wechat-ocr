def test_ocr():
    import pathlib

    import wechat_ocr

    imgpath = pathlib.Path("cpp/doc/images/linux-spt.jpg").absolute()
    result = wechat_ocr.ocr(str(imgpath))
    print(result)
    assert isinstance(result, dict)
    assert "ocr_response" in result
    ocr_response = result["ocr_response"]
    assert isinstance(ocr_response, list)
    assert ocr_response
