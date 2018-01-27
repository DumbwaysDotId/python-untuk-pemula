# class
class Person():
    name = "Joko"
    age = 10
    gender = "male"

    def get_personality(self):
        return "bad"


class Employee(Person):
    def __init__(self, **kwargs):
        k = kwargs
        self.salary = k['salary']

    def get_name(self):
        return self.name

#instantiate class
employee = Employee(salary=1000)
employee.name = "Samohong"
print(employee.name, employee.salary, employee.get_personality())
