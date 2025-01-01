## -1
a = [1, 2]
b = [1, 2]
print((id(a)) == id(b))
a = [1, 2]
b = a
print((id(a)) == id(b))
print(a is b)

## 2
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
print(numbers is new_numbers)

numbers = [1, 2, 3, 4]
print(id(numbers))
numbers.append(5)
print(id(numbers))

## -3
user_number = float(input("Enter number: "))
if user_number > 0:
    print("so duong")
elif user_number < 0:
    print("so am")
else:
    print("So 0")

## -4
hours = float(input("So gio lam viec: "))
wage = float(input("Luong: "))

salary = hours * wage

if hours > 40:
    salary = 40 * hours + (hours - 40) * wage * 1.1

print(f"Nhan vien duoc ${salary}")
