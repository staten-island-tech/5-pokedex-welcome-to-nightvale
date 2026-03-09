import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
types = open("./types.json", encoding="utf8")
t_data = json.load(types)
t_datas = []
lang_list = ["english, japanese, chinese, french"]
""" lang = input("Choose a language: English, Japanese, Chinese, French ")
x = lang.lower()

while x not in lang_list:
    newlang = input("Language not found. Please enter a language from the list  ")
    x = newlang.lower()

for item in data:
    print(item["name"][x])

for item in t_data:
    t_datas.append(item[x])
typ = input(f"Select a type: {t_datas} ")
y = typ.lower()
for item in data:
    if item["type"] == y:
        print(item["name"][x]) """

""" lang = input("Choose a language: English, Japanese, Chinese, French ")
x = lang.lower()
for item in data:
    print(item["name"][x])

for item in t_data:
    t_datas.append(item[x])
typ = input(f"Select a type: {t_datas} ")
y = typ.lower()
z = []
for item in data:
    z.append
    print(item["name"][typ][y])
        
for i in z:
    print(i) """

lang = input("Choose a language: English, Japanese, Chinese, French ")
x = lang.lower()
for item in data:
    print(item["name"][x])

for item in t_data:
    t_datas.append(item[x])
typ = input(f"Select a type: {t_datas} ")
y = typ.lower()

for item in data:
    for it in item["type"]:
        if it == y:
            print(item["name"][x])