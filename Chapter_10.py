# Solving a problem by creating objects is called object oriented language, 
# this concept works on reusable of code.
# A class is a blueprint of creating objects. // Class Name Should Be written in Pascal Case.
# it just like a template for the user. memory is only allocated after object instantiation
# objects (oops) basically invoke the method available to it without revealing the details 
# this is called abstraction or encapsulation 
# types are 
# 1.Class
# 2.Attribute
# 3.Method

class Form:
    candidates = "ISSB" # Class Attribute

    def __init__(self, roll_no, name, father_name, cnic, father_cnic): # Constructor
        self.roll_no = roll_no
        self.name = name
        self.father_name = father_name
        self.cnic = cnic
        self.father_cnic = father_cnic

        with open("Candidates_file.txt","w") as f:
            content = f.write(f"{self.roll_no}. {self.name} {self.cnic} {self.father_name}  {self.father_cnic}   \n")
        print(f"Data of The Following [{self.name}]Candidate is Created \n")

    def candidates_details(self):
        with open("Candidates_file.txt","r") as f:
            content = f.readline()
            if self.name.lower() in content.lower():
                print(content)
            else:
                print("No Record Found ! \n")

    @staticmethod
    def recommendation_letter():
        print("It is Inform To the Candidate.\n Congratulation On Recommendation From ISSB ")


# Prompt the user for the candidate's details
option = ""
while option != "e":
  roll_no = str(input("Enter The Candidate Roll No. : "))
  name = str(input("Enter The Candidate Name : "))
  father_name = str(input("Enter The Candidate Father Name : "))
  cnic = str(input("Enter The Candidate CNIC : "))
  father_cnic = str(input("Enter The Candidate Father's CNIC : "))
  option = str(input("Do You Want To Exit Write 'e' otherwise 'n' for not :  "))

# Create an object of the Form class with the user-provided details
candidate = Form(roll_no, name, father_name, cnic, father_cnic) # initiateded 
# candidate.name = "Ahmad" # search for the candidate by name
# candidate.candidates_details()

