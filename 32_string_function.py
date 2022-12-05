"""
1. find() : find the value of any string
2. index() : return the value of index number
3. isalpha() : return value true or false  if string in any number show the false and only for string value show the true
4. isdigit() : return value true or false if string in only number show the true and only for string value show the false
5. isalnum() : return value true or false if string in any number with only string show the true another case show the value of false
6. if value is not available on string to find show the -1 value and index are show the error

"""

a = "hello world"
b = a.find("o")
c = a.index('d')

print(b)
print(c)

print(a.isalpha())
print(a.isdigit())
print(a.isalnum())


i = "hello123"
print(i.isalpha())
print(i.isdigit())
print(i.isalnum())



j = "123"
print(j.isalpha())
print(j.isdigit())
print(j.isalnum())




