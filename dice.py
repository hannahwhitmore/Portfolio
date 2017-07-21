from random import randint
dice = randint(1,6)


a = input("Guess which number the dice rolled, 1-6: ")
num = int(a)
if num == dice:
    print("Good job, you guessed it! The number was: " + str(dice))
else:
    print("Unfortunately, you did not guess it. The number was: " + str(dice))
