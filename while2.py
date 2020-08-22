name=input("Enter your name  : ")
food_item=[]
i=1
while(i<11):
    foodname=input("Enter your favorite food " + str(i) + ": ")
    food_item.append(foodname)
    i=i+1
    

print(name,"favorite foods are...")


for i in range(10):
    print(str(i+1) + ". ",food_item[i])


