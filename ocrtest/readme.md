# pdf混淆加密文件识别提取

采用方案为ocr识别，先将pdf转换为图片，对图片进行ocr识别，然后将识别出的文字写入xml文件。具体分为以下三个步骤：

* pdf按页转成图片
* ocr识别图片中的文字
* 将识别文字写入xml

## pdf转图片

pdf转图片所依赖的内容较多，需要一一进行下载，python相关的库可使用pip下载，其他外部调用程序则需手动下载进行安装，同时配置相关的环境变量。具体如下：

1. pip
   * pip install wand
   * pip install PyPDF2
2. 手动下载
   * ImageMagick
   * ghostscript
3. 注意事项
   * 在下载imageMagick时，必须保证下载的包在安装时有c++或c库可选，否则没安装c或c++库，python调用会失败
   * ghostscript则只需简单加入到环境变量让python程序能找到即可

## ocr 图片识别

* install tessecret
* pip install wand
* pip install pytesseract

### 注意事项

在实际运行过程中，可能会出现找不到tesseract.exe这个执行文件，也可能会出现找不到chi_sim.traineddata这个数据文件。遇到这些问题时，只要通过环境变量的形式指明这些文件的路径即可。

* 安装好tesseract后，需修改pytesseract.py文件，将tesseract_cmd='tesseract'设置为绝对路径，或将tesseract.exe所在目录加入到环境变量。

* 同时将tessdata目录的上级目录所在路径：(默认为tesseract-ocr安装目录)添加至TESSDATA_PREFIX环境变量中。
* 若出现找不到语料文件，即找不到chi_sim.traineddata文件，需将该文件移动到TESSDATA_PREFIX所指目录下。

# 