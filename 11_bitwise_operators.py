"""
Bitwise Operators

#bin predifine to show the binanry number

Operator	Name	Description
& 	        AND	    Sets each bit to 1 if both bits are 1
|	        OR	    Sets each bit to 1 if one of two bits is 1
^	        XOR	    Sets each bit to 1 if only one of two bits is 1
~	        NOT	    Inverts all the bits
<<	        Zero    fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	        Signed  right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


"""

x = 10
y = 10
print(bin(x))
print(bin(y))

print("AND", x & y, bin(x & y))
print("OR", x | y, bin(x | y))
print("XOR", x ^ y, bin(x ^ y))
print("NOT", ~x)
print("NOT", ~y)
print("Zero", x << y, bin(x << y))
print("Signed", x >> y, bin(x >> y))
