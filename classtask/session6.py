# def greet(name):
#     print("Hello, " + name + "!")

# def welcome():
#     return "welcome"

# print(greet("Alice"))  # Output: Hello, Alice!
# print(welcome())
# Return gives as value as return and print gives us none



# def fun1():
#     city = input("Enter your city: ")
#     return "city"
# def fun2():
#     place = input("your favorite place: ")
#     return "place"

# def fun3(city: str, place: str):
#     return {
#         "city": city, 
#         "place": place
#     }
# city = fun1()
# place = fun2()

# print(fun3(fun1(),fun2()))
    
# def factorial(n):
#     if n == 2:
#         return 2
#     return n * factorial(n - 1)

# print(factorial(3))  # Output: 120

# factorial (5) > fac(4) > fac(3) > fac(2) > fac(1)
# 5 * 4 * 3 * 2 * 1


# def fibo(n):
#     count = 1
#     while count <= n:
#         count += (n)
#     return fibo(n)

# print(fibo(5))


# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibo(n - 1) + fibo(n - 2) 
# print(fibo(7))
# print([fibo(n) for n in range(7)])

# try:
#     num = int(input("please enter a number: "))
#     print(10 / num)
# except ValueError:
#     print("Enter a valid integer")
# except ZeroDivisionError:
#     print("Enter a different number rather then 0 ")

dic = {
    "elsu": 100,
    "sam": 45,
    "kat": 89,
    "lisa": 90
}

inp = input("Please enter a sudent name: ")
try: 
    if inp in dic:
        print(dic[inp])
except:
    print("The name if not in the list")

def students(dic):
    inp = input("Please enter a sudent name: ")
    try: 
        return(dic[inp])
    except KeyError:
        return("The name is not in the list")

print(students(dic))


    
    





