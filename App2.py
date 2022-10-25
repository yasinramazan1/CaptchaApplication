import time # Saatle ilgili işlemler yapabilmek için gerekli olan Python modülünün import edilmesi
from selenium import webdriver # Tarayıcıyı çalıştırmak için gerekli olan Selenium kütüphanesinden webdriver modülünün import edilmesi
from selenium.webdriver.common.by import By # Arama işleminin türü için gerekli olan modülün import edilmesi
from selenium.webdriver.common.keys import Keys # Klavyeden girdi yapılabilmesi için gerekli modülün import edilmesi

import pytesseract # pytesseract kütüphanesinin import edilmesi
from PIL import Image # Pillow kütüphanesinden Image modülünün import edilmesi

browser = webdriver.Chrome("C:/Users/Yasin Ramazan GÖK/Desktop/chromedriver.exe") # chromedriver'ın çalışması için bulunduğu konumu tanımlıyoruz.
browser.get("http://disrandevu.ksbu.edu.tr:8081/") # Tarayıcıda verilen linke direkt erişiyoruz.
browser.maximize_window() # Tarayıcıyı tam ekran yapma
time.sleep(2) # Bekletme
captchaPhoto = browser.find_element(By.XPATH,"/html/body/form/div[4]/div/div[4]/div[1]/div/div[2]/div[4]/div/img") # İlgili elementi xpath yolu ile bulma
captchaPhoto.screenshot("D:/CaptchaApplication/captchaScreenshot.png") # İlgili elementin ekran görüntüsünü alma ve kaydetme
time.sleep(2)
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe" # Tesseract OCR'nin çalıştırılabilmesi için path'ini tanımlıyoruz.
text = pytesseract.image_to_string(Image.open("captchaScreenshot.png"), lang="tur") # Tesseract'a gönderilen fotoğraftan yazıyı okuma
time.sleep(2)
tcNo = browser.find_element(By.XPATH,"/html/body/form/div[4]/div/div[4]/div[1]/div/div[2]/div[1]/div/input")
tcNo.send_keys("12345678901") # textbox'a veri girişi 
time.sleep(2)
telefonNo = browser.find_element(By.XPATH,"/html/body/form/div[4]/div/div[4]/div[1]/div/div[2]/div[3]/div/input")
telefonNo.send_keys("1111111111")
time.sleep(2)
captchaText = browser.find_element(By.XPATH,"/html/body/form/div[4]/div/div[4]/div[1]/div/div[2]/div[4]/div/input")
captchaText.send_keys(text) 
time.sleep(2)
loginButton = browser.find_element(By.XPATH,"/html/body/form/div[4]/div/div[4]/div[1]/div/div[3]/a")
loginButton.click() # Butona işlev kazandırma 
time.sleep(20)
quit()

