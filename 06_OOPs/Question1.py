class Student:
    def display_details(self, Name, rollno, marks):
        self.name = Name
        self.rollno = rollno
        self.marks = marks
        print(f"Name:  {self.name}, Roll No: {self.rollno}, Marks: {self.marks}")
    
student1 = Student()
student1.display_details("Alice", 101, 95)
student2 = Student()
student2.display_details("Bob", 102, 88)