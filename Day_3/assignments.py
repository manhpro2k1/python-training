## -1
print("Bai 1")
# Viết chương trình nhập vào họ tên và in ra màn hình.
# Input: Họ tên
# Output: Họ tên vừa nhập
firstname_and_lastname = input("Enter firstname and lastname: ")
print(firstname_and_lastname, "\n")

## -2
print("Bai 2")
# Viết chương trình nhập vào hai số nguyên và in ra tổng của chúng.
# Input: Hai số nguyên a, b
# Output: Tổng của a và b
a = input("Enter inter number a: ")
b = input("Enter inter number b: ")
print("Total of a and b is: ", int(a) + int(b), "\n")

## -3
print("Bai 3")
# Viết chương trình nhập vào chiều dài, chiều rộng của hình chữ nhật. Tính và in ra diện tích.
# Input: Chiều dài, chiều rộng
# Output: Diện tích hình chữ nhật
length = float(input("Rectangular length: "))
width = float(input("Rectangular width: "))
area = length * width
print(area, "\n")

## -4
print("Bai 4")
# Viết chương trình nhập vào bán kính hình tròn. Tính và in ra chu vi hình tròn.
# Input: Bán kính r
# Output: Chu vi hình tròn
radius_circle = float(input("Enter circle radius r: "))
perimeter = 2 * radius_circle * 3.14
print(perimeter,"\n")

##-5
print("Bai 5")
# Viết chương trình nhập vào điểm Toán, Văn, Anh. Tính và in ra điểm trung bình.
# Input: Điểm Toán, Văn, Anh
# Output: Điểm trung bình của 3 môn
math = float(input("Enter points maths: "))
literature = float(input("Enter points literature: "))
english = float(input("Enter points english: "))
average = (math + literature + english) / 3
print("Average of three subjects is: ", average,"\n")

##-6
print("Bai 6")
# Viết chương trình nhập vào số giờ làm và lương theo giờ. Tính và in ra tổng lương.
# Input: Số giờ làm, lương theo giờ
# Output: Tổng lương
hours_worked = float(input("Enter number hours_worked: "))
wage_per_hour = float(input("Enter wage per a hour: "))
total_wage = hours_worked * wage_per_hour
print(total_wage,"\n")

##-7
print("Bai 7")
# Viết chương trình nhập vào tên sản phẩm, số lượng và đơn giá. Tính và in ra tổng tiền.
# Input: Tên sản phẩm, số lượng, đơn giá
# Output: Tên sản phẩm và tổng tiền
product_name = input("Enter product name: ")
number_product = int(input("Enter number of product: "))
price = float(input("Enter price per a product: "))
total_price = number_product * price
print(product_name, "Total price is: ", total_price,"\n")

##-8
print("Bai 8")
# Viết chương trình nhập vào chiều cao (mét) và cân nặng (kg). Tính và in ra chỉ số BMI.
# Input: Chiều cao, cân nặng
# Output: Chỉ số BMI
height = float(input("Enter height: "))
weight = float(input("Enter weight: "))
BMI = height / pow(weight, 2)
print(BMI,"\n")

##-9
print("Bai 9")
# Viết chương trình nhập vào một số tiền USD. Tính và in ra số tiền VND tương ứng.
# Input: Số tiền USD
# Output: Số tiền VND (tỷ giá: 1 USD = 24,555 VND)
dollar = float(input("Enter dollar: "))
vnd = dollar * 24.555
print(vnd,"\n")

##-10
print("Bai 10")
# Viết chương trình nhập vào họ và tên riêng biệt, sau đó ghép lại và in ra họ tên đầy đủ.
# Input: Họ, tên
# Output: Họ tên đầy đủ
last = input("Enter last name: ")
first = input("Enter first name: ")
print(f"{last} {first}", end=".")
