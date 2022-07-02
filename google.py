import undetected_chromedriver.v2 as uc
from selenium import webdriver
from scrapy.selector import Selector
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from time import sleep
import csv

driver=uc.Chrome()
url='https://www.google.com/search?rlz=1C1ALOY_esCO955CO955&tbs=lf:1,lf_ui:3&tbm=lcl&sxsrf=APq-WButwR3jxVjXcXbxO_yPlV8UvVQrPA:1648773276157&q=san+jose+california+moving&rflfq=1&num=10&sa=X&ved=2ahUKEwip3MKLz_H2AhVBTTABHb9TBAIQjGp6BAgLEAE&biw=1920&bih=937&dpr=1#rlfi=hd:;si:12594107279166168139,l,ChpzYW4gam9zZSBjYWxpZm9ybmlhIG1vdmluZ0jkkP7qlZaAgAhaJhADGAAYARgCGAMiGnNhbiBqb3NlIGNhbGlmb3JuaWEgbW92aW5nkgEObW92aW5nX2NvbXBhbnmqAQ4QASoKIgZtb3ZpbmcoAA;mv:[[37.4017808,-121.81837279999999],[37.2448416,-121.98114319999998]]'
driver.get(url)
sleep(2)
try:
    iAgree=driver.find_element(By.XPATH,"(//div[@class='QS5gu sy4vM'])[2]")
    if iAgree:
        iAgree.click()
except:
    pass
html = driver.page_source
response = Selector(text=html)
companies=driver.find_elements(By.XPATH,"//div[@jsname='GZq3Ke']")


sleep(2)
