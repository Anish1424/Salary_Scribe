from employee.employee import Employee
from salary.salary import Salary
from salary.salary_details import SalaryDetails
from salary.salary_sheet import SalarySheet

def main():
    print("Choose Salary Type:")
    print("1. Monthly_Salary")
    print("2. Annual_Package")
    choice = input("Enter your choice (1 or 2): ")

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee name: ")
    designation = input("Enter employee designation: ")  
    try:
        if choice == '1':
            salary_type = "monthly"
            amount = float(input("Enter monthly basic salary: "))
        elif choice == '2':
            salary_type = "annual"
            amount = float(input("Enter annual package: "))
        else:
            print("Invalid choice. Please select 1 or 2.")
            return
    except ValueError:
        print("Invalid input. Salary must be a number.")
        return

    performance_rating = input("Enter performance rating (0-5): ")
    if performance_rating == "":
        print("Performance rating cannot be empty.")
        return
    try:
        performance_rating = float(performance_rating)
    except ValueError:
        print("Invalid input. Performance rating must be a number.")
        return

    if salary_type == "monthly":
        amount=amount
    else:
        amount=amount/12

    employee = Employee(emp_id, name, designation, amount)
    salary = Salary(salary_type,amount)  

    da = (10/100) * employee.basic_salary
    hra = (20/100) * employee.basic_salary
    ta = (5/100) * employee.basic_salary
    
    if performance_rating >= 3.5:
        bonus = (10/100) * employee.basic_salary  
    else: 
        bonus=(5/100) * employee.basic_salary


    if employee.basic_salary * 12 > 250000:
        tax_rate=(5/100)
    else:
        tax_rate=0

    salary_details = SalaryDetails(employee.basic_salary, da, hra, ta, bonus, tax_rate)

    salary_sheet = SalarySheet(employee, salary, salary_details)
    salary_sheet.display()

if __name__ == "__main__":
    main()
