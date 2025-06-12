# for loop until 5
# print 

#Interetor is a variable used within loop the value of which changes based on the sequence 
# sequence_data type is the data type that has start point and end point
#string indexing. though indexing we can get the start of the string and the end of the stirng  
# for <Interetor> in <sequence_data type>:
#     <code that needs to be repeated>
#I n p u t 
# inp = input("Input: ")
# for char in inp:
#     print(char)

# inp1 = input("Input a word: ")
# inp2 = input("Input a character: ")

# for char in inp1:
#     if char == inp2: 
#         print(char)

# inp1 = input("Input a word: ")
# inp2 = input("Input a character: ")
# counter = 0

# for char in inp1:
#     if char == inp2: 
#         counter += 1 

# print(counter)
#range(start, end, jump) start:end:jump

# for num in range(1,11,2):
#     print(num)

#Input: 15 

# inp = int(input("Input"))
# for num in range(inp):
#     if num % 2 == 0:
#         print(num)
# range only works with integer 
# int(range(10))
# for loop has iterator 
# for iterats though sequence_data types from start to end 

#while loop
#unlike for loop,while loop doesn't not have a start or end 
#while loop is based on condition

#if the condition is true code will be repeated untill it turns false

# while <condition>: num1 > num2 
#     code

# inp1 = int(input("Input: "))
# num = 0 

# while  num < inp1:
#     print(num)
#     num +=0


#break / continue - used with loops only 
#break stops the loop 

# for num in range(4):
#     for i in range(1, 10):
#         if i == 5:
#             break
#         else:
#             print(i)
#     print("-------")

#continue - skips the input
# for i in range(1, 10):
#     if i == 5:
#         continue
#     else:
#             print(i)

# while  num < inp1:
#     print(num)
#     num +=0

# inp1 = int(input("Until what number to count: "))
# inp2 = int(input("Wehre to break: "))


# if inp1 < inp2 :
#     print(" Out of range ")
# else:
#     num = 0
#     while num < inp1:
#         if inp2 == num: 
#             break 
#         print(num)
#         num += 1

#Lists | Tuple | Dictionaries | Sets --> Data types that can hold o  or more values.

# strings, float, integers, booleans  ----> they can onlu hold single value 
# int =10
# float =10.0
# booleans = True | false
# string = "Hello"  

#List is a datatype that can hold 0 or more values , you can store any data types in list 
#List starts with [] 
# list = ["Hello","World", 10 ,20.5, "test"  ]   
# # print(list[5])
# # print(list[-1][-1])
# print(list[1][2])
# #append funtion adds elements at the end of the list 
# lst_fruits = ["pinaple", "pear", "apricot", "peach"]
# # for fruit in lst_fruits: 
# #     print(f"Fruit: {fruit}")
# # lst_fruits.append('apple')
# # lst_fruits.append('kiwi')

# #insert 
# # lst_fruit.insert(location , element)
# lst_fruits.insert(2, 'apple')
# print(lst_fruits)

# lst_fruits = ["pinaple", "pear", "apricot", "peach"]
# lst_fruits.pop(1)
# # lst_fruits.remove('pear')
# print(lst_fruits)
# OVERWRITE 
# lst_fruits[0] = lst_fruits[-1]
# print(lst_fruits)

# x ,y = 10,15 
# print(x, y)


# char = input("Please enter a character: ")
# lst_fruits = ["pinaple", "pear", "kiwi", "apricot","peach", "pear", "cherry", "melon" ]
# count = 0 
# for fruit in lst_fruits: 
#     if char in fruit:
#         print(fruit)
#     else:
#         count +=1
# if count == len(lst_fruits):
#     print("No fruits")
    










