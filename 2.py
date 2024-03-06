import requests  # импорт библиотеки для отправки http-запросов
from bs4 import BeautifulSoup  # импорт библиотеки для очистки содержимого от html разметки
import json  # для работы с JSON-данными

url = "https://hr-link.ru/blog/statya/aihelper"  # адрес сайта с которого будет браться текст

# Получение содержимое страницы
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Очищение от HTML-разметки
text = soup.get_text().replace('\n', ' ')
# Сохранение результата в файл
data = {
    "url": url,
    "text": text
}
with open('aihelper.json', 'w', encoding='utf-8') as f:  # открывает фаил в режиме записи
    json.dump(data, f, ensure_ascii=False,  # записывает данные из 'data' в файл
              indent=4)  # 'indent=4' означает что каждый уровень вложенности будет сдвинут на 4 пробела
