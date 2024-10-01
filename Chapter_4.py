# # list are the container that store a set of values in a variable
var = ["Ahmad", "Ashfaq", 26, 3, 2004]
print(f"original list is  = {var}")
# list slicing ------------------------------------------------------------------------------------
print(var[0:2])
print(var[2:])
var[2] = 27
print(var)
# # list method -------------------------------------------------------------------------------------
list_name = [1, 2, 5, 6, 7, 9, 8]
print(list_name)
# list_name.sort()
# print("Sorting The List = ",list_name)
# # --------------------------------------------------------------------------------------
# list_name.reverse()
# print("Sorting The List in reverse order= ",list_name)
# # --------------------------------------------------------------------------------------
# list_name.append("GCUL")
# print("Append in The List add the specific value in the end of the list = ",list_name)
# # --------------------------------------------------------------------------------------
list_name.insert(0, "AHMAD")
print("Inserting in the List = ",list_name)
# # --------------------------------------------------------------------------------------
# list_name.pop(0)
# print("Remove a value from The List through index= ",list_name)
# # --------------------------------------------------------------------------------------
# list_name.remove("GCUL")
# print("Remove a value from The List through by writing it properly= ",list_name)
# # --------------------------------------------------------------------------------------
# # --------------------------------------TUPLE-------------------------------------------
# # tuple is a set of values that cannot be changed once declared 
# tuple_example = ("a","b","c",1,2,3)
# # or to declare a one item tuple you must use the comma with it  like (1, ) otherwise
# # (1) only is declared as an integer for the variable
# print(tuple_example)
# # tuple_example[0]="change"
# # print(tuple_example)
# # function for tuples are .count .index 
# # ---------------------------------------------------------------------------------------
# print(tuple_example.index(1)) # index requires atleast 1 argument (for indexing)
# print(tuple_example.count(2)) # count 2 value repeats in the tuple
# # ----------------------------------------------------
# # END
