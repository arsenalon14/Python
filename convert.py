def far(x):
    return (x*(5/9)+32)
def cel(x):
    return ((x-32)*5/9)

print("Hi do you like to convert for celsius to fahrenheit or fahrenheit to celsius")
print("Type 1 for Celsius to fahrenheit")
print("Type 2 for fahrenheit ot celsius")


while True:
    answer = input()
    if answer in ("1"):
        num1 = float(input("Please insert number in Celsius: "))
        result1 = far(num1)
        print(f"From {num1} Celsius is {result1:.2f} Fahrenheit")
    elif answer in ("2"):
        num2 = float(input("Please insert number in Fahrenheit: "))
        result2 = cel(num2)
        print(f"From {num2} Fahrenheit is {result2:.2f} Celsius")
    else:
        print("Wrong number")
    break



