#pop() remove (val)
#del
# lst = [1, 2 ,3 ]
# del lst[0]
# print(lst)

#List funtion /methods 
#append()
#insert()
#remove()
#pop()

# lst = ["2", "5", "6" "-1" ,"9", "-11", "string", "apple" "cherry"]
# lst.sort()
# print(lst)

# lst = [1, 5, 5, 0, True, 8 , False ]
# lst.sort()
# print(lst)

# lst = [1, 5, 5, 0, 4, 8, 45 ]
# print(lst.index(0))

#split()
# str1 = "Hello Worls, this is a test "
# lst_str = str1.split()
# print(lst_str)

# str1 = "Hello:Worls,:this:is:a:test "
# lst_str = str1.split(':')
# print(lst_str)

#split() ---> splits string to a list elemets (default is ' ')
#Strip ->
# str1 = " Hello Worls, this is a test "
# lst_str = str1.split(' ')
# filtred = []
# for word in lst_str: 
#     filtred.append(word.strip())
# print(filtred)


# lst_num = []
# for num in range(1,11):
#     if num % 2 == 0:
#         lst_num.append(num)
# print(lst_num)

# lst_num = [<value to insert> for <interator> in <sequence>]

# lst_num = [num2 for num in range (1,11) for num2 in range(1, 3) ]
# print(lst_num)
# lst_num = [[1, 2] for num in range (1,11)]
# print(lst_num)


# lst_num = [num2 for num in range (1,11) for num2 in range(1, 3) ]

#nestat for loops

# for i in range(1,11):
#     print(f"Run {i}")
#     for j in range(1,6):
        
#         print(j, end=' ')
#     print()
#     print("-----------")

#Diference between mulable and immutable data types

#Mutable --> mutate -- change it's contest. It can change
#List --> append(), pop(), change the order, reverse the list, sort...

# lst = [1, 2, 3, 4] ##immutable
# # immutable data types
# -string, integer,float, booleans

# lst = ["Hello", "there", "word"]
# lst[2] = "akumo"
# print(lst)
# word = "Hello"
# word[-1] = 0
# word = "hello"
# print(word + 'akumo')

#List

#Tuple ## read only 

# tpl = (1,2,3,4)
# # print(type(tpl))
# print(tpl[::-1])
# You can change the value if the list inside of the tuple

# Tuple does have build in funcions but they are read only.
# One of them si index, it can not change the tuple , but it give where the value is located

# tpl = (1, 'Hello', 'there', 'akumo')

# tpl = (1,5,8,2, 0, -24)
# # for num in tpl:
# print(sorted(tpl))

#Dictionaries 
# dictionaries -are key value stores
#sets{1,2,3,4}

# keys must be unique 
# x = {"key": "value", "key2": "value2"}
# print(x)

# x = {1: [1,2,3,4,5,6,7,8,9,10], 2: "value2"}
# print(x[1])

# you need to put a key world in order to access the dictionarie.

dic = {
    1:{"name": "Elsu", "Lastname": "Loda", "doob": "06/23/2003" },
    2:{"name": "Anna", "Lastname": "Ana", "doob": "06/23/2001" },
    3:{"name": "Lisa", "Lastname": "Lisa", "doob": "06/23/2000" }
    }

for key, value in dic.items():
    print(f"Hi my name is {value['name']} {value['Lastname']}. I was born in {value['doob']}")
    print(f"My student number is {key}" )
    

