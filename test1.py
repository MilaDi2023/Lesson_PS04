# Код для вызова браузера, загрузки одной страницы, другой страницы и обновления страницы.
# Для каждой из страниц делается скриншот.

from selenium import webdriver
import time

browser = webdriver.Chrome() # Создаётся объект
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model") # Вызывается страница браузера
browser.save_screenshot("dom.png") # Делаем скриншот в файл dom.png
time.sleep(5) # Идёт задержка на странице 5 секунд

browser.get("https://ru.wikipedia.org/wiki/Selenium") # Вызывается другая страница браузера
browser.save_screenshot("selenium.png") # Делаем скриншот в файл selenium.png
time.sleep(3) # Идёт задержка на странице 3 секунды
browser.refresh() # Перезагрузка странички браузера
