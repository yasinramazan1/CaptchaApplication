import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def siteyiAc():
    tarayici = webdriver.Chrome("C:/Users/Yasin Ramazan GÖK/Desktop/chromedriver.exe")
    tarayici.get("https://www.google.com.tr/?hl=tr")
    tarayici.maximize_window()
    time.sleep(2)
    obsGirisSayfasi = tarayici.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    obsGirisSayfasi.send_keys("Karadeniz Teknik Üniversitesi"+Keys.ENTER)
    time.sleep(1)
    obsGirisSayfasi = tarayici.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a/h3")
    obsGirisSayfasi.click()
    time.sleep(1)
    obsGirisSayfasi = tarayici.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[2]/a")
    obsGirisSayfasi.click()
    time.sleep(1)
    obsGirisSayfasi = tarayici.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div/div[1]/button[2]/div")
    obsGirisSayfasi.click()
    time.sleep(1)
    obsGirisSayfasi = tarayici.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/ul/li[1]/a")
    obsGirisSayfasi.click()
    time.sleep(1)
    photo = tarayici.find_element(By.XPATH,"/html/body/form/div[5]/div[3]/div[1]/table/tbody/tr[3]/td[2]/div/div/div/img")
    photo.screenshot("D:/yasinramazan/ChaptchaApplication/chaptchaScreenshot.png")
    time.sleep(2)

    