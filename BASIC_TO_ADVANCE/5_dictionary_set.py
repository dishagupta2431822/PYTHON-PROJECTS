d={}  #empty dictionary
print(d,type(d))

marks={
    "Disha":90,
    "Harsh":95,
    "Anya":99,
    "Aransh":99
}

print(marks,type(marks))
print(marks["Disha"])


# funtions of dictionary

print(len(marks))  #gives the number of key value pairs in the dictionary
print(marks.keys())
print(type(marks.keys())) #gives only keys in dict_keys

print(marks.values())
print(type(marks.values()))  #gives only values in dict_values

print(marks.items())
print(type(marks.items()))  #gives key value pair in dict_items

marks.update({"Disha":100})   #update the value of key Disha to 100
marks.update({"Disha1":100})  #add new key Disha1 with value 100
marks.update({"Disha5":100})  #add new key Disha5 with value 100
print(marks)    

print(marks.get("Disha"))
print(marks.get("Disha2")) # it will return none if key is not present
marks.pop("Disha1")  # it will remove the key Disha1 and its value
print(marks)

marks.popitem()  # it will remove the last key value pair
print(marks)

marks.clear()  # it will remove all the key value pairs
print(marks)    


#sets
s={1,2,3,4,5,"Disha"}
print(s,type(s))

e=set()  #empty set
print(e,type(e))

# function of set

print(len(s))  #gives the number of elements in the set

s.add(6)  # it will add 6 to the set
print(s)

s.remove(3)  # it will remove 3 from the set
print(s)

s.discard(4)  # it will remove 4 from the set
print(s)

s.discard(10)  # it will not give error if 10 is not present in the set
print(s)

s.pop()  # it will remove a random element from the set
print(s)

s.clear()  # it will remove all the elements from the set
print(s)

# operation in 
s1={1,2,3,4,5}
s2={"Disha","Harsh","Anya","Aransh"}
print(s1.union(s2))  # new set of union of s1 and s2

print(s1.intersection(s2))  # new set of intersection of s1 and s2

print(s1.difference(s2))  # new set of difference of s1 and s2

print(s1.symmetric_difference(s2))  # new set of symmetric difference of s1 and s2

print(s1.issubset(s2))  # True if s1 is a subset of s2

print(s1.issuperset(s2))  # True if s1 is a superset of s2

print(s1.isdisjoint(s2))  #True if s1 and s2 have no common elements    

s3=s1-s2  # new set of difference of s1 and s2
print(s3)

s4=s1&s2  # new set of intersection of s1 and s2
print(s4)

s5=s1|s2  # new set of union of s1 and s2
print(s5)

s6=s1^s2  # new set of symmetric difference of s1 and s2
print(s6)


