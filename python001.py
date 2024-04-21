## Find Sum of Numbers Entered by User (deactivated by ## symbols)

#number1 = int(input("Enter first number "))
#number2 = int(input("Enter second number: "))

#print("The sum of {} and {} is: {}".format(number1, number2, number1 + number2))


## Entering the condition  (active)
count = int(input("Enter count of numbers : "))

sum = 0
for num in range(count):
    number = int(input())
    sum = sum + number 

print("The sum of all numbers is : ", sum)
