#project day 3
name_employee = input("The employee's name is: ").strip().title()

hourly_wage = float(input("Hourly wage is: "))
hours_worked = float(input("How many hours the employee worked: "))
employee_total_earnings = hourly_wage * hours_worked

# Regina George earned $800 this week.
print(f'{name_employee} earned ${employee_total_earnings} this week')
