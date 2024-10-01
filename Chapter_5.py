# # dictionary is a collection of key value pairs such as below
# # ----------------------------------------------------------------------------------
# dictionary = {
#     1:24,
#     "Name":"Ahmad",
#     "Father": "Ashfaq",
#     "DOB":"26-03-2004", 
#     "Marks":75,
#     "list" : [1036, 951, 75]
# }
# print(type(dictionary))
# print(dictionary)
# print(dictionary["DOB"])

# # properties of dictionary
# # it is unordered
# # it is mutable
# # it is indexed
# # -----------------------------------------------------------------------------------
# # ------------------------------ Dictionary Methods ---------------------------------
dictionary = {
    1:24,
    "Name":"Ahmad",
    "Father": "Ashfaq",
    "DOB":"26-03-2004", 
    "Marks":75,
    "list" : [1036, 951, 75]
}

print(dictionary.items()) # list all the items in the dictionary both keys and values
print(dictionary.keys()) # list all the items in the dictionary only keys
dictionary.update({"Name" : "Hamad", "DOB":"21-09-2006", "Relation With Previous One": "Brother"}) # update and add some new keys and values in the previous dictionary
print(dictionary.items())
print(dictionary.get("Name")) # list only the specific key's value
# # ----------------------------------------------------------------------------------------------------
# # -------------------------------- SETS --------------------------------------------------------------
# # sets are the collection of non-repeatative elements 
# # properties of sets 
# # 1. unordered
# # 2. cannot be changed
# # 3. unindexed means cannot be access by index number
# # 4. cannot contain duplicate values 

# sets = {1, 2, 3, "Ahmad"}
# print(sets)
# # ------------- Methods -------------------------------------------------------------------------------
# sets.update("abc") # add new elements in set but in string form
# print(sets)

# print(sets.__len__()) # Count No. of elements

# sets.remove("a") # Remove the written element from the set
# print(sets)

# sets.pop() # removes a random element from a set
# print(sets)

# sets.clear() # makes the set empty
# print(sets)
# ------------------------------------------------------------------------------------------------------
# a = {1,3,5,7,9,24,"Ahmad"}
# b = {2,4,6,8,0,24,"Hamad"}
# print(a.union(b))
# print(a.intersection(b))

# ------------------------------------------------------------------------------------------------------
# ----------------------------------------------------
# END