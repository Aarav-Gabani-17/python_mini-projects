import random
#______________________________________
#               MENU
#______________________________________
def menu():
    print("1️⃣ Easy   - 1 to 100 ")
    print("2️⃣ Medium - 1 to 500 ")
    print("3️⃣ Hard   - 1 to 1000 ")
    print("4️⃣ Insane - 1 to 2500 ")
#______________________________________
#           FIRST GUESS
#______________________________________
def guess():
    try:
        no = int(input("\nGuess : "))
    except ValueError:
        while(True):
             try:
                no = int(input("\nGuess : "))
                break
             except:
                 print("Invalid input ⚠️")
                 continue 
    global count
    count = 1
#_________________________________________________
#               ALL POSSIBILITIES 
#_________________________________________________
    while(True):
        if(no > ran):
            count += 1
            try:
                no = int(input("\nGuess lower : "))
            except ValueError:
                while(True):
                    try:
                       no = int(input("\nGuess lower: "))
                       break
                    except:
                       print("Invalid input ⚠️")
                       continue 
                      
                    

        elif(no < ran):
            count += 1
            try:
                no = int(input("\nGuess higher : "))
            except ValueError:
                while(True):
                    try:
                       no = int(input("\nGuess higher: "))
                       break
                    except:
                       print("Invalid input ⚠️")
                       continue 

        elif(int(no) == ran):
            print("\nYou guessed the correct number! 🎉💫")
            print(f"\nYou took {count} attempt(s) to guess!")
            break

end = "yes"

while((end).lower() == "yes"):

    menu()
#____________________________________________________________
#                       CHOICE SELECTION
#____________________________________________________________ 
    choice = input("Enter the choice : ")

    while(True):
        if(choice.isnumeric() == False):
            print("\n Invalid input...")
            choice = input("\n Re-Enter the choice : ")
        elif(choice.isnumeric() == True):
            if(int(choice) > 4 or int(choice) < 1):
                print("\n Invalid input...")
                choice = input("\n Re-Enter the choice : ")
            else:
                break
#____________________________________________________________
#                      EASY MODE
#____________________________________________________________
    if(choice == "1"):
        ran = random.randint(1, 100)
        guess()
        with open("easy.txt", "a") as e:
            pass
        with open("easy.txt", "r+") as e:
            try:
                score = e.read()
                if(score == ""):
                    raise ValueError
            except ValueError:
                if(score == ""):
                    score = "0"
            if(count < int(score) or score == "0"):
                e.seek(0) #🔰 Use : after read, curser is at the end then write won't overwrite 
                          # so seek(0) drag the curser at starting point
                e.write(f"{count}")
                # 🔰 Use : e.truncate() — old leftover characters remain.
                #    e.g. old score "100", new "9" → file becomes "900" without truncate.
                e.truncate()
                print("Congratulations, you broke the old record! 🏆")
                print(f"Best score = {count}")
#____________________________________________________________
#                      MEDIUM MODE
#____________________________________________________________
    elif(choice == "2"):
        ran = random.randint(1, 500)
        guess()
        with open("medium.txt", "a") as m:
            pass
        with open("medium.txt", "r+") as m:
            try:
                score = m.read()
                if(score == ""):
                    raise ValueError
            except ValueError:
                if(score == ""):
                    score = "0"
            if(count < int(score) or score == "0"):
                m.seek(0)
                m.write(f"{count}")
                m.truncate()
                print("Congratulations, you broke the old record! 🏆")
                print(f"Best score = {count}")
#____________________________________________________________
#                      HARD MODE
#____________________________________________________________
    elif(choice == "3"):
        ran = random.randint(1, 1000)
        guess()
        with open("hard.txt", "a") as h:
            pass
        with open("hard.txt", "r+") as h:
            try:
                score = h.read()
                if(score == ""):
                    raise ValueError
            except ValueError:
                if(score == ""):
                    score = "0"
            if(count < int(score) or score == "0"):
                h.seek(0)
                h.write(f"{count}")
                h.truncate()
                print("Congratulations, you broke the old record! 🏆")
                print(f"Best score = {count}")
#____________________________________________________________
#                      INSANE MODE
#____________________________________________________________
    elif(choice == "4"):
        ran = random.randint(1, 2500)
        guess()
        with open("insane.txt", "a") as i:
            pass
        with open("insane.txt", "r+") as i:
            try:
                score = i.read()
                if(score == ""):
                    raise ValueError
            except ValueError:
                if(score == ""):
                    score = "0"
            if(count < int(score) or score == "0"):
                i.seek(0)
                i.write(f"{count}")
                i.truncate()
                print("Congratulations, you broke the old record! 🏆")
                print(f"Best score = {count}")
#____________________________________________________________
#                      CONTINUE / EXIT
#____________________________________________________________
    end = input("\n Type yes to play again, anything else to quit : ")
