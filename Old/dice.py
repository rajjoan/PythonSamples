import random
roll_again="yes"
while roll_again=="yes"or roll_again=="y":
        print("Rolling the dices.....")
        print("The values are......")
        print(random.randint(1,6))
        print(random.randint(1,6))
        roll_again=input("Roll again?(yes or no) : ")
print("Thank you for playing") 
