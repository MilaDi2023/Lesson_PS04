# Код для вызова браузера, открытия сайта Википедии, вбивания в поисковую строку нужной информации (Солнечная система),
# вывода списка статей, содержащих эту инфу, а также переход на первую статью из этого списка

from selenium import webdriver
from selenium.webdriver import Keys # Импорт библиотеки для ввода с клавиатуры
from selenium.webdriver.common.by import By # Импорт библиотеки для поиска элементов на странице через DOM
import time

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
assert "Википедия" in browser.title # Проверяем, точно ли у страничка с вышеуказанной ссылкой заголовок Википедия
time.sleep(5)
search_box = browser.find_element(By.ID, "searchInput") # Ищем на странице элемент, у которого ID - searchInput
search_box.send_keys("Солнечная система") # Задаем в поисковой строке значение "Солнечная система"
search_box.send_keys(Keys.RETURN) # Отправляем наш запрос
# Откроется список всех статей Вики, где упоминается Солнечная система
time.sleep(5)
a = browser.find_element(By.LINK_TEXT, "Солнечная система") # Находится 1-й элемент списка, содержащий "Солнечная система"
a.click() # Делаем клик по этому элементу
time.sleep(5)
