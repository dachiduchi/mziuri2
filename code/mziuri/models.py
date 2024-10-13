class Member:
    def __init__(self , name , age , status , subject):
        self.name = name
        self.age = age
        self.status = status
        self.subject = subject

class Teacher:
    def __init__(self , name , age):
        self.name = name
        self.age = age

class Teacher(Member):
    def __init__(self , name , age , status , subject):
        super().__init__(name , age , status , subject)
        self.salary = salary

    def calculate_yearly_salary(self):
        return self.salary * 12

class Student:
    def __init__(self , name , age):
        self.name = name
        self.age = age


Dachi = Student("dachi" , 14)
shotiko = Teacher("shotko" , 21)

print("dachi")