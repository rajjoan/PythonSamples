# Question 8.

#Suppose you have to go grocery shopping. Create a list for the same with following items-

##a. Eggs

##b. Milk

##c. Bread

##d. Chips

##e. Tomatoes

##f. Ketchup

##Milk and Bread were not available in the store. Remove these items from your list and print the updated list.

#You decide to get a healthier snack instead of chips. Replace 'Chips' with 'Oats'.


grocery = ['eggs','milk','bread','chips','tomatoes','ketchup']
print(grocery)
grocery.pop(1)
grocery.pop(1)
print(grocery)
grocery[1] = "oats"
print(grocery)
