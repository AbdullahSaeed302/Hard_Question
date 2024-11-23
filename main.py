'''
3. Create a class "Employee" and add salary and increment properties to it.

Write a method "salaryAfterIncrement" method with a @property decorator with a setter 
which changes the value of increment based on the salary.
# '''

# My Method:
salary_ = int(input("Enter your Salary: "))
increment_ = int(input("Enter you Increment Percentage: "))

class Employee:
    salary = salary_
    increment = increment_

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * (self.increment / 100)) # Returns the new salary after increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = ((new_salary / self.salary) -1) * 100 # Sets the increment value!

# Creating Objects!
object = Employee()
print("-" * 40)

print(f"Salary before increment: {object.salary} Rupees")

print("-" * 40)

print(f"Salary after increment: {int(object.salaryAfterIncrement)} Rupees")

print(f"Increment percentage: {round(object.increment)}%")

print("-" * 40)