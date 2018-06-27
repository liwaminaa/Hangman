word=input("Type a word for someone to guess: ")

word=word.lower()

if(word.isalpha()== False):
    print("That's not a word!")

guesses=[]
maxfails=6

dash=[]
print()

print(len(word))
for x in word:
    dash.append("-")
print(dash)

print()
guess=input("Guess a letter: ")

for letter in word:
    if guess == letter:
         guesses.append(guess)
         print("correct")

for letter in word:
    if guess != letter:
        guesses.append(dash)
    print("That's not right,try again")


print()
guess= input("Guess a letter:")

listofguesses=[guess]

print()

for letters in guess:
    print(listofguesses)


#dash= _
#dash * len(word)
#print(dash)

#dash.append()
#    print(dash)
