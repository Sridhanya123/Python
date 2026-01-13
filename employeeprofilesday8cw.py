class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self, name, age,employee_id):
        super().__init__(name, age)
        self.employee_id=employee_id
    def show_details(self):
        print("Name",self.name)  
        print("Age",self.age)
        print("EmployeeID",self.employee_id) 