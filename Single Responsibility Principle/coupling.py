# Coupling: Coupling is the degree of interdependence between software modules; a measure of how closely connected two routines or modules are; the strength of the relationships between modules.

class Student:

    def __init__(self, id: int, name: str, age: int, address: str):
        self.id = id
        self.name = name
        self.age = age
        self.address = address

    def save(self):
        # save the student to the database -> MySQL
        pass

    def get_student_id(self):
        # get the student id
        return self.id
    
    def get_student_name(self):
        # get the student name
        return self.name
    
"""
This is a tightly coupled class. It has 2 responsibilities - saving the student to the database and getting the student details.
The responsibility of the save method is to save the student to the database. Hence it deals with the database connection and the SQL query which should not
be the responsibility of this class. The get_student_id and get_student_name methods are also not related to the save method. Hence this class violates the
Single Responsibility Principle.
"""

class Student:

    def __init__(self, id: int, name: str, age: int, address: str):
        self.id = id
        self.name = name
        self.age = age
        self.address = address

    def save(self):
        StudentRepository().save(self)

    def get_student_id(self) -> int:
        # get the student id
        return self.id
    
    def get_student_name(self) -> str:
        # get the student name
        return self.name
    

class StudentRepository:

    def save(self, student: Student):
        # save the student to the database -> MySQL
        pass

"""
The class StudentRepository is responsible for saving the student to the database. The class Student is responsible for getting the student details.
Both classes are now following the Single Responsibility Principle and loosely coupled.
"""