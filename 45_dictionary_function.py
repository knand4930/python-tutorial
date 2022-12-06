"""
Dictionary Function

1. get() : get the data from key
2. keys() : get the all keys data
3. values() : get the all values data
3. items() :  get the all data
4. del()   : delete the value form the keys
5. pop() : delete the value from the keys with print which value are printed
6. dict() : create new dictionary
7. update() : update the value
8. copy() : create duplicate dictionary
"""


dic = {
    "name":"Nand Kishore",
    "email":"knand4930@gmail.com",
    "dob" :"15/12/1999",
    "profession":  "Computer Science"
}


#
# g = dic.get("name")
# print(dic["name"])
# print(g)
#
# for i in dic.keys():
#     print(i)
#
# for j in dic.values():
#     print(j)
#
# for k, l in dic.items():
#     print(k, l)
#
# del dic["name"]
# print(dic)
#
# print(dic.pop("email"))
# print(dic)
#
# d = dict(name="python", fee="8000")
# print(d)

# dic.update({"name":"Kishore"})
# print(dic)

# dic.clear()
# print(dic)

# dic.copy()
# print(dic)

# dic["course"] = "python courses"
# print(dic)

dic['name'] = "raj kishore"
print(dic)