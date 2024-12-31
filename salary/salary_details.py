class SalaryDetails:
    def __init__(self, basic, da, hra, ta, bonus, tax_rate):
        self.basic = basic
        self.da = da
        self.hra = hra
        self.ta = ta
        self.bonus = bonus
        self.tax_rate = tax_rate

    def calculate_gross_pay(self, salary):
        monthly_salary = salary.calculate_monthly_salary()
        return monthly_salary + self.da + self.hra + self.ta + self.bonus

    def calculate_net_pay(self, salary):
        gross_pay = self.calculate_gross_pay(salary)
        tax_deduction = gross_pay * self.tax_rate / 100
        return gross_pay - tax_deduction
