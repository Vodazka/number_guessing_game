import random
number=random.randint(1,100) #makes it choose a random number from 1 to 100

print("Welcome to the number guessing game")
print("Your goal is to guess how many times i wanted to throw my computer off my window as i was coding this")
print("The answer may vary from 1 to 100")
print("Good luck")
print("I hope you fail.")
print("So, what is your guess?")

number_guess=int(input(":  "  ))  # user imputs their first guess

while(number_guess != number):  #loop repeats itself as long as the number guessed != to random.randint(1,100)
    if(number_guess<number):
        print("Oh come on it was more than that")
        print("Try again, your sufferring brings me joy")
        number_guess=int(input(":  "))
    elif(number_guess>number):
        print("Lower damn it. I am not THAT stupid!")
        print("Give it another go, come on, contribute to my hapinees as i watch you fail countless times")
        number_guess=int(input(":  "))
    else:
        print("Unfortunately that is correct")
        print("Who told you to do guess on the first try")
else:
    print("Looks like the fun is over") 