#    expenses tracker

# This is a "dict inside a dict" (a nested dictionary).
# The outer dict has category names as keys (food, transport, etc.)
# Each of those keys holds ANOTHER dict as its value.
# That inner dict will store: expense_name -> list of prices
# Example after some entries: {"food": {"pizza": [300, 250], "milk": [40]}}
dictionary_collection = {
    "food": {},
    "transport": {},
    "education": {},
    "shopping": {},
    "entertainment": {},
    "bills": {},
    "health": {},
    "gifts": {},
    "personal": {}
}

def menu():
     print("\n")   
     print("0) Exit")
     print("1) Add expenses")
     print("2) Check all expenses")
     print("3) check categorywise expenses")
     print("\n") 
     list_choice=input("\tEnter choice : ")
     print("\n") 
     return list_choice

def add_expenses():

     print("\n1) 🍔 Food — breakfast, lunch, snacks, restaurants")
     print("2) 🚌 Transport — bus, auto, fuel, train")
     print("3) 🛍️ Shopping — clothes, accessories, general purchases")
     print("4) 📚 Education — books, stationery, courses ")
     print("5) 🎬 Entertainment — movies, games, outings") 
     print("6) 🏠 Bills — electricity, internet, mobile recharge")
     print("7) 💊 Health — medicines, doctor visits")
     print("8) 🎁 Gifts — gifts for friends/family")
     print("9) 💰 Personal — miscellaneous personal spending\n")
     purchase_type=input("\nEnter purchase category name : ")
     purchase_type=purchase_type.lower()

     
     try:
         purchase=input("\nEnter expense name : ")
         price=int(input("\nEnter expense : "))
         if(price<=0):
                  raise ValueError   
     except ValueError:
         print("\nInvalid amount...")
         while(True):
           try:
               price=int(input("\nRe-Enter expense : "))
               if(price<=0):
                  raise ValueError
               else: 
                  x="done"   
           except ValueError:
               print("\nInvalid amount...") 
               x="repeat"  
           if(x=="done"):
               break

     if purchase_type in dictionary_collection.keys():

                # here we're checking the INNER dict (dictionary_collection[purchase_type])
                # to see if this exact expense name was already added before

                if purchase in dictionary_collection[purchase_type].keys():
                        dictionary_collection[purchase_type][purchase].append(price)
                else:
                        dictionary_collection[purchase_type].update({purchase : [price]})        
     else:
                print("category not found...")

     
def check_expenses():

        # total_sum and sum_collection are NOT defined inside this function.
        # they're created in the main while loop below (outside any function)
        # and this function just reads them. Python allows this because
        # they're treated as "global" variables here.

        print(f"\n\tYour total expenses(in rupees) = {total_sum}\n")
        for name1,total1 in sum_collection.items():
                if(total1!=0):
                    name1=name1[:-4]    
                    print(f"{name1} : {total1}\n")

                    for name2,total2 in dictionary_collection[name1].items():
                        print(f"\t{name2} : {total2}")


def categorywise():
     print("\n1) 🍔 Food — breakfast, lunch, snacks, restaurants")
     print("2) 🚌 Transport — bus, auto, fuel, train")
     print("3) 🛍️ Shopping — clothes, accessories, general purchases")
     print("4) 📚 Education — books, stationery, courses ")
     print("5) 🎬 Entertainment — movies, games, outings") 
     print("6) 🏠 Bills & Utilities — electricity, internet, mobile recharge")
     print("7) 💊 Health — medicines, doctor visits")
     print("8) 🎁 Gifts — gifts for friends/family")
     print("9) 💰 Personal — miscellaneous personal spending\n")               
     cat_choice=input("Enter category name: ")

     # NOTE: the "else" below belongs to the "for" loop, not to the "if".
     # This is a lesser-known Python feature called a for-else: the else
     # block runs once the for loop finishes, UNLESS the loop hit a "break".
     # Since there's no "break" anywhere in this loop, this else will
     # ALWAYS run after the loop ends, even when a match WAS found above.
     # That's why "Data doesn't exist..." can print even after showing
     # correct data — worth fixing with a break inside the if, or an
     # "if/else" instead of "for/else" if you want to look into it later.
     for name1,total1 in dictionary_collection.items():
          if(name1==cat_choice):
                print(f"\n\t{name1 :- }\n")
                for name2,total2 in dictionary_collection[name1].items():
                        print(f"{name2} : {total2}")
     else:
        print("Data doesn`t exist...")                    
                               

                         
list_choice="start"
while(list_choice!="0"):

     food_sum=0
     transport_sum = 0
     education_sum=0
     entertainment_sum=0
     shopping_sum=0
     bills_sum=0
     health_sum=0
     gifts_sum=0
     personal_sum=0

     # for each category, we loop through the inner dict's VALUES
     # (each value is a list of prices, e.g. [300, 250]) and add up
     # every list into one running total using sum()
     for prices in dictionary_collection["transport"].values():
           transport_sum += sum(prices)
     for prices in dictionary_collection["food"].values():
           food_sum += sum(prices)      
     for prices in dictionary_collection["education"].values():
           education_sum += sum(prices)      
     for prices in dictionary_collection["entertainment"].values():
           entertainment_sum += sum(prices)     
     for prices in dictionary_collection["shopping"].values():
           shopping_sum += sum(prices) 
     for prices in dictionary_collection["bills"].values():
           bills_sum += sum(prices)  
     for prices in dictionary_collection["health"].values():
           health_sum += sum(prices) 
     for prices in dictionary_collection["gifts"].values():
           gifts_sum += sum(prices)  
     for prices in dictionary_collection["personal"].values():
           personal_sum += sum(prices)                                           
     total_sum = personal_sum+gifts_sum+health_sum+bills_sum+entertainment_sum+shopping_sum+education_sum+transport_sum+food_sum    

     # another dict here: just a simple lookup table mapping
     # "category_sum" -> the total number we just calculated above.
     # This is NOT nested (values are plain numbers, not dicts/lists),
     # it's only here so check_expenses() can loop through all totals easily.
     sum_collection={
           "transport_sum" : transport_sum,
           "food_sum" : food_sum, 
           "education_sum" : education_sum, 
           "entertainment_sum" : entertainment_sum, 
           "shopping_sum" : shopping_sum, 
           "bills_sum" : bills_sum,
           "health_sum" : health_sum,
           "gifts_sum" : gifts_sum,
           "personal_sum" : personal_sum,               
     }

     list_choice=menu()
     if(list_choice=="0"):
          print("\n\tThank you for use...")
          break
     elif(list_choice=="1"):
           add_expenses()
     elif(list_choice=="2"):
           check_expenses()       
     elif(list_choice=="3"):
           categorywise()