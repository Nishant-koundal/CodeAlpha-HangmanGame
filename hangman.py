import random
print("🎮🎮🎮WELCOME TO HANGMAN GAME🎮🎮🎮")

pdfnd_words=["lotus","rose","code","alpha","lily"]

random_word=random.choice(pdfnd_words)

total_attempts=6
guessed_word=["_"]*len(random_word)

print("You have only 6 attempts. GOOD LUCK!!!")
print("word :"," ".join(guessed_word))

while total_attempts>0 and "_" in guessed_word:
    user=input("Enter a letter : ")


    if len(user)!= 1 or not user.isalpha():
        print("Please enter a single letter.")
        continue

    if user in random_word:
        for i in range(len(random_word)):
            if random_word[i]==user:
                guessed_word[i]=user
            print("Correct"," ".join(guessed_word))
            
    else:
        total_attempts-=1
        print("Wrong! Total attempts left - ",total_attempts)

if "".join(guessed_word)==random_word:
    print("\n You Win!🎉The word was : ",random_word,"\nThanks for playing!")
else:
    print("\nYou lose☠️!The word was : ",random_word)

    