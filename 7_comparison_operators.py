"""
Comparison Operators
#show the answer only for boolean value



Operator	        Name	                    Example	Try it
==	                Equal	                     x == y
!=	                Not equal	                 x != y
>	                Greater than	             x > y
<	                Less than	                 x < y
>=	                Greater than or equal to	 x >= y
<=	                Less than or equal to	     x <= y


"""
import time

x = 20
y = 10

start = time.time()
print("Equal:- ", x == y)
print("Not Equal:- ", x != y)
print("Greater than:- ", x > y)
print("Less than:- ", x < y)
print("Greater than or equal to:- ", x >= y)
print("Less than or equal to:- ", x <= y)

end = time.time()

print(end - start)
