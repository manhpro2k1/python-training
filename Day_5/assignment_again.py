## -1
#from Day_3.project1 import hours_worked, hourly_wage

list_1 = [1, 2, 3, 4, 5]
list_2 = [1, 2, 3, 4, 5]
print(list_1 == list_2)
print(list_1 is list_2)
print(id(list_1)==id(list_2))
list_2 = list_1
print(list_1 == list_2)
print(list_1 is list_2)

## -2
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
print(id(numbers))
print(id(new_numbers))
print(numbers == new_numbers)

numbers = [1, 2, 3, 4]
print(id(numbers))
numbers.append(5)
print(id(numbers))
print(numbers is new_numbers)

## -3
numbers = float(input("Enter number: "))
if numbers>0:
    print(f"{numbers} is positive: ")
elif numbers<0:
    print(f"{numbers} is negative: ")
else:
    print(f"{numbers} is O")

## -4
hours_worked = float(input("Enter hour worked of employee: "))
hourly_wage = float(input("Enter hourly wage of employee: "))
if hours_worked>40:
   basic_wage = 40*hourly_wage
   additional = (hours_worked-40)*1.1*hourly_wage
   total = basic_wage+additional
   print(" So tien nhan duoc la: ", total,"VND")
else:
    print("So tien nhan duoc la: ", hourly_wage*hours_worked,"VND")

##
hours_worked = float(input("Enter hour worked of employee: "))
hourly_wage = float(input("Enter hourly wage of employee: "))
salary = hourly_wage*hourly_wage
if hours_worked>40:
    salary = (hourly_wage*40)+(hours_worked-40)*hourly_wage*1.1
print("So tien nhan duoc la: ",salary, "VND")
print(f"Nhan vien duoc ${salary}")
