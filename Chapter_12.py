# there are many built-in exception in python when something goes wrong in the code 
# this exception show the error without cracking the whole process of the code
# try:
#     #code
#  except ValueError :
#     #code
#  except ZeroDivisionError :
#     #code
#  except TypeError :
#     #code
#  except Exception : // for all other type of error
# --------------------------------------------------------------
# >>>>>>>>>>>> try with else clause <<<<<<<<<<<<<

# try:
#     #code
#  except:
#     #code
#  else: // this statement only runs after the successfully execution of TRY: #code
#     #code
# --------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>> try with finally <<<<<<<<<<<<<<<<<<<<<<
# try:
#     #code
#  except :
#     #code
# finally: // this code runs regardless of the error exception
#     #code
# --------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>> Enumerate <<<<<<<<<<<<<<<<<<<<<<<<
# this function is used when we want to print the items in the list with index 
# list1 = ["Ahmad", "Hamad", "Abdul Wahid", 2004, 2006, 2010]
# for index, item in enumerate(list1):
#     print(index, item)
# --------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>List Comprehession<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# list comprehession is an elegent way of creatig list from the existing one 
# like
i = 0
list1 = [1,2,3,4,4,5,6,8,9,0,66,7]
print(f"Original List = {list1}")
list2 = [i for i in list1 if i <= 8] # i means items in list 
list3 = [i for i in list2] # copy the list 
print(list2)
print(list3)
# ----------------------------------------------------------------
# import random 
# list1 = []
# index = 0
# n = 1
# guess =  random.randint(1, 100)
# print(guess)
# while  True:
#     try:
#      num = int(input("Enter Any Num "))
     
#      if num == guess:
#         print("You Guess The Number Correct \n ")
#         list1.append(num)
#         break
#      elif num > guess:
#         list1.append(num)
#         print("Enter Smaller Number \n")
#      elif num < guess:
#         print("Enter Greater Number \n")
#         list1.append(num)
#     except Exception as e:
#         print(f"Enter Valid Arguments otherwise this error comes : {e} \n")
#     else:
#         n +=1
#     # finally:
#     # #     print("Done Regardless of Error \n")
# print(f"Well Done You Guess The Number In {n} attempts \n")
# for index, items in enumerate(list1) :
#     print(f"{index}Values Which You Enter : {items} ")
# ----------------------------------------------------------------------------




