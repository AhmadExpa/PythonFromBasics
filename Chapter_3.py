# # String Slicing 
# ''' string slicing is used to give user a specific part of the string 
# means if the string is a = pakistan you can also print only word "pak" by using string slicing
# '''
# # string slicing syntax 
# #  new_variable = old_variable(that contains the string)[first_index:second_index] 
# # keep in mind that first index is included and second is not
# # Let see by example
# # -------------------------------------------------------------------
# name = "Ahmad" 
# # -------------------------------------------------------------------
# # digits start from 0=a, 1=h, 2=m, 3=a, 4=d 
# # or in negative  sequence one its starts from right to left and ends on -1 
# # -5=a, -4=h, -3=m, -2=a, -1=d
# # -------------------------------------------------------------------
# name = "Ahmad" 
# string_slicing = name[1:4] # normal
# print("String Slicing Normally = ",string_slicing)
# # -------------------------------------------------------------------
# name = "Ahmad" 
# string_slicing_negative = name[-4:-1] # Answer will be the same using negative sequence
# print("String Slicing Negative = ",string_slicing_negative)
# # -------------------------------------------------------------------
# # for joining two strings we simply add them like
# join_string = string_slicing + string_slicing_negative
# print("Joining Two Strings Normal+Negative = ",join_string)
# # --------------------------------------------------------------------
# # Slicing with Skip Value 
# name = "Ahmad" 
# print("Slicing With Skip Value = ",name[0:4:2]) # name[first_index:second_index:number_of_skips(if writes 1 it means one by one digit same as above)]
# # --------------------------------------------------------------------
# # String_Function
name = "Ahmad Ashfaq" 
print("Show The Number of characters in the string including spaces",len(name)) # Len Function
print(name.endswith("hag")) # Endswith Function show that whether the string ends with that specific letter or not 
print(name.count("a")) # .count function used to count a letter in a string
print(name.capitalize()) # capitalize function used to captial the first letter of the string
print(name.strip()) # this function is used to remove extra spaces from the starts
print(name.find("Ahm")) # find a word in a string (the first time that word repeats it gives it index)
print(name.replace("Ahmad", "Ahmed")) # used to replace all the old with the new one
print("Escape Sequences \n \t tab \n")
# # ------------------------------------------------------------------------ 
# # ----------------------------------------------------
# # END



