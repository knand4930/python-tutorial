"""

1. String Iteration

"""

a = "Hello world"

#length of the string
l = len(a)
print(len(a))

for i in range(l):
    # print(i)
    print(i, "=>", a[i])


#second one option of reverse

for k in range(l-1, -1, -1):
    print(k, "=> ",a[k])



#use the reverse of string
rev = a[-1::-1]
ln = len(rev)

for j in range(ln):
    print(j, "=>", rev[j])


#third method for reverse string
for m in a[-1::-1]:
    print(m)
