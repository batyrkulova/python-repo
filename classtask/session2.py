#Numeric Data Types
#Binary
# Binary are 0 and 1 
# Binary representation of a number in python is 0b;
# bin function translates from decimal binary 
# print(0b010101)
# print(bin(21))
#Hexadecimal 
# hexadecimal = 16 0x (0-9) (a-f)
# hex function translates from decimal to hex
# print(0x123fd3)
# print(hex(100))
#Octal 
#octal 8 0-7 Oo
# print(0o4361)
# print(oct(35))

#variable conventions (best practices)
#snake_casing, camelCasing 
#last_name --> snake_casing
# lastName ---> camelCalsing

# Python always uses snake_casing
# regular_variable = "Hello"
# _hidden_var
# __hidden_var_extra 

### Booleans
# Booleans is the data type 
# Boolean has 2 states : True or False
#Boolean operaters 
# my_var = True
# my_var2 = False

# and, or , not

#and operaror is used to connect 2  boolean to form a single decision 
# False is a prioraty in and condition

# print(True and True ) ## True and true --. true
# print(True and False) ## True and False--> False
# print( False and False) ## False

# or operators is used to connect 2 boolean to form a signle a decision. True is a priority 
# print(True or True ) ## True and true --. true
# print(True or False) ## True and False--> true 
# print( False or False) ## False

#not operators - used to return the oposite of the boolean 
# print(not True) #False
# print(not False)#True
# There is a priority, and goes first

#if <condition1> or/end <condition2>

#Comperesion operators
#All of the comperesion operators return Boolean Data Type
# <Less than
#>greater than
#<=less then or equal
#>= greater then or equal

# if always takes boolean data type 
# if condition always runs when the final decision is True 
# if <condition> and <condition>:
#     #indentation = tab 
#     #code 
# if <condition>:
#     <indentation>
#     <code>

# elif <condition>
#     indentation = tab
#     code
#     if condition
#     indentation
#     code 
# else: 
#     indentation
#     code 

# fsting 
# var = input("Provide 1 word: ")
# var1 = input("Provide 2 word: ")
# if len(var) > len(var1): 
#     print(f"Word {var} is longer " )
# elif len(var) < len(var1):
#     print(f"Word {var1} has more characters")
# else:
#     print(" They are equal")

# num = int(input("Please provide a number: "))
# if num < 60:
#     print("F")
# elif num >= 60 and num < 70 :
#         print("D")
# elif num >=70 and num < 80 :
#     print("C")
# elif num>=80 and num < 90 : 
#     print("B")
# else:
#     print("A")

# year = int(input("Please provide a year: "))

# if year % 100 ==0 and year % 4 ==0:
#     print("It's not a leap year")
# elif year % 4 ==0 or year % 400 ==0 :
#     print("It's a leap year and divisble")
# else:
#     print("Its not a leap year ")

# inp = input("First Boolean: ")
# inp2 = input("Sesond Boolean: ")

# bool1= False
# bool2 = False
# if inp == 'True': 
#     bool1 = True
# else:
#     bool1 = False

# if inp == 'True': 
#     bool2 = True
# else:
#     bool2 = False
# print(f"{inp} and {inp2} == {bool2 and bool2}")
# print(f"{inp} or {inp2} == {bool2 and bool2}")
# print(f"{inp} and not {inp2} == {bool2 and bool2}")
    
