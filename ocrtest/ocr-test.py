import os
from PIL import Image
import pytesseract

#tessdata_dir_config = '--tessdata-dir "H:\\Tesseract-OCR\\tessdata\\"'
dir='E:\\pythonWork\\pythonWork\\1'
files=os.listdir(dir)
texts=[]
for file in files:
	file=os.path.join(dir,file)
	image=Image.open(file)
	text=pytesseract.image_to_string(image,lang='chi_tra')
	texts.append(text)

src_file=os.path.join(dir,'src.txt')
with open(src_file,'w') as f:

	for text in texts:
		f.write(text)
#image=Image.open('E:\\pythonWork\\pythonWork\\00000.jpg')
##print(text)