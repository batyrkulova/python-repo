Task1:

inp = input("please enter an input: ").split()
reversed_list = []
for i in reversed(inp):
    if i not in reversed_list:
        reversed_list.append(i)
print(reversed_list)

# # Task 2:
words = input("Enter words: ").split()
duplicate = []
for word in words :
    if word not in duplicate:
        duplicate.append(word)
       
print(duplicate)


Task 3:
inp = input("Please enter words: ").split()
longest = max(inp, key=len)
print(longest)

inp = input("Please enter words: ").split()
longest = ""
for word in inp:
    if len(word) > len(longest):
        longest = word
print(longest)


Task 4:
numbers = list(map(int, input("Enter numbers: ").split()))
larg = 0
secd = 0
for i in numbers: 
    if i > larg:
        secd = larg
        larg = i
    elif i > secd and i != larg:
        secd = i
print(secd)






