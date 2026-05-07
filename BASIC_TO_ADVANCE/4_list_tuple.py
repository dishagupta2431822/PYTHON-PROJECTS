friends=["Disha","Anya","Aransh","Harsh"]
print(friends)  #['Disha', 'Anya', 'Aransh', 'Harsh']
print(friends[0])  #Disha
friends[0]="Aranya"  #List are mutable

print(friends)  #['Aranya', 'Anya', 'Aransh', 'Harsh']

#slicing in list
print(friends[1:3])  #['Anya', 'Aransh']

# functions of list
friends.append("Disha")  #add element at the end of the list
print(friends)  #['Aranya', 'Anya', 'Aransh', 'Harsh', 'Disha'] 

print(friends.count("Disha"))  #1 [number of appearance]
friends.sort() #sort the list in ascending order
print(friends)  #['Anya', 'Aransh', 'Aranya', 'Disha', 'Harsh']

friends.reverse() #reverse the list
print(friends)  #['Harsh', 'Disha', 'Aranya', 'Aransh', 'Anya']

friends.insert(5,"Gunnu") #insert element at the given index
print(friends)  #['Harsh', 'Disha', 'Aranya', 'Aransh', 'Anya', 'Gunnu']

friends.remove("Aranya") #remove the given element from the list
print(friends)  #['Harsh', 'Disha', 'Aransh', 'Anya', 'Gunnu']

friends.pop() #remove the last element from the list
print(friends)  #['Harsh', 'Disha', 'Aransh', 'Anya']

#tuple

a=()
print(a)  #()
print(type(a))  #<class 'tuple'>
a=(1,4,"Disha",9.5)
print(type(a))  #<class 'tuple'> can't be changed tuple is immutable

#tuple methods
no=a.count(1)  #count the number of appearance of the given element
print(no)  #1
print(a.index(1))  #0 (index of first occurrence of the given element)  

tup1=(1,2,3)
tup2=("Disha","Anya")
tup3=tup1+tup2  #concatenation of two tuples
print(tup3)  #(1, 2, 3, 'Disha', 'Anya')

tup4=tup1*3  #repetition of the tuple
print(tup4)  #(1, 2, 3, 1, 2, 3, 1, 2, 3)

print(2 in tup1)  #True (membership operator)
print(5 in tup1)  #False (membership operator)
print(len(tup3))  #5 (length of the tuple)
print(max(tup1))  #3 (maximum element in the tuple)
print(min(tup1))  #1 (minimum element in the tuple)

sliced=tup3[3:6]  #slicing of the tuple
print(sliced)  #('Disha', 'Anya')
