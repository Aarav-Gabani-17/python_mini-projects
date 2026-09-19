# ============================================================
#                     📒 CONTACT DIARY
#         A simple CLI-based phonebook manager in Python
# ============================================================

# 📦 Pre-loaded contacts dictionary  →  { name : number }
contact = {
    "aarav gabani"  : "1234567890",
    "om mangukiya"  : "1122334455",
    "alex shah"     : "6677889900"
}


# ──────────────────────────────────────────────────────────────
# 🔒 VALIDATOR : Ensures the entered number is exactly 10 digits,
#               doesn't start with 0, and contains only digits.
# ──────────────────────────────────────────────────────────────
def digits_error():

    number = input("\n Enter contact : ")

    while(True):
        if(len(number) != 10):                    # ❌ Must be 10 digits
            print("\nInvalid number...⚠️")
            number = input("\nRe-Enter contact : ")

        elif(number.startswith("0")):             # ❌ Cannot start with 0
            print("\nInvalid number...⚠️")
            number = input("\nRe-Enter contact : ")

        elif(number.isnumeric() == False):        # ❌ Must contain only digits
            print("\nInvalid number...⚠️")
            number = input("\nRe-Enter contact : ")

        else:                                     # ✅ Valid number — return it
            return number
            


# ──────────────────────────────────────────────────────────────
# 📋 MENU : Displays the main options to the user
# ──────────────────────────────────────────────────────────────
def menu():
    print("\n1️⃣  ADD NAME & CONTACT ")
    print("2️⃣  FIND NAME & CONTACT ")
    print("3️⃣  CHANGE NAME & CONTACT")
    print("4️⃣  ALL CONTACTS ")
    print("5️⃣  DELETE CONTACT ")


# ──────────────────────────────────────────────────────────────
# 🎯 SELECT : Reads and validates the user's menu choice (1–5)
# ──────────────────────────────────────────────────────────────
def select():
    global choice                                 # 'choice' is used across functions

    try:
        choice = int(input("\nEnter choice : "))
        if(choice > 5 or choice < 1):            # Out-of-range → force re-entry
            print("\n\tInvalid choice...⚠️")
            raise ValueError
    except:
        while(True):
            choice = int(input("\nRe-Enter choice : "))
            if(choice <= 5 and choice >= 1):     # ✅ Valid range — exit loop
                break
            else:
                print("\n\tInvalid choice...⚠️")


# ──────────────────────────────────────────────────────────────
# ➕ ADD CONTACT : Takes first + last name and a valid number,
#                 then inserts the new entry into the dictionary.
# ──────────────────────────────────────────────────────────────
def add_contact():

    f_name = input("\n Enter first name : ")
    l_name = input("\n Enter last name : ")
    cont   = digits_error()                       # Validate the phone number

    name = f_name + " " + l_name                 # Combine into full name
    contact.update({name : cont})                 # Add/update entry in dict
    print("contact saved successfully...")

# ──────────────────────────────────────────────────────────────
# 🔍 FIND : Search a contact either by name or by number
# ──────────────────────────────────────────────────────────────
def find():

    print("\n\t1️⃣ Find by name...")
    print("\t2️⃣ Find by contact...")

    # --- Validate sub-choice ---
    try:
        find_choice = int(input("\nEnter choice : "))
        if(find_choice > 2 or find_choice < 1):
            print("\n\tInvalid choice...⚠️")
            raise ValueError
    except:
        while(True):
            find_choice = int(input("\nRe-Enter choice : "))
            if(find_choice == 2 or find_choice == 1):  # ✅ Only 1 or 2 allowed
                break
            else:
                print("\n\tInvalid choice...⚠️")

    # --- Search by NAME ---
    if(find_choice == 1):
        f_name = input("\n Enter first name : ")
        l_name = input("\n Enter last name : ")
        name   = f_name + " " + l_name

        try:
            # data available before error raise then print Data available and the data not found
            print(f"\n\t • Data available \n📋 {name} : {contact[name]} ")  # KeyError if not found
        except:
            print("\n Data not found⚠️")

    # --- Search by NUMBER ---
    elif(find_choice == 2):
        search = digits_error()                   # Get + validate number

        # ☠️  'name' and 'cont' here are loop variables (like 'i' in range())
        # ☠️  Don't reuse 'search' as the loop variable — it would get overwritten
        for name, cont in contact.items():
            if(cont == search):
                print(f"\n {name} : {search}")
                # 🔰 Prints only the matching entry, not the whole dict


