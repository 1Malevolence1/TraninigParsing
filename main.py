from bs4 import BeautifulSoup
import requests
import json

url = "https://namedb.ru/search-by-letter/"

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"

}

# req = requests.get(url, headers=headers)
# src = req.text

# with open("index.html","w",encoding="utf-8") as file:
#     file.write(src)

with  open("index.html",encoding="utf-8") as file:
    src = file.read()


soup = BeautifulSoup(src,"lxml")


name_reading = soup.find_all(class_="name-item s-male")
dict_finish = {}

all_table_name = {}
alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
count = 0
for letter in alphabet:
    all_table_name[count] = letter
    count += 1

for key in all_table_name:
    name_list = []
    for item_name in name_reading:

        name_info = item_name.text[:-1]

        if name_info[0] == all_table_name[key]:
            name_list.append(name_info)
    dict_finish[all_table_name[key]] = name_list

print(all_table_name)
print(dict_finish)


with open("table_name.json","w",encoding="utf-8") as file:
    json.dump(dict_finish,file,indent=4,ensure_ascii=False)





