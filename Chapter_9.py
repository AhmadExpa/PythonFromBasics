# -----------------------------------------------------
# The data in the ram is volatile ,
# so after the execution of a program all its content will be lose
# if we need to use that data which is entered by the user during the execution ,
# so we need to store that data in our harddisk or something which stores permanentent
# ------------------------------------------------------------------
# To open a file in python we use open() but the thing matters at this point is that
# the file you wanna to read should already present in the hdd /etc

# so i'm gonna to write a file or making a file first and enters some data in it 
# and then read it . To write a program in python we use write or append mode.

# write_file = open("stone_paper_scissor_hi_score.txt","w")
# write_file.write("This Text File Includes the high score value of The Stone Paper Scissor Game : ")
# write_file.close()

# Now read the above file ------------------------------------------

# read_file = open("stone_paper_scissor_hi_score.txt","r")
# full_file = read_file.read() # read full file
# print(full_file)
# read_line = read_file.readline() # read specific number of lines by default it is 1
# print(read_line)
# read_character = read_file.read(5) # read the file character wise 
# print(read_character)
# read_file.close()
# --------------------------------------------------------------------
# Note : You can read a file at a once at a point 
# which means you can either read it full or line wise or character wise
# --------------------------------------------------------------------
# the simplest way to read and write a file is following the above is the standard way
# option = int(input("How Many Candidates Name You Want To Enter : "))
# with open("Candidates_file.txt","w") as candidates:
#     for i in range(1,option+1):
#         name = input("Enter The Names Of Candidates = ")
#         candidates.write(f" {i}. {name} \n")
# # -------------------------------------------------------
# caste = ["awan", "malik", "rajpoot", "butt", "jutt"]

# with open("Candidates_file.txt","r") as f:
#     content = f.read()
   
# with open("Candidates_file.txt","w") as f:
#      for word in caste:
#         content = content.replace(word,"Caste_Removed")
#      f = f.write(content)
# # --------------------------------------------------------
with open("products.txt","r") as f:
    var = True
    while var:
     content = f.readline()
     if "lays" in content.lower():
        print("Yes It's Available \n")
        print(content)
    else:
        print("Nothing Found \n")
# -------------------------------------------------------
# Ends




