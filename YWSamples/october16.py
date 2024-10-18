##vowels = 'Hello how are you'
##
##split = vowels.split()
##split1 = list(vowels)
##print(split)
##print(split1)
##
##
##
##today = ['10','16','2024']
##
##joined = "-".join(today)
##print(joined)


##password = 'nike'
##wrong_passwords = []
##codename = ""
##attempt = 0
##
##while codename !='nike':
##    codename = input("Enter the code name : ")
##    if codename != password:
##        print("Access Denied")
##        wrong_passwords.append(codename)
##        attempt = attempt + 1
##        if attempt == 3:
##            print("Access Denied. Too many failed attempts.")
##            break
##    else:
##        print('Access Granted')
##
##print("wrong passwords tried: ", wrong_passwords)



##import random
##list_random = []
##
##for i in range(20):
##    list_random.append(random.randint(1,100))
##
##
##print(list_random)
##print("max" , max(list_random))
##print("min", min(list_random))


##import random
##
##list_random = []
##
##for i in range(20):
##    list_random.append(random.randint(1,100))
##
##print(list_random)
##list_random.sort(reverse=1)
##print(list_random)
##print(list_random[-2])




import random
list_random = []

for i in range(10):
    list_random.append(random.randint(1,100))
print(list_random)
for i in range(len(list_random)-1, -1, -1):
    if list_random[i] < 20:
        list_random.pop(i)

print(list_random)

list_random.sort()
print(list_random[1])

































