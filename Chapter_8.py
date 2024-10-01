# -----------------------------------------------
# # functions are used to break the program into small parts
# # and each part perform a specific task 
# def cand(name = "NAME"):
#    return print(f"This Letter is received by all the shortlisted candidates after the interview.  \n Congratulation {name} \n For Further assistance Call us : \n \t 0000800000 ")
# cand(input("Enter The Name Of Recommended Candidate : "))
# # ---------------------------
# # Recursion is commonly used to code directly the algorithm. 
# # In Recursion the function call itself until the specified condition becomes false 
def factorial_simple(num):
    if num == 1 or num == 0:
        return print(f"Factorial of {num} is 1")
    i = 1
    result = 1
    while i <= num:
     result = result * i
     i = i + 1
    return print(f"Factorial Of {num} is {result} \n")

def factorial_recursive(num):
   
    if num == 1 or num == 0:
        return 1
    return  num * factorial_recursive(num-1)


# factorial_simple(5)
factorial_recursive(5)
# print(f)

