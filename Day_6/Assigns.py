employees = [
    #     0         1   2
    ("Rolf Smith", 35, 8.75),  # 0
    ("Anne Pun", 30, 12.50),  # 1
    ("Charlie Lee", 50, 15.50),  # 2
    ("Bob Smith", 20, 7.00)  # 3
]

#for employee in employees:
#    money_total = employee[1] * employee[2]
#    print(f"{employee[0]} earned ${money_total}")

total_wage = number_of_employees = 0

for employee in employees:
    wage = employee[2]
    total_wage = total_wage + wage
    number_of_employees = number_of_employees + 1

average = total_wage / number_of_employees

for emp in employees:
    if emp[2] > average:
        print(emp[0])
