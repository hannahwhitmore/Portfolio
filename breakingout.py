print("You have just been imporisioned for something you did not commit. Your goal is to successfully break out without anyone recognizing you.")
print("")
print("Your first mission is to escape your cell")
def o():
    print("")
    c = input("Do you bribe the security guard or try to break the lock at night? Type b for bribe and l for lock.")
    if c == "b":
        print("He doesn't accept")
        ch = input("Do you attack him or get your cell mate to attack him so you can run? Type a for attack c for cell mate.")
        if ch == "a":
            print("He fights back")
            print("")
            cho = input("Do you kill him or give up. Type k for kill and g for give up")
            if cho == "k":
                print("You did it!")
            elif cho == "g":
                print("Thats disappointing. Guess you'll have to stay in prision.")
        elif ch == "c":
            print("He fights back")
            print("")
            cho = input("Do you kill him or give up. Type k for kill and g for give up")
            if cho == "k":
                print("You did it!")
            elif cho == "g":
                print("Thats disappointing. Guess you'll have to stay in prision.")
    elif c == "l":
        print("You successfully broke the lock")
        print("")
        choi = input("Do you have your cell mate keep watch or make a run for it. Type c for cell mate and r for run.")
        if choi == "c":
            print("Your cell mate betrays you and tries to escape for himself.")
            print("")
            choic = input("Do you forgive him and try to escape together or kill him. Press f for forgive and k for kill.")
            if choic == "f":
                print("Your cell mate helps you get out of the building and you've made it out!")
            elif choic == "k":
                print("You killed your cell mate, but he would have helped you. You got spotted by a guard.")
                print("")
                choice = input("Do you want to hitchhike or run as far as possible. Press h for hitchike and r for run.")
                if choice == "h":
                    print("Congratulations! You safley made it out of the area.")
                elif choice == "r":
                    print("Unfortunately, you were frantically running and got hit by a car, rip.")
        elif choi == "r":
            print("You successfully ran out!")

    else:
        print("Invalid input.")
o()
