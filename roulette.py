#black is even and red is odd
from random import randint
bet = randint(1,36)
play = True
while play:
    guess = input("Do you want to guess even/odd(1), color(2), or make a specific number bet(3).")
    if guess == "1":
        mo = input("How much money do you want to put down?")
        money = int(mo)
        be = input("How much money do you want to bet?")
        b = int(be)
        g1 = input("even or odd?")
        if(g1 == "odd" and (bet%2 != 0)):
            print("Correct, the number was: " + str(bet))
            money = money + b
            print("You now have " + str(money) + " dollars")
            p = input("Would you like to play again?")
            if p == "no":
                play = False
            else:
                play = True
        elif(g1 == "even" and(bet%2 == 0)):
            print("Correct, the number was: " + str(bet))
            money = money + b
            print("You now have " + str(money) + " dollars")
            p = input("Would you like to play again?")
            if p == "no":
                play = False
            else:
                play = True
        else:
            print("Incorrect, the number was: " + str(bet))
            money = money - b
            print("You now have " + str(money) + " dollars")
            p = input("Would you like to play again?")
            if p == "no":
                play = False
            else:
                play = True
    elif guess == "2":
        mo = input("How much money do you want to put down?")
        money = int(mo)
        be = input("How much money do you want to bet?")
        bet = int(be)
        g2 = input("Black is even numbers and red is odd numbers, which color would you like to choose?")
        if(g2 == "black" and (bet%2 ==0)):
            print("Correct, the number was: " + str(bet))
            money = money + b
            print("You now have " + str(money) + " dollars")
            p = input("Would you like to play again?")
            if p == "no":
                play = False
            else:
                play = True

        elif(g2 == "red" and (bet%2 !=0)):
            print("Correct, the number was" + str(bet))
            money = money + b
            print("You now have " + str(money) + " dollars")
            p = input("Would you like to play again?")
            if p == "no":
                play = False
            else:
                play = True
        else:
            print("Incorrect, the number was: " + str(bet))
            money = money - b
            print("You now have " + str(money) + " dollars")
            p = input("Would you like to play again?")
            if p == "no":
                play = False
            else:
                play = True
    elif guess == "3":
        mo = input("How much money do you want to put down?")
        money = int(mo)
        be = input("How much money do you want to bet?")
        bet = int(be)
        g3 = input("Which number, 1-36 are you betting on? ")
        gint = int(g3)
        if gint == bet:
            print("You guessed the right number!")
            money = money + b
            print("You now have " + str(money) + " dollars")
            p = input("Would you like to play again?")
            if p == "no":
                play = False
            else:
                play = True
        else:
            print("Incorrect, the number was: " + str(bet))
            money = money - b
            print("You now have " + str(money) + " dollars")
            p = input("Would you like to play again?")
            if p == "no":
                play = False
            else:
                play = True
    else:
        print("Invalid.")
