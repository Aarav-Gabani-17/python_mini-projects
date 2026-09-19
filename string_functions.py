   # string is imutable that means we can't change in existing string 

a="aarav"
b="GABANI"
c="my name is gabani aarav"
d=c.title()

     #  case convertion 

print(a.capitalize())
print(c.title())
print(a.upper())
print(b.lower())
print(d.swapcase())

     # searching & finding 
     
print("you have leave the space",c.find(" "),"times")      
print(f"you have leave the space {c.find(" ")} times")  #f(you can directly write string and variable in "" but type variable in {}) 
print(f"index of is = {c.index("is")}")  
print(f"ocurrance of a = {c.count("a")}")
print(a.endswith("rav"))
print(a.startswith("aaa"))

     #  replace 
     
print(c.replace("aarav","kiya"))     

     #  cheking of string 
     
"hello".isalpha()    # True  (only letters)
"123".isdigit()      # True  (only digits)
"abc123".isalnum()   # True  (letters + digits)
"   ".isspace()      # True  (only spaces)
"Hello".istitle()    # True  (title case)
"HELLO".isupper()    # True
"hello".islower()    # True

     #  Padding & Alignment

print("hi".center(10),"=> function work")       # "    hi    "
print("hi".ljust(10, " "),"=> function put it left side")    # "hi       "
print("hi".rjust(10, "+"),"=> function put it right side")   # "++++++++hi"
print("ab".zfill(3),"       => fill front side with 0")          # "00042"

      # slicing 
      
 """
(0)(1)(2)(3)(4)(5) 
 0  1  2  3  4  5    :index(+)
-6 -5 -4 -3 -2 -1    :index(-)
"""
s = "012345"

s[2]      # '2'   → index 2
s[1:4]    # '123' → index 1,2,3 (4 excluded)
s[:3]     # '012'  → from beginning to index 3
s[3:]     # '345'  → from index 3 to end
s[:]      # '012345' → full string (copy)
s[-3:]    # '34' → last 2 chars
s[:-2]    # '0123'→ remove last 2


s[::2]    # '024'  → every 2nd char
s[::3]    # '03'   → every 3rd char
s[1::2]   # '135'  → start at 1, every 2nd
s[0:5:2]  # '024'  → index 0 to 5, step 2

 """
(0)(1)(2)(3)(4)(5) 
 0  1  2  3  4  5    :index(+)
-6 -5 -4 -3 -2 -1    :index(-)
"""

s[::-1]   # '543210' → full reverse          "most important"
s[4:1:-1] # '432'    → reverse from 4 to 2
s[::-2]   # '531'    → reverse, every 2nd