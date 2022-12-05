"""
Logical operators
#show the result in boolean value

Operator	    Description	                                                    Example
and 	        Returns True if both statements are true	                    x < 5 and  x < 10
or	            Returns True if one of the statements is true	                x < 5 or x < 4
not	            Reverse the result, returns False if the result is true	        not(x < 5 and x < 10)



"""

x = 5
y = 10

print(x < 5 and y < 10)
print(x == 5 and y == 10)
print(x < 5 or y == 10)
print(not (x == 5 and y == 10))
print(not (x == 5 or y != 10))
print(not (x == 5 and y > 10))
