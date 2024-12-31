class SalarySheet:
    def __init__(self, employee, salary, salary_details):
        self.employee = employee
        self.salary = salary
        self.salary_details = salary_details

    def display(self):
        monthly_salary = self.salary.calculate_monthly_salary()
        annual_salary = self.salary.calculate_annual_salary()
        gross_pay = self.salary_details.calculate_gross_pay(self.salary)
        net_pay = self.salary_details.calculate_net_pay(self.salary)
        print("------------------------------------------------------")
        print(f"Salary Sheet for {self.employee.name} (ID: {self.employee.emp_id})")
        print("------------------------------------------------------")
        print(f"Designation: {self.employee.designation}")
        print(f"Basic Monthly Salary: ₹{monthly_salary:.2f}")
        print(f"Dearness Allowance (DA): ₹{self.salary_details.da:.2f}")
        print(f"House Rent Allowance (HRA): ₹{self.salary_details.hra:.2f}")
        print(f"Travel Allowance (TA): ₹{self.salary_details.ta:.2f}")
        print(f"Bonus: ₹{self.salary_details.bonus:.2f}")
        print(f"Gross Pay: ₹{gross_pay:.2f}")
        print(f"Tax Deduction ({self.salary_details.tax_rate}%): ₹{gross_pay * self.salary_details.tax_rate / 100:.2f}")
        print(f"Net Pay: ₹{net_pay:.2f}")
        print(f"Annual Net Salary: ₹{net_pay * 12:.2f}")
        print("------------------------------------------------------")
