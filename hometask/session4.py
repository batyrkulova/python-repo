students = {"Alice": 45, "Bob": 78, "Charlie": 52, "David": 33}
tar = 50
for key, value in students.items():
    if value >= tar :
        print(key,value)


inp = input("Enter a word: ")
def sliced(inp):
    new = {}
    for ch in inp:
        if ch in new:
            new[ch] += 1
        else:
            new[ch] = 1
    return new
print(sliced(inp))    




dict1 = {"apple": 3, "banana": 5, "orange": 2}
dict2 = {"banana": 2, "orange": 4, "grape": 6}
for key,value in dict1.items():
    if key not in dict2:
        print(key,value, "#Only in dic1:" )
    if key in dict1 and key in dict2:
        dict2[key] += value
        print(key, dict2[key], f"# {dict1.get(key)} (from dict1)  {dict2.get(key)} (from dict2)")
for key,value in dict2.items():
    if key not in dict1:
        print(key,value, "#Only in dict2")
