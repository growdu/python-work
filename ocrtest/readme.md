# ocr cognize pdf

* install tessecret
* pip install wand
* pip install pytesseract

# 注意事项

安装好tesseract后，需修改pytesseract.py文件，将tesseract_cmd='tesseract'设置为绝对路径，或将tesseract.exe所在目录加入到环境变量。

同时将tessdata目录的上级目录所在路径：(默认为tesseract-ocr安装目录)添加至TESSDATA_PREFIX环境变量中。