from webdriver_manage.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from seleniu.webdriver.common.br import By

nv= webdriver.Chrome(service = Service(ChromeDriver().instal()))
link = ""
nv.get(link)

key.capt = nv.find_element(By.ID, "").get_attribute()
nv.find_element(By.ID, )
