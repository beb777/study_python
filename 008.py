print('____________________________________')
# list
natural_number = [1, 2, 9, 2, 3, 56, 2, 5]
print(natural_number[0])
print(natural_number[1])
print(natural_number[2])
#..... until end of the index 
number_copy = natural_number.copy()
print(number_copy)
print(natural_number[0])# print index 0
print(natural_number[-1])#last index
print(natural_number.insert(3,12))# index then value to add a new list 12 is the new number
#print(natural_number[7])# index out of range
# method of list
#natural_number.sort()
#natural_number .reverse()
natural_number.append(11)# insert a list at the end
natural_number.pop()# remove the last
print(len(natural_number))
print(natural_number)
print(8 in natural_number)# to check a number in the list(existance)
print(9 in natural_number)
#natural_number.remove(1)# remove the first index
print(natural_number.remove(1))
print(natural_number.count(2))# count how many 2 are in the list
del natural_number[0:6]# removing
print(natural_number)

print('____________________________________')



print('____________________________________')