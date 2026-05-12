import wechat_ocr

imgpath = input("imgpath: ")
result = wechat_ocr.ocr(imgpath)
print(result)
