class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi,my first {self.name}. I am {self.age} years old and I am {self.gender}.")

parson1 = Person("Gedeon","22","Male")
person2 = Person("clemantine","20","Female") 