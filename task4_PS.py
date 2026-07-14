# HR and payroll System

def main_hr_app() :
    print('=' * 80)
    print('Welcome to HR and payroll System!'.center(80))
    print('=' * 80)
    employee_name = input('Enter your name :\n').capitalize().strip()
    department = input('Enter your Department :\n').capitalize().strip()
    performance_rating = int(input('Enter your Performance Rating :\n'))
    base_salary = float(input('Enter your Base Salary :\n'))
    if base_salary < 0 or performance_rating > 5 or performance_rating < 1:
        print('Invalid data entered. Please restart and check your inputs.')
        return

    bonus = calculate_bonus(base_salary, performance_rating)
    gross_salary = base_salary + bonus
    tax = calculate_tax(gross_salary)
    net_salary = gross_salary - tax
    
    return (f'--- Payroll Summary for {employee_name} ({department} Dept) ---\n'
            f'Base Salary: {base_salary:,.2f} EGP\n'
            f'Bonus: {bonus:,.2f} EGP\n'
            f'Gross Salary: {gross_salary:,.2f} EGP\n'
            f'Tax Deductions: {tax:,.2f} EGP\n'
            f'-----------------------------------------\n'
            f'Net-Salary is : {net_salary:,.2f} EGP')


def calculate_bonus(base_salary, rating) :
    if rating == 5 :
        bonus = base_salary * 0.2
    elif 5 > rating >= 3 :
        bonus = base_salary * 0.1
    elif 3 > rating >= 1 :
        bonus = 0
    else :
        bonus = 0
        print('The rating is Invalid, Try again.')
        
    return bonus

def calculate_tax(gross_salary) :
    if gross_salary > 7000 :
        tax = gross_salary * 0.15
    elif 7000 >= gross_salary >= 3000 :
        tax = gross_salary * 0.1
    elif 3000 > gross_salary >= 1 :
        tax = 0
    else :
        tax = 0
        print('The gross salary is Invalid, Try again.')
    
    return tax


print(main_hr_app())