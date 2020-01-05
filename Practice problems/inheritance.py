class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        Employee.__init__(self,id, name)
        self.weekly_salary = weekly_salary

    def _calculate_payroll(self):
        return self.weekly_salary
    
    def calculate_payroll(self):
        return 0

class HourlyEmployee(Employee,SalaryEmployee):
    def __init__(self, id, name, weekly_salary, hours_worked, hour_rate):
        Employee.__init__(self,id, name)
        SalaryEmployee.__init__(self, id, name, weekly_salary)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def __repr__(self):
        return (str(self.weekly_salary) + " " + str(self.hours_worked) + " " + str(self.hour_rate))

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate * self.weekly_salary

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        SalaryEmployee.__init__(self,id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        a = SalaryEmployee(self.id, self.name,self.weekly_salary)
        return a.calculate_payroll() * self.commission

commission_employee = CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
print(commission_employee.calculate_payroll())

hourly_employee = HourlyEmployee(2, 'Brad',35,20,450)
print(hourly_employee.calculate_payroll())
print(hourly_employee)