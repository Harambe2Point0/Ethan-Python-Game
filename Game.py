# Setup
print ("Setup Initiated")

g = input("Enter Word to be Guessed")
array = []
correct = False

for i in range(0, len(g)):
    array.append("_")

print ("This is Hangman! You will have 7 guesses to spell the word. If you do not spell the word within 5 guesses, he dies.")
print ("\n"*40)


# Logic
while True:
    for i in range (0, len(g)):
        print(array[i], end="")
    print()
    guess = input("First Guess")
    for i in range(0, len(g)):
        if guess == g[i]:
            correct = True
            array[i] = guess
    if correct == True:
        print ("Correct")
    else:
        print ("Incorrect, Nerd")
