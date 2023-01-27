import requests
import json
import random


class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.score = random.randint(0, 100)

# 自分お情報をcsvにするmethod

    def toCSV(self):
        return f'{self.name},{self.city},{self.score}'


# http通信してresponseオブジェクトを取得
URL = 'https://jsonplaceholder.typicode.com/users'
res = requests.get(URL)
# rex.text(本文:json)を取り出して、それをパースする
data = json.loads(res.text)
# debug print
# print(data)

# personリスト作成
persons = []
# dataを回す(dは１人分のdictionary)
for d in data:
    # personオブジェクト生成
    persons.append(Person(d['name'], d['address']['city']))
    # リストに追加
    # persons.append(person)

    # リストを点数降順で並び替え
persons.sort(key=lambda d: -d.score)

# print(persons[0].toCSV())

# ファイルはの書き込み
with open('result.csv', 'w', encoding='utf-8') as file:
    for p in persons:
        file.write(p.toCSV()+'\n')
