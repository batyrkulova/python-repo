# Task1.
# num = int(input("Please enter a number: "))
# if num < 0 and num % 2 == 0 :
#     print("The number is negative.\nThe nummber is even")
# elif num < 0 and not num % 2 == 0 :
#     print("The nuumber is negative.\nThe number is odd")    
# if num > 0 and num % 2 == 0 :
#     print("The number is positive.\n The number is even ")
# elif num > 0 and not num % 2 == 0 : 
#     print("The number is positive.\nThe number  is odd ")
# elif num == 0 :
#     print("The number is 0")

# Task2
# inp1 = input("Choose between True or False: ")
# inp2 = input("Chose again, True or False: ")

# if inp1 == "True" and inp2 == "True" :
#     print(f"{inp1} and {inp2} = True ")
#     print(f"{inp1} or {inp2} = False ")
#     print(f" not {inp1}= {inp2} ")
# elif inp1 == "True" and inp2 == "False" :
#     print(f"{inp1} and {inp2} = False") 
#     print(f"{inp1} or {inp2} = True ")
#     print(f" not {inp1} = {inp2} ")
# if inp1 == "False" and inp2 == "True" :
#     print(f"{inp1} and {inp2} = False") 
#     print(f"{inp1} or {inp2} = True ")
#     print(f" not {inp1} = {inp2} ")
# elif inp1 == "False" and inp2 == "False" :
#     print(f"{inp1} and {inp2} = False") 
#     print(f"{inp1} or {inp2} = False ")
#     print(f" not {inp1} = True ")
# else:
#   print("Incorrect input")

#Task 3 
# passwd = input("Please enter a password: ")
# if len(f"{passwd}") >=8 and "@" in passwd and " " not in passwd :
#     print("Strong password")
# else :
#     print("Weak password or contains spaces")

# Task 4
# plr1 = input("Player 1, please enter rock, paper or scissors: ")
# plr2 = input("Player 2, please enter rock, paper or scissors: ")
# if plr1 == "rock" and plr2 == "paper" or plr1== "paper" and plr2 == "scissors" :
#     print("Player 2 wins")
# elif plr1 == "paper" and plr2 == "rock" or plr1 == "scissors" and plr2 == "paper" :
#     print("Player 1 wins")
# elif plr1 == "scissors" and plr2 == "rock" :
#     print("Player 2 wins")
# elif plr1 == "rock" and plr2 == "scissors" :
#     print("Player 1 wins")
# elif plr1 == plr2 :
#     print("It's a tie")
# else: 
#     print("Invalid input")


#Task 5
# a, b, c = map(int, input("Enter three integers separated by spaces: ").split())
# if a + b <= c or b + c <= a or c + a <= b : 
#     print("This is not a triangle ")
# elif a == b and b == c :
#     print(" Equilateral triangle")
# elif a == b or b == c :
#     print("Isosceles triangle")
# elif a != b and b != c :
#     print("Scalene triangle")


