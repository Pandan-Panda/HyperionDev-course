#Task 12 Lists

#Creating a list
string_list = ["Tighnari","Kaveh", "Alhaitham", "Cyno"]
#Indexing a list
pet_list = ["cat", "dog", "hamster", "goldfish"]
print(pet_list[0])
#slicing a list
num_list = [1, 2, 3, 4, 5]
print(num_list[1:2])
#changing an element in a list
string_list[2] = "Nilou"
#adding an element to a list
string_list.append("Candace")
#deleting an element from a list
del string_list[4]

#copy() and deepcopy()
import copy
a = [[1,2,3], [4,5,6]]
b=a[:]
c= copy.deepcopy(a)
d= copy.copy(a)    
b[0][1] = 10      #changes position [0][1] in both a and b
c[1][1] = 12
print(a)
print(b)
print(c)
print(d)