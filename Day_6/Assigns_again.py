## -1
#from Day_6.Assigns import number_of_employees

employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
#for employee in employees:
#    total_week = employee[1]*employee[2]
#    print(f"So tien nhan vien duoc tra la: ${total_week}")

## -2
#Input: da co da buoc tren bai 1
#Output: print out those who are earning an hourly wage above average.
# Can tim: luong trung binh cua 4 nhan vien (1 + 2+ 3 + 4)/4
# B1:
Total_wage = number_of_employees = 0
for employee in employees:
    wage = employee[2]
    Total_wage = Total_wage+ wage
    number_of_employees= number_of_employees+1
    average = Total_wage/number_of_employees
for emp in employees:
    if emp[2]>average:
        print(emp[0])