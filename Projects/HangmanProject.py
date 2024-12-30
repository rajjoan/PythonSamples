import random

words = [ 'computer', 'notebook', 'coffee', 'interface', 'window']

word = random.choice(words)

blanks = []
for i in range(len(word)):
    blanks.append('_')
print(blanks)

list_word = list(word)
#print(list_word)

chances = 0
num_chances = len(list_word) + 1

while chances < num_chances:
    print("You have", num_chances - chances, "chances left")
    user_guess = input("Guess a letter: ")

    if user_guess in list_word:
        for j in range(len(list_word)):
            if user_guess == list_word[j]:
                blanks[j] = user_guess
        print(blanks)
    else:
        print(blanks)
        print(user_guess, "is not in the word")


    if blanks == list_word:
        print(blanks)
        print("You win!")
        break

    chances = chances + 1


    if chances == num_chances:
        print("You ran out of chances.")
        break