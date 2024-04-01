##create a list using constructor
mylist = list(("Avi","Negi","Omen","Ghost","Tokito"))
# print(type(mylist))

##acess items of list
# for i in mylist:
#     print(i)

##for all elements of list
#print(mylist)

##for particular element of list
#print(mylist[-2])

##access the items using range
#print(mylist[-4:-1])

##insertion/add in list 
# mylist.append("cypher") # add at last
# print(mylist)
# mylist.insert(3,"Blaze") # add at specific position
# print(mylist)

##to merge 2 lists
#lists = ["Ghost","Soap","Price"]
# mylist.extend(lists)
# print(mylist)

##deleting item from list
# mylist.remove("Negi")
# print(mylist)
# mylist.pop(1) # remove particular item
#print(mylist)

##check the given element is present or not in the list
# if"Avi" in mylist:
#     print("Avi is here")
# else:
#     print("Avi is not here")

##change/update element using indexing
# mylist[0] = "Avi Negi" 
# print(mylist)

##sorting the list
# mylist.sort(reverse=True) # sort in descending order
# print(mylist)

# mylist.sort() # sort in ascending order
# print(mylist)

mylist.clear() # clear all elements of list
print(mylist)
