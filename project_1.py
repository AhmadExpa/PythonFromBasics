# ------------------------------------------------------------------------
import random
# ------------------------------------------------------------------------
def games_rule(comp,player):
    if (comp==player):
        return   None
    if (comp == "s" and player == "x"):
        return  True
    if (comp == "p" and player == "s"):
        return  True
    if (comp == "x" and player == "p"):
        return  True
    if (comp == "x" and player == "s"):
        return  False
    if (comp == "s" and player == "p"):
        return  False
    if (comp == "p" and player == "x"):
        return  False

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
for_quit = "n"
while for_quit != "q":

     you = str(input("Player Turn: Stone(s) Paper (p) Scissor(x) ? = "))
     # ------------------------------------------------------------------------
     while (you !="s")or(you !="p")or(you !="x"):
      if (you =="s")or(you =="p")or(you =="x"):
         break
      else :
         print(f"Are You Stupid. \n You Enter this {you} \n")
         you = str(input("Player Turn: Stone(s) Paper (p) Scissor(x) ? = "))
     # -------------------------------------------------------------------------
     computer = random.randint(1, 3)
     if computer==1:
        computer = str("s")
     elif computer==2:
         computer = str("p")
     elif computer==3:
         computer = str("x")
# -------------------------------------------------------------------------
     game_win = games_rule(computer, you)
# -------------------------------------------------------------------------
     if  game_win == True:
      print(f"Computer Choose {computer} and You {you} . \n {{ Thus Computer Wins }}\n")
     elif  game_win == False:
      print(f"Computer Choose {computer} and You {you} . \n {{ Thus You Wins }}\n")
     elif  game_win == None:
      print(f"Computer Choose {computer} and You {you} . \n {{ Thus It's Tie }} \n")
     for_quit = input("Enter 'q' To Quit and 'n' for not to quit From Game \n ")
# --------------------------------------------------------------------------

