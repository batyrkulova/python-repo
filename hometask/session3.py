#Task1

# inp = input("please enter an input: ").split()
# reversed_list = []
# for i in reversed(inp):
#     if i not in reversed_list:
#         reversed_list.append(i)
# print(reversed_list)

# # # Task 2.
# words = input("Enter words: ").split()
# duplicate = []
# for word in words :
#     if word not in duplicate:
#         duplicate.append(word)
       
# print(duplicate)






# Task 3.
# inp = input("Please enter words: ").split()
# longest = max(inp, key=len)
# print(longest)

# inp = input("Please enter words: ").split()
# longest = ""
# for word in inp:
#     if len(word) > len(longest):
#         longest = word
# print(longest)


# Task 4: Find the Second Largest Number in a List (No max() or sort())
# Ask the user to enter a list of numbers. Find and print the second largest number without using max() or sort().

# Example:
# Enter numbers: 10 45 78 23 89 56  
# Second largest number: 78


# numbers = list(map(int, input("Enter numbers: ").split()))
# larg = 1
# secd = 1
# for i in numbers: 
#     if i > larg:
#         secd = larg
#         larg = i
#     elif i > secd and i != larg:
#         secd = i
# print(secd)






