#Library Management

# Book CLass initializes the book details
class Book:
    id = ''

    def __init__(self, bookID):
        self.name = input('Enter Book Name : ')
        self.author = input('Enter Book Author : ')
        self.year = input('Enter Book Year: ')
        Book.id = bookID

# Print book details
    def print_details(self):
        print('Book Name : ', self.name)
        print('Book ID : ', Book.id)
        print('Book Author & Year: ', self.author, self.year)

#Faculty class inherits the book class and also inherits the Book class
class Faculty(Book):
    def __init__(self, f_id, f_name, f_quota, bookID):
        super().__init__(bookID)
        self.f_id = f_id
        self.f_name = f_name
        self.f_quota = f_quota

    # Method Overriding
    def print_details(self):
        print("Faculty Name: ", self.f_name)
        print('Faculty ID: ', self.f_id)
        print('Faculty Quota: ', self.f_quota)

#Student class initialises the details of students
class Student():
    fname = ''
    id = ''

    def __init__(self):
        Student.fname = "Jai"
        self.lname = "Koya"
        Student.id = 189
        self.gender = "Male"
        self.quota = 8

#Department class inherits the details of depatment
class Department():
    name = ''

    def __init__(self):
        Department.name = "Computer Science"
        self.rackno = 7

#Collect class inherits the student,department and book
class Collect(Student, Department, Book):
    def __init__(self):
        Student.__init__(self)
        Book.__init__(self, 56)
        Department.__init__(self)

#Prints the inherited properties of super classes
    def print_details(self):
        print("Book Collection Details:\nStudent Name:{}\nStudent ID:{}\nBook ID:{}\nDepartment Name:{}"
              .format(Student.fname, Student.id, Book.id, Department.name))

#faculty object creation and overided method calling
faculty = Faculty(25, 'jai', 112, 56)
faculty.print_details()

#Collect class and overided method calling
collect = Collect()
collect.print_details()