import random

print("If you enter wrong choices twice in a row, point will be granted to the computer.") 

n = int(input("\nEnter number of innings : "))
choices = ["stone", "paper", "scissor"]

com_p = 0
me_p = 0    
x = None

print("\n\tchoices = [stone, paper, scissor]")

for i in range(0, n):
  
    me = input("\nEnter your choice : ")
    me = me.lower()
    com = random.choice(choices)

    print("\nComputer chose : ", com)
    print("You chose      : ", me)

    if(com=="stone" and me=="paper"):
        x = "you win"
    elif(com=="stone" and me=="scissor"):
        x = "you lose"
    elif(com=="paper" and me=="scissor"):
        x = "you win"    
    elif(com=="paper" and me=="stone"):
        x = "you lose"  
    elif(com=="scissor" and me=="stone"):
        x = "you win"      
    elif(com=="scissor" and me=="paper"):
        x = "you lose" 
    elif(com==me):
        x = "Tie"
    else:
        x = None
        print("\t⚠️  Invalid choice..")
        print("\t🔁 Re-enter") 
        
        me = input("\nEnter your choice : ")
        com = random.choice(choices)
        print("\nComputer chose : ", com)
        print("You chose      : ", me)
         
        if(com=="stone" and me=="paper"):
            x = "you win"
        elif(com=="stone" and me=="scissor"):
            x = "you lose"
        elif(com=="paper" and me=="scissor"):
            x = "you win"    
        elif(com=="paper" and me=="stone"):
            x = "you lose"  
        elif(com=="scissor" and me=="stone"):
            x = "you win"      
        elif(com=="scissor" and me=="paper"):
            x = "you lose" 
        elif(com==me):
            x = "Tie"
        else:
            x = None
            print("\t❌ Invalid again! Point granted to computer.")
            com_p += 1

    if(x == None):
        pass    
    if(x == "you lose"):
        com_p += 1
        print("\t💻 Computer wins this inning!")
    if(x == "you win"):
        me_p += 1
        print("\t🎉 You win this inning!")
    if(x == "Tie"):
        print("\t🫱🏼‍🫲🏻 It's a tie!")

    print(f"\n After {i+1} innings :-  computer={com_p} : you={me_p}")

print("\n--- 🏆 Final Result ---")
if me_p > com_p:
    print("🎉 You won the game!")
elif com_p > me_p:
    print("💻 Computer won the game!")
else:
    print("🫱🏼‍🫲🏻 It's a tie!")
    
    
      # smart code by claude...
"""
     
def get_result(com, me):
    #Returns result or None if invalid choice.
    if me not in choices:
        return "invalid"
    if com == me:
        return "tie"
    wins = [("paper", "stone"), ("scissor", "paper"), ("stone", "scissor")]
    if (me, com) in wins:
        return "you win"
    return "you lose"

def play_turn():
    #Plays one turn, returns result.
    me = input("\nEnter your choice: ").strip().lower()
    com = random.choice(choices)
    print("Computer chose:", com)
    print("You chose:", me)
    return get_result(com, me), com, me

for i in range(n):
    result, com, me = play_turn()

    if result == "invalid":
        print("\t⚠️ Invalid choice.. Re-enter")
        result, com, me = play_turn()

        if result == "invalid":
            print("\t❌ Invalid again! Point to computer.")
            com_p += 1
            result = None  # skip normal scoring

    if result == "you win":
        me_p += 1
        print("\t🎉 You win this inning!")
    elif result == "you lose":
        com_p += 1
        print("\t💻 Computer wins this inning!")
    elif result == "tie":
        print("\t🤝 Tie!")

    print(f"\n  After {i+1} innings :- computer={com_p} : you={me_p}")      
    
   """