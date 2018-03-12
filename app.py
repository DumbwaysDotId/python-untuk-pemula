# parent class
class Person:

    name = "Joko"

    def walk(self):
        return "walking"

    def drink(self):
        return "drinking"

# child class
class Employee(Person):

    def get_name(self):
        return self.name

    def walk_and_drink(self):
        drink = self.drink()
        return "employee is walking n " + drink

employee = Employee()
employee.name = "Cintya"
print(employee.get_name())
print(employee.walk_and_drink())
