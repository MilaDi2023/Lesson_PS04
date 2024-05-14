# Код для составления списка разделов из статьи Вики и перехода от одного к другому в рандомном порядке

from selenium import webdriver
from selenium.webdriver import Keys # Импорт библиотеки для ввода с клавиатуры
from selenium.webdriver.common.by import By # Импорт библиотеки для поиска элементов на странице через DOM
import time
import random

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

hatnotes = [] # Создаем переменную под список всех разделов

for element in browser.find_elements(By.TAG_NAME, "div"): # Перебираем список получившихся элементов с тегом div
    cl = element.get_attribute("class") # Берем элемент с тегом div и ищем у него атрибут class
    if cl == "hatnote navigation-not-searchable": # Если у класса атрибут равен hatnote navigation-not-searchable, то
        hatnotes.append(element) # Добавляем этот элемент в список

print(hatnotes)
# Переход на рандомный раздел
hatnote = random.choice(hatnotes)
# Ищем внутри этого раздела ссылку на статью в Вики
link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
# Переходим по этой найденной ссылке
browser.get(link)
time.sleep(3)
