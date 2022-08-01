myList = []
for i in range(10):
    myList.append(i)
print("Created list is :")
print(myList)

myList.append("alohomora")
print("Appneding a string to end of list:")
print(myList)

myList.insert(0, "insert")
print("Using insert function in List, the new list is:")
print(myList)

print("Resersing a list:")
print(myList[::-1])

myList.remove(2)
print("Removing item from list:")
print(myList)

anotherList =['a', 'b', 'c']
myList.extend(anotherList)
print("entending the list with another list:")
print(myList)

print("length of list is:")
print(len(myList))

print("First item in list is:")
print(myList[0])

print("list in a list:")
myList.insert(0, [11,22,33])
print(myList)