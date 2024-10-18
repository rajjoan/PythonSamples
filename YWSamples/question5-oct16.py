# Question 5.
##Create a list of 7 numbers divisible by 8.
##
##i) Add another number divisible by 7 at 4th position and print the new list
##
##ii) Delete the 2nd item and print the new list
##
##iii) Add 5 to all the items of the list and print the new list

list1 = []

for i in range(1,7):
    list1.append(i*8)
print(list1)
list1.insert(3, 49)
print(list1)
list1.pop(1)
print(list1)
for i in range(len(list1)):
    list1[i]=list1[i]+5

print(list1)
