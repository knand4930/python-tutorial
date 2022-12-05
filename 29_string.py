"""
#String

1. string indexing and slicing
2. A string is a sequence of characters
3. String can be created by enclosing characters inside a single quote or double-quotes
4. triple quotes can be used represent multiline strings
"""

a = "hello world"

s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)

print(a[4])
print(a[-1])

# start value and the last one is last value of string
print(a[0:5])

# start value to end the value of blank the second.
print(a[0:])

# reverse slicing
print(len(a))
print(a[-1::-1])
print(a[-1:-12:-2])
