import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
types = open("./types.json", encoding="utf8")
t_data = json.load(types)
t_datas = []

lang = input("Choose a language: English, Japanese, Chinese, French ")
x = lang.lower()
for item in data:
    print(item["name"][x])

for item in t_data:
    t_datas.append(item[x])
typ = input(f"Select a type: {t_datas} ")
y = typ.lower()
for item in data:
    if item["type"] == y:
        print(item["name"][x])

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
    if item["type"] == y:
        z.append(item["type"])
for i in z:
    print(i) """