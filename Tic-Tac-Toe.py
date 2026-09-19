import random

# ─────────────────────────────────────────
#  BOARD SETUP
#  Player = ❌  |  Computer = ⭕
# ─────────────────────────────────────────
board = [
    "0", "1", "2",
    "3", "4", "5",
    "6", "7", "8"
]

def reset_board():
    """
    Restores all board cells back to their original index strings.
    
    💡 LEARNING — 'global':
        Without 'global board', any assignment like board = [...]
        inside a function creates a NEW local variable and the
        original board outside stays unchanged.
        'global board' tells Python: use the board that lives
        outside this function, not a new local one.
    """
    global board
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]


# ─────────────────────────────────────────
#  SCORE TRACKING  
# ─────────────────────────────────────────
count       = 0   
match_count = 0   
win_count   = 0   
lost_count  = 0   
tie_count   = 0   


# ─────────────────────────────────────────
#  ALL WINNING COMBINATIONS
# ─────────────────────────────────────────
win = [
    (0, 1, 2),   
    (3, 4, 5),  
    (6, 7, 8),   
    (0, 3, 6),   
    (1, 4, 7),   
    (2, 5, 8),   
    (0, 4, 8),   
    (2, 4, 6)    
]


def game():
    """Prints the current state of the board in a 3x3 grid."""
    print("\n")
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])


def comp_random():
    """
    Computer's move logic — three layers of strategy:

      1️⃣  WIN   
      2️⃣  BLOCK 
      3️⃣  RANDOM 

    💡 LEARNING — 'return':
        After placing a move, we immediately 'return' to exit
        the function. Without return, the code would keep
        checking the remaining conditions unnecessarily.
    """
    global com

    # ── Strategy 1: Try to WIN ──────────────────────────────
    for a, b, c in win:
        if(board[a] == board[b] == "⭕" and (board[c] != "⭕" and board[c] != "❌")):
            com = c
            board[int(com)] = "⭕"
            return

    for a, b, c in win:
        if(board[c] == board[b] == "⭕" and (board[a] != "⭕" and board[a] != "❌")):
            com = a
            board[int(com)] = "⭕"
            return

    for a, b, c in win:
        if(board[a] == board[c] == "⭕" and (board[b] != "⭕" and board[b] != "❌")):
            com = b
            board[int(com)] = "⭕"
            return

    # ── Strategy 2: BLOCK the player ────────────────────────
    for a, b, c in win:
        if(board[a] == board[b] == "❌" and board[c] != "⭕"):
            com = c
            board[int(com)] = "⭕"
            return

    for a, b, c in win:
        if(board[c] == board[b] == "❌" and board[a] != "⭕"):
            com = a
            board[int(com)] = "⭕"
            return

    for a, b, c in win:
        if(board[a] == board[c] == "❌" and board[b] != "⭕"):
            com = b
            board[int(com)] = "⭕"
            return

    # ── Strategy 3: RANDOM move ─────────────────────────────
    com = random.randint(0, 8)

    while(True):
        if(board[com] == "❌" or board[com] == "⭕"):
            com = random.randint(0, 8)   # cell taken, try again
        else:
            board[com] = "⭕"            # empty cell found, place move
            break


def results(count):

    global win_count, lost_count, tie_count, match

    if count > 4 and count < 10:
        for a, b, c in win:

            if(board[a] == board[b] == board[c] == "❌"):
                print("\n\tyou won 🎉")
                win_count += 1
                match = "over"
                break

            elif(board[a] == board[b] == board[c] == "⭕"):
                print("\n\tyou lost 😞")
                lost_count += 1
                match = "over"
                break

            elif(count == 9):
                print("\n\tTie 🤝")
                tie_count += 1
                match = "over"
                break


def error():
    """
    Handles player input safely.
    Keeps asking until a valid empty cell (0–8) is entered.

    💡 LEARNING — try / except:
        'try' runs code that might fail.
        'except ValueError' catches invalid input like letters
        instead of crashing the program.

    """
    try:
        me = input("\n\tEnter the address : ")
    except ValueError:
        pass

    while(True):
        if(me == ""):
            me = input("\nRe-Enter address: ")

        elif(me.isnumeric() == False):
            print("\n Invalid input")
            me = input("\nRe-Enter address: ")

        elif((board[int(me)]).isnumeric() == False or int(me) > 8 or int(me) < 0):
            # Cell already occupied (no longer a digit) or out of range
            print("\n Invalid input")
            me = input("\nRe-Enter address: ")

        else:
            board[int(me)] = "❌"   # valid cell → place player's mark
            break


# ═══════════════════════════════════════════
#  MAIN GAME LOOP — keeps playing until
#  the player decides to quit.
# ═══════════════════════════════════════════
while(True):

    match = "start"
    count = 0

    # ── TOSS ────────────────────────────────
    rand = random.randint(1, 2)
    print("\n\t Let's toss for first Turn\n")

    try:
        choice = int(input("\nEnter your choice 1️⃣ or 2️⃣ : "))
        if(choice != 1 and choice != 2):
            print("\nInvalid choice...⚠️")
            raise ValueError
    except ValueError:
        while True:
            try:
                choice = int(input("\nEnter your choice 1️⃣ or 2️⃣: "))
                if(choice != 1 and choice != 2):
                    print("\nInvalid choice...⚠️")
                    raise ValueError
                break
            except ValueError:
                continue

    if(choice == rand):
        print("\nyou won the toss, have the first choice...")
        result = "win"
    else:
        print("\nyou lost the toss...")
        result = "lose"

    game()   # show the empty board

    # ════════════════════════════════════════
    #  PLAYER GOES FIRST
    # ════════════════════════════════════════
    if(result == "win"):

        print("\n\tHave the first turn...")

        while match != "over":

            if(count > 4 and count < 10):
                results(count)

            if match == "over":
                break

            # ── Player's turn ──
            error()
            game()
            count += 1

            if(count > 4 and count < 10):
                results(count)

            if(match == "over"):
                break

            # ── Computer's turn ──
            comp_random()
            game()
            count += 1

    # ════════════════════════════════════════
    #  COMPUTER GOES FIRST
    # ════════════════════════════════════════
    elif(result != "win"):

        while(match != "over"):

            if(count > 4 and count < 10):
                results(count)

            if(match == "over"):
                break

            # Computer's first move: always pick a corner or center
            f_move = ["0", "2", "4", "6", "8"]
            if(count == 0):
                com = random.choice(f_move)
                board[int(com)] = "⭕"

            # All moves after first use full strategy
            if(count != 0):
                comp_random()

            game()
            count += 1
            

            if(count > 4 and count < 10):
                results(count)

            if(match == "over"):
                break

            # ── Player's turn ──
            error()
            game()
            count += 1

    # ── SCOREBOARD after each match ─────────
    match_count += 1
    print(f"\n Match  = {match_count}")
    print(f"\n Won    = {win_count}")
    print(f"\n Lost   = {lost_count}")
    print(f"\n Tie    = {tie_count}")

    nxt = input("\n Enter yes if you want to continue: ")
    if nxt.lower() != "yes":
        print("Thank you for playing! 👋")
        break

    reset_board()   # clear the board for the next match