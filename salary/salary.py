class Salary:
    def __init__(self, salary_type, amount):
        self.salary_type = salary_type
        self.amount = amount

    def calculate_monthly_salary(self):
        if self.salary_type == "annual":
            return self.amount / 12
        elif self.salary_type == "monthly":
            return self.amount
        else:
            raise ValueError("Invalid salary type")

    def calculate_annual_salary(self):
        if self.salary_type == "annual":
            return self.amount
        elif self.salary_type == "monthly":
            return self.amount * 12
        else:
            raise ValueError("Invalid salary type")
