from PIL import Image
import pytesseract

#tessdata_dir_config = '--tessdata-dir "H:\\Tesseract-OCR\\tessdata\\"'
image=Image.open('E:\\pythonWork\\pythonWork\\ocrtest\\ocrtest.jpg')
text=pytesseract.image_to_string(image,lang='chi_sim')
print(text)