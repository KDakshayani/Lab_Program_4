a= float(input("Enter the first number: "))
b= float(input("Enter the second number: "))


add = a + b
sub= a - b
mul=a*b

print(f"The sum of {a} and {b} is: {add}")
print(f"The difference between {a} and {b} is: {sub}")
print(f"The product of {a} and {b} is: {mul}")

if b!=0:
    div=a/b
    print(f"The quotient of {a} and {b} is: {div}")
else:
    print("Can't divided by zero")