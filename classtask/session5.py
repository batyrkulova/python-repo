# Dictiniory is the data type that can hold multiple key value pairs. 
# It's mutuble data type
#mutable -list,dict
#imutable- string, integer, float, tuple, bolean.

#create a dict structure for laptop

# laptop = {
#     "Dell": {
#         "software": {
#             "os": "Linux Mint",
#             "version": "22.04",
#             "applications": ["python", "vscode", "slack"]
#         },

#         "hardware": {
#             "model": "XPS 15",
#             "cpu": "Inter Core i5, (6 cores)",
#             "ram": "8gb",
#             "storage": "256gb",
#             "screen": "ips"
#         }
#     },

#     "MacBook": {
#         "software": {
#             "os": "Mac OS",
#             "version": "Sequoia 15.01",
#             "applications": ["telegram", "slack", "ms teams"]
#         },

#         "hardware": {
#             "model": "macbook air",
#             "cpu": "M1 8(cores)",
#             "ram": "8gb",
#             "storage": "512gb",
#             "screen": "ips"
#         }
#     },

#     "Acer": {
#         "software": {
#             "os": "Linux Ubuntu",
#             "version": "22.04",
#             "applications": ["python", "nodejs", "slack"]
#         },

#         "hardware": {
#             "model": "Swift 16",
#             "cpu": "Inter Core i9, (16 cores)",
#             "ram": "32gb",
#             "storage": "1tb",
#             "screen": "oled"
#         }
#     }
# }

#Task1.
#Get all the laptop names

# new = []
# for key,value in laptop.items(): 
#     if key not in new:
#         new.append(key)
# print(new)

#Task2

#print all the specs in the software

# for key,value in laptop.items():
#     print(key)
#     print(value["software"]["os"])
#     print(value["software"]["version"])
#     print()



# Task 3
# for key , value in laptop.items():
#     print(key)
#     for app in value['software']['application']:
#         print(app)


# fruits = {"banana":2, "apple":1, "pear":3}
# fruits["kiwi"] = 6
# fruits.pop("apple")
# print(fruits)

# var = {"key": "value"} -Dictiniory
# Sets are mutable, and stores only values

# sets = {"value1", "value2" }
# print(type(sets))


#Functions 
# function is a block of reusble code
# What is return? Is a keyword that is used only in fuctionst
#return is used to output a data type
#What is the difference between print and return? 


# def greet(name):
#     return(f"Hello, {name}")
# inp = input("What is your name: ")
# print(greet(inp))

from session6 import students

dic = {
    "elsu": 100,
    "sam": 45,
    "kat": 89,
    "lisa": 90
}

print(students(dic))

