
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
text = pytesseract.image_to_string(Image.open("C:/Users/Yasin Ramazan GÖK/Desktop/Adsız.jpg"))
# text = pytesseract.image_to_string(Image.open("C:/Users/Yasin Ramazan GÖK/Desktop/Adsız.jpg"), lang="tur")
print(text)