def employee(name_hour):
    max1 = 0
    employee = ''
    for name,hour in name_hour:
        if hour > max1:
            max1 = hour
            employee = name
        else:
            pass
    return(employee,max1)

def inputdata():
    list1 = list()
    while len(list1) <= 4:
        name = str(input("Enter your name: "))
        hour = float(input("Enter hour of working: "))
        list1.append([name,hour])
    return (list1)

print("Program for check employee of the month")
print("By checking there work hour.")

x = inputdata()

y = employee(x)

print(f"employee of the month is {y[0]} working {y[1]} hours.")





