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
y = typ.capitalize()

for item in data:
    for m in item["type"]:
        if m == y:
            print(item["name"][x])

search = input("Search for a pokemon:  ")
for pokemon in data:
    count = 0
    s = 0
    for char in pokemon["name"]:
        if char == search[count]:
            count += 1
            s += 1
    if s > len(search):
        print(pokemon["name"][x])