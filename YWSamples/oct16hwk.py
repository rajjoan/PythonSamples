#october 16
# question 1 

##import random
##list1 = []
##
##for i in range(15):
##    list1.append(random.randint(1,100))
##
##list1.sort()
##print(list1[7])

## question 2

##namelist = []
##weightlist = []
##while True:
##    name = input("enter your name : ")
##    weight = int(input("enter your weight in pounds : "))
##    namelist.append(name)
##    weightlist.append(weight)
##    tocontinue = input("Do you want to continue : ")
##    if tocontinue == "no":
##        break
##for i in range(len(weightlist)):
##    weightlist[i]=weightlist[i]+10
##namelist.pop(-1)
##weightlist.pop(-1)
##
##print(weightlist)

# question 3

##usernames = ["rebecca_10","juliet.3_4","cookies123","j.a_c.k","addison.1987"]
##
##while True:
##    new_username = input("Add new username : ")
##    if new_username in usernames:
##        print("The username you entered already exists")
##    else:
##        usernames.append(new_username)
##    remove_username = input("Do you want to remove your username : ")
##    if remove_username == "yes":
##        usernames.remove(new_username)
##
##    tocontinue = input("Do you still want to continue : ")
##    if tocontinue == "no":
##        break
##
##print(usernames)


# question 4

##student_marks = [98, 76, 88, 92, 90, 83, 77, 95, 89, 100]
##
##total_value = 0
##
##for i in range(len(student_marks)):
##    total_value = total_value + student_marks[i]
##
##
##
##print(total_value/len(student_marks))


# Question 5.
##Create a list of 7 numbers divisible by 8.
##
##i) Add another number divisible by 7 at 4th position and print the new list
##
##ii) Delete the 2nd item and print the new list
####
####iii) Add 5 to all the items of the list and print the new list
##
##
##list1 = []
##
##for i in range(1,7):
##    list1.append(i*8)
##print(list1)
##list1.insert(3, 49)
##print(list1)
##list1.pop(1)
##print(list1)
##for i in range(len(list1)):
##    list1[i]=list1[i]+5
##
##print(list1)



##
### Question 6.
##
##list1 = []
##list1[0]=9
##print(list1)

 
            
##  questions 7

##library = ['Wings of Fire', "Harry Potter", "Harry Potter", "To Kill a Mocking Bird", "Animal Farm"]
##
##while True:
##    ask = input("Enter a name for donating a book : ")
##    if ask not in library:
##        print("")

# question 8
##
##grocery = ['eggs','milk','bread','chips','tomatoes','ketchup']
##print(grocery)
##grocery.pop(1)
##grocery.pop(1)
##print(grocery)
##grocery[1] = "oats"
##print(grocery)











