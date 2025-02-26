# Visitor design pattern

class Courses:

    def accept(self, visitor):
        visitor.visit(self)

    def teaching(self, visitor):
        print(self, "Taught by ", visitor)

    def studying(self, visitor):
        print(self, "studied by ", visitor)


    def __str__(self):
        return self.__class__.__name__


# Concrete Courses
class SDE(Courses): pass

class STL(Courses): pass

class DSA(Courses): pass


class Visitor:

    def __str__(self):
        return self.__class__.__name__


class Instructor(Visitor):
    def visit(self, crop):
        crop.teaching(self)


class Student(Visitor):
    def visit(self, crop):
        crop.studying(self)


# Concrete classes
sde = SDE()
stl = STL()
dsa = DSA()

# Creating Visitors
instructor = Instructor()
student = Student()

# Visitors visiting courses
sde.accept(instructor)
sde.accept(student)

stl.accept(instructor)
stl.accept(student)

dsa.accept(instructor)
dsa.accept(student)
