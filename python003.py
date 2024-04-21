#Swap Two Variables in Python

#1-using temporary variable
x = 10
y = 20

print("the values of x and y are {}, {} before swapping".format(x,y))

temp = x
x = y = temp
print("the values of x and y are {} {} after swapping".format(x,y))

## 2 without using a temporary variable

#x = 10
#y = 20

#print("the values of x and y are {}, {} before swapping".format(x,y))

#x, y = y, x
#print("the values of x and y are {} {} after swapping".format(x,y))
