# Код для вызова статьи в Вики и выдачи инфы из этой статьи в консоли по одному параграфу, используя клавишу Enter

from selenium import webdriver
from selenium.webdriver import Keys # Импорт библиотеки для ввода с клавиатуры
from selenium.webdriver.common.by import By # Импорт библиотеки для поиска элементов на странице через DOM
import time

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

paragraphs = browser.find_elements(By.TAG_NAME, "p") # Ищем все элементы с тегом р, т.е. параграфы (они же абзацы статьи)

# Делаем так, чтобы следующий параграф появлялся в консоли после предыдущего по нажатию Enter
for paragraph in paragraphs:
    print(paragraph.text)
    input()