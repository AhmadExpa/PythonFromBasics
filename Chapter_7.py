# ----------------------------------LOOPS--------------------------------------------------
# repeats a set of instructions in Python (loop) 
# while Loop 
# i = 0
# while i<10:
#     print("Yes",i)
#     i = i + 1
# print("Done \n")
# -----------------------------------------------
# # use of sets in loops 
# i = 1
# names_of_candidates = []
# while i <= 10 :

#  names_of_candidates.insert(i,input(f"Enter Name Of Candidate No.{i} = "))
#  i = i + 1
# print("Done \n")
# print("Following Canditates Names Are Given \n")
# names_of_candidates.sort()
# # print(names_of_candidates)
# # -----------------------------------------------
# # to use the for loop function in this program 
# for items in names_of_candidates :
#     print(items)
# print("Done \n")
# -----------------------------------------------
# for and range loop use in python 
# for i in range(1, 10, 2): # range (start point, end point but it is not included at the end, increment or skip value by default it is 1 )
#     print(i)
# -----------------------------------------------
# # for with else ( When the loop exhaust then the else statement works )
# for i in range(10):
#     print(i)
# else:
#     print("Done \n")
# ------------------------------------------------
# break statement in loop 
# for i in range(2100):
#     print(i)
#     if i == 2023:
#         break
# else:
#     print("This Statement prints when your loop runs successfully without any break")
# --------------------------------------------------
# continue statement in loop is used when you want to continue the loop on a specific value without executing the other parts below the continue statement in the loop body
# for i in range(10):
#     if i == 7: # when the i becomes 7 it continues to the the next iteration without printing the 7
#         continue
#     print(i)
# --------------------------------------------------
# pass statement (it means do nothing on a specific condition)
# i = 5
# if i < 10:
#   pass # if I don't write pass then the program throw an error if I don't write anything in the body of if
# print(i)
# ------------------------------------------------
# stars print
n = 100
i = 0
while n>-3:
     i = i+1
     print("*" * (n))
     print(" "*i,end="")
     n = n-2
# ----------------------------------------------------
# END