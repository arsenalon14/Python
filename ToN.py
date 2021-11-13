def add(x,y):
  return x + y
def subtract(x,y):
  return x - y
def divide(x,y):
  return x/y
def multiply(x,y):
  return x*y

print("choos operation")
print("Press 1 for '+' ")
print("Press 2 for '-' ")
print("Press 3 for '/' ")
print("Press 4 for '*' ")

while True:
  chooe = input("Choose number to begin: ")
  if chooe in ("1","2","3","4"):

    num1 = float(input("enter first number "))
    num2 = float(input("enter second number "))
    if chooe == "1":
      result1 = add(num1, num2)
      print(result1)
    elif chooe == "2":
      result2 = subtract(num1 , num2)
      print(result2)
    elif chooe == "3":
      result3 = divide(num1,num2)
      print(result3)
    elif chooe == "4":
      result4 = multiply(num1,num2)
      print(result4)

    print("Thank You")
  break






