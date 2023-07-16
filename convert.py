## update code to make it ask for number again if input wrong number.
## make convert program that convert from/to celsius to/from fahrenheit.

## Convert Fahrenheit to Celsius.
def far(x):
    return (x*(5/9)+32)

## Convert Celsius to Fahrenheit
def cel(x):
    return ((x-32)*5/9)

print("Hi do you like to convert for celsius to fahrenheit or fahrenheit to celsius")
print("Type 1 for Celsius to fahrenheit")
print("Type 2 for fahrenheit ot celsius")

answer =""
complete = False
while not complete:
## input only 1 or 2
    answer = input()
    if answer == "1":
        num1 = float(input("Please insert number in Celsius: "))
        result1 = far(num1)
        print(f"From {num1} Celsius is {result1:.2f} Fahrenheit")
        complete = True
    elif answer == "2":
        num2 = float(input("Please insert number in Fahrenheit: "))
        result2 = cel(num2)
        print(f"From {num2} Fahrenheit is {result2:.2f} Celsius")
        complete = True
    else: ## If input other number
        print("Wrong number\nPlease in put number again\nType 1 for Celsius to fahrenheit\nType 2 for fahrenheit ot celsius)
    continue
    
print("Exiting program")


