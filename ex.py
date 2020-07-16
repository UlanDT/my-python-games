import random
random_number = random.randint(1, 100)

print("Hello Player, Welcome to the game! \nGuess the number to win the game. The number is somewhere between 0 and 100")

guesses = [0]

while guesses[-1] != random_number:
    user_number = int(input("Enter the number: "))

    difference = user_number - random_number

    last = guesses[-1] - random_number

    if user_number > 100:
        print("Out of Bounds")
    elif user_number < 0:
        print("Out of Bounds")

    while len(guesses) == 1:
        if abs(difference) <= 10:
            print("Warm")
            break
        else:
            print("Cold")
            break

    if  len(guesses) > 1:
        if abs(difference) < abs(last):
            print("Warmer")
        else:
            print("Colder")

    if user_number == random_number:
        print("Victory!")
        print("You Have Won in " + str(len(guesses)) + " turns")

    guesses.append(user_number)
