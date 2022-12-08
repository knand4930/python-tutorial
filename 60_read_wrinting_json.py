
import json
file = open('data_json.json', 'r')
finaldata = file.read()
print(finaldata, type(finaldata))
print("======================================")

pydata = json.loads(finaldata)
print(pydata, type(pydata))
print("======================================")
print(pydata["people"])
print("======================================")
data = pydata["people"]

for i in data:
    print(i)
    print("===========================")
    print(i['firstName'])
    print("===========================")
    print(i["lastName"])
    print("===========================")
    print(i["gender"])
    print("===========================")
    print(i["number"])
