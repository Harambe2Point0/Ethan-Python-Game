# Setup
print ("Setup Initiated")

g = input("Enter Word to be Guessed")
array = []

for i in range(0, len(g)):
    array.append("_")

print ("\n"*40)


# Logic
while True:
    correct = False
    for i in range (0, len(g)):
        print(array[i], end="")
    print()
    guess = input()
    if len(guess) < 2:
        for i in range(0, len(g)):
            if guess == g[i]:
                correct = True
                array[i] = guess
        if correct == True:
            print ("Correct")
        else:
            print ("Incorrect")
    else:
        print ("U suck. Put in one letter")
