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

""" lang = input("Choose a language: English, Japanese, Chinese, French ")
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
            print(item["name"][x]) """

""" e = input("Search for a pokemon:  ")
search = e.capitalize()
length = int(len(search)) - 1
for item in data:
    count = 0
    for char in item["name"][x]:
        if count == length:
            print(item["name"][x])
        elif char == search[count]:
            count += 1 """
""" 
e = input("Search for a pokemon:  ")
search = e.capitalize()
length = int(len(search)) - 1
for item in data:
    count = 0
    for char in item["name"][x]:
        if char == search[count]:
            count += 1
            print(count)
            if count == length:
                print(item["name"][x]) """

""" e = input("Search for a pokemon:  ")
search = e.capitalize()
length = int(len(search)) - 1
for item in data:
    count = 0
    wrong = 0
    for char in item["name"][x]:
        if char == search[count]:
            count += 1
            if count == length:
                print(item["name"][x])
                count = 0
        else:
            wrong += 1
            if wrong >= 1:
                count = 0 """

                
""" e = input("Search for a pokemon:  ")
search = e.capitalize()
length = int(len(search)) - 1
for item in data:
    count = 0
    for char in item["name"][x]:
        while count <= length:
            if char == search[count]:
                count += 1
        print(item["name"][x])
        count = 0 """


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

e = input("Search for a pokemon:  ")
search = e.capitalize()
length = int(len(search))
found = 0
for item in data:
    count = 0
    wrong = 0
    for char in item["name"][x]:
        if char == search[count]:
            count += 1
            if count == length:
                print(item["name"][x])
                count = 0
                found += 1
        else:
            wrong += 1
            if wrong >= 1:
                count = 0
if found == 0:
    print("No pokemon was found. ")
