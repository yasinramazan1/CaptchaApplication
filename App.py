import time # Saatle ilgili işlemler yapabilmek için gerekli olan Python modülünün import edilmesi
from selenium import webdriver # Tarayıcıyı çalıştırmak için gerekli olan Selenium kütüphanesinden webdriver modülünün import edilmesi
from selenium.webdriver.common.by import By # Arama işleminin türü için gerekli olan modülün import edilmesi
from selenium.webdriver.common.keys import Keys # Klavyeden girdi yapılabilmesi için gerekli modülün import edilmesi

import pytesseract # pytesseract kütüphanesinin import edilmesi
from PIL import Image # Pillow kütüphanesinden Image modülünün import edilmesi

browser = webdriver.Chrome("C:/Users/Yasin Ramazan GÖK/Desktop/chromedriver.exe") # chromedriver'ın çalışması için bulunduğu konumu tanımlıyoruz.
browser.get("https://www.google.com.tr/?hl=tr") # Tarayıcıda verilen linke direkt erişiyoruz.
browser.maximize_window() # Tarayıcıyı tam ekran yapma
time.sleep(2) # Bekletme
googleSearch = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input") # Web sayfasında xpath'e göre element bulma
googleSearch.send_keys("Karadeniz Teknik Üniversitesi"+Keys.ENTER) # Textbox'a klavyeden veri girişi 
time.sleep(1)
ktuMainPage = browser.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a/h3")
ktuMainPage.click()
time.sleep(1)
studentModule = browser.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[2]/a")
studentModule.click()
time.sleep(1)
eStudent = browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div/div[1]/button[2]/div")
eStudent.click()
time.sleep(1)
studentLoginScreen = browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/ul/li[1]/a")
studentLoginScreen.click()
time.sleep(1)
captchaPhoto = browser.find_element(By.XPATH,"/html/body/form/div[5]/div[3]/div[1]/table/tbody/tr[3]/td[2]/div/div/div/img")
captchaPhoto.screenshot("D:/CaptchaApplication/captchaScreenshot.png") # İlgili elementin ekran görüntüsünü alma ve kaydetme
time.sleep(2)
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe" # Tesseract OCR'nin çalıştırılabilmesi için path'ini tanımlıyoruz.
text = pytesseract.image_to_string(Image.open("captchaScreenshot.png"), lang="tur") # Tesseract'a gönderilen fotoğraftan yazıyı okuma
time.sleep(1)
captchaText = browser.find_element(By.XPATH,"/html/body/form/div[5]/div[3]/div[1]/table/tbody/tr[4]/td[2]/span/input[1]")
captchaText.send_keys(text) 
time.sleep(2)
userName = browser.find_element(By.XPATH,"/html/body/form/div[5]/div[3]/div[1]/table/tbody/tr[1]/td[2]/span/input[1]")
userName.send_keys("5. Week ISS Captcha Application")
time.sleep(1)
password = browser.find_element(By.XPATH,"/html/body/form/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/span[1]/input[1]")
password.send_keys("1234567890")
time.sleep(2)
loginButton = browser.find_element(By.XPATH,"/html/body/form/div[5]/div[3]/div[1]/table/tbody/tr[5]/td[2]/table/tbody/tr/td[2]/span")
loginButton.click() # Butona işlev kazandırma 
time.sleep(20)
quit()


