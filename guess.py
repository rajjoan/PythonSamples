import random
ans = "y"
while (ans == "y"):
   secret = random.randint(1,99)
   guess = int(input("Enter an integers between 1  and 99 :"))
   while (secret != "guess"):
       if guess < secret:
         print ("Too low")
         guess = int(input("Enter an integers between 1  and 99 :"))
       elif guess > secret:
         print ("Too high")
         guess = int(input("Enter an integers between 1  and 99 :"))
       else:
         print ("Yippe you guessed it right")
         break
   ans = input("Do you want to play again?(Enter y or n)") 





