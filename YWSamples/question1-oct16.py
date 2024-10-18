#Question 1.
#Generate a list of 15 random integers using the randint function. Print the median of the list.

#Tip: Median is the middle value in a sorted list.

import random
list1 = []

for i in range(15):
    list1.append(random.randint(1,100))

list1.sort()
print(list1[7])
