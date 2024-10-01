# Inheritace And More On OOPs
# Inheritace is the way of creating new class from old class. 
# The old class will be the parent class and the new class will occur as a Child Class.
# Types Of inheritance 
# 1. Single Inheritace
# 2. Multiple Inheritace
# 3. MultiLevel Inheritance 
# ----------------------------------------------------------
# class data:
#     def __init__(self, student_name, semester, teacher_name, teacher_grade):
#         self.student_name = student_name
#         self.semester = semester
#         self.teacher_name = teacher_name
#         self.teacher_grade = teacher_grade

# class teaching_staff:
#     def teacher(self):
#         job_type = "Government"
#         print(f"Teacher Name : {self.teacher_name} \n Teacher Grade : {self.teacher_grade}")
# class student:
#     def student(self):
#      last_semester = 8
#      if self.semester < 8 :
#         print(f"Following Semester Are Left = {8 - self.semester} For {self.student_name}\n")
#      else :
#         print("You Are Graduated From This Institute \n")
# class administration (data, teaching_staff, student): # Multi Inheritance If we call one Class then it will be one Single Inheritance
#     college = "GCU"

# # ----------------------------------------------------------------


# data_form = administration("Ahmad", 3, "Imran", 17)
# data_form.teacher()
# data_form.student()



#               super method is used to access the method of the super class super __init__

class One:
    def __init__(self):
        print("Initializing  .One.... \n")
    def print_function(self):
     print("This IS Class ONe")
class Two(One):
    def __init__(self):
        print("Initializing  .Two.... \n")
    def print_function(self):
     super().print_function()
     print("This IS CLass TWo")
class Three(Two): # also an example of multi level inheritance
    def __init__(self):
        print("Initializing  .Three.... \n")
    def print_function(self):
     super().print_function()
     print("This IS Class Three")

one_1 =  One()
one_1.print_function()
two_2 = Two()
two_2.print_function()
three_3 = Three()
three_3.print_function()
# -------------------------------------------------------------------------
#             @classmethod() is method which is bound to the class not the object of the class 
#              which means that you can change the value of the attribute in the class through the object
# class Example:
#     institute = "GCU"
#     location = "Lahore"
#     post_code = 54000
#     @classmethod
#     def changePostcode(cls, cpc):
#         cls.post_code = cpc

# e = Example()
# print(e.institute)
# print(e.location)
# print(e.post_code)
# e.changePostcode(54400)
# print(e.post_code)
# ............................................................................
#                @property() decorator also a getter method type used to do changing within function
# class Student:
#     semester_fee = 100000
#     admission_charges = 20000
#     sports_fee = 3000
#     it_facilities = 2000
#     @property
#     def total_fee(self): # total fee calculation
#         return self.semester_fee + self.admission_charges + self.sports_fee + self.it_facilities
#     @total_fee.setter
#     def total_fee(self, fee): # changing in fee occurs only in semester fee
#         self.semester_fee = fee - self.admission_charges - self.sports_fee - self.it_facilities

## print all the data .
# stu = Student()
# print(stu.semester_fee)
# print(stu.admission_charges)
# print(stu.sports_fee)
# print(stu.it_facilities)
# print(stu.total_fee)
## change in total fee
# stu.total_fee = 120000
## change occurs in semester fee
# print(stu.semester_fee)
# ........................................................................
#                              OverLoading
# operators in python can be overload by the dunder method
#  it is used when the user or the programmer wants to 

# for example when you used to add two number 
# and that time you want that the code automatically realize that the number are add 
# and the code do a specific task on its execution
# like p1 + p2 ---> p1 __add__ p2

# class Number:
#     def __init__(self,num):
#         self.num = num
#     def __add__(self,num2):
#         print("Iniatializing the Addition Process")
#         return self.num + num2.num

# num1 = Number(3)
# num2 = Number(5)
# sum = num1 + num2 # at this point the function runs and return value to the variable sum
# print(sum)

# there are many other OverLoading operators in python 
# which can be found through the python documentation
# like 
#  p1 + p2 ---> p1 __add__ p2
#  p1 * p2 ---> p1 __mul__ p2
#  p1 - p2 ---> p1 __sub__ p2
#  p1 // p2 ---> p1 __floordiv__ p2
#  p1 / p2 ---> p1 __truediv__ p2
# __str__ method is used to get a display upon calling a string in program
#  __len__ method is used to get a display upon calling a len function in code
# like
# class Example:
#    def __init__(self, string):
#     self.string = string
#    def __str__(self):
#         return f"You Enter a String: {self.string}"
#    def __len__(self):
#         return len(self.string)

# var = Example("string")
# print(var)
# print(len(var))
# --------------------------------------------------------------------------------