# ──────────────────────────────────────────────────────────────
# ✏️  CHANGE : Update name, number, or both for an existing entry.
#             Keeps asking for a name until a match is found.
# ──────────────────────────────────────────────────────────────
def change():

    data_change = "exist"

    # Loop until a valid existing contact is found
    while(data_change == "exist"):
        print("\n\tPlease enter existing data...")
        search_f_name = input("\n Enter first name : ")
        search_l_name = input("\n Enter last name : ")
        search_name   = search_f_name + " " + search_l_name

        for name, cont in contact.items():
            if(search_name == name):             # ✅ Match found
                print(f"\n{name} : {cont}")
                print("\n\t1️⃣ Change name...")
                print("\t2️⃣ Change contact...")
                print("\t3️⃣ Change both...")
                data_change = "done"             # Exit outer while loop
                break
        else:
            data_change = "exist"               # No match → loop again
            print("Data not available...")

    # --- Validate change sub-choice ---
    try:
        change_choice = int(input("\nEnter choice : "))
        if(change_choice > 3 or change_choice < 1):
            print("\n\tInvalid choice...⚠️")
            raise ValueError
    except:
        while(True):
            change_choice = int(input("\nRe-Enter choice : "))
            if(change_choice <= 3 and change_choice >= 1):  # ✅ Valid
                break
            else:
                print("\n\tInvalid choice...⚠️")

    # --- Change BOTH name and number ---
    if(change_choice == 3):
        new_f_name = input("Enter first name to change with : ")
        new_l_name = input("Enter last name to change with : ")
        new_name   = new_f_name + " " + new_l_name
        new_cont   = digits_error()

        for name, cont in contact.items():
            if(name == search_name):
                del contact[name]                # Remove old entry
                contact.update({new_name : new_cont})  # Add updated entry
                for name, cont in contact.items():
                    print(f"{name} : {cont}")
                break

    # --- Change NUMBER only ---
    if(change_choice == 2):
        new_cont = digits_error()

        for name, cont in contact.items():
            if(name == search_name):
                del contact[name]                # Remove old entry
                contact.update({search_name : new_cont})  # Same name, new number
                for name, cont in contact.items():
                    print(f"{name} : {cont}")
                break

    # --- Change NAME only ---
    if(change_choice == 1):
        new_f_name = input("Enter first name to change with : ")
        new_l_name = input("Enter last name to change with : ")
        new_name   = new_f_name + " " + new_l_name

        for name, cont in contact.items():
            if(name == search_name):
                new_cont = cont                  # Keep existing number
                del contact[name]
                contact.update({new_name : new_cont})  # New name, same number
                for name, cont in contact.items():
                    print(f"{name} : {cont}")
                break


# ──────────────────────────────────────────────────────────────
# 📜 ALL CONTACTS : Prints every name-number pair in the diary
# ──────────────────────────────────────────────────────────────
def all():
    print("\n")
    print("\t CONTACT LIST :-\n")
    for name, cont in contact.items():
        print(f"{name} : {cont}")


# ──────────────────────────────────────────────────────────────
# 🗑️  DELETE : Find a contact by name and remove it after
#              user confirms with 'ok'.
# ──────────────────────────────────────────────────────────────
def delete():

    f_name = input("\n Enter first name : ")
    l_name = input("\n Enter last name : ")
    name   = f_name + " " + l_name

    # --- Check if contact exists ---
    try:
        if name in contact.keys():
            print("\n\t • Data available")
            print(f"\n📋 {name} : {contact[name]} ")
            data = "available"
        else:
            raise ValueError                     # Not found → jump to except
    except:
        print("\n Data not found⚠️")
        data = "unavailable"

    # --- Ask for confirmation before deleting ---
    if(data == "available"):
        delete_choice = input("\nEnter 'ok' to confirm deletion : ")

        if((delete_choice).lower() == "ok"):
            del contact[name]
            print("\n\tDeletion completed...\n")
            for name, cont in contact.items():   # Show remaining contacts
                print(f"{name} : {cont}")
        else:
            print("Deletion is aborted...")


# ============================================================
#  🔁 MAIN LOOP : Keeps the app running until user exits
# ============================================================

loop = "on"

while(loop == "on"):

    menu()      # Show options
    select()    # Get user's choice

    # Route to the correct function based on choice
    if(choice == 1):
        add_contact()
    elif(choice == 2):
        find()
    elif(choice == 3):
        change()
    elif(choice == 4):
        all()
    elif(choice == 5):
        delete()

    # Ask if the user wants to continue
    loop = input("\nIf you want to continue enter 'on' : ")

    if(loop.lower() == "on"):
        pass
    else:
        print("\nThank you...👋")   # Graceful exit message
    