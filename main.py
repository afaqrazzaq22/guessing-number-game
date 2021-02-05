from art import logo
import random
print(logo)
random_check = random.randint(1, 100)
print("Computer is going to think  the number. ")


def check(random_check):
    ask = input("please enter h for hard way or e for easy way : ")
    if ask == "h":
        allowed_chance = 5
    elif ask == "e":
        allowed_chance = 10
    while allowed_chance:
        user_input = int(input("please enter any number: "))
        if allowed_chance > 0:
            if user_input < random_check:
                allowed_chance -= 1
                print(
                    f"To low and your remaining chances are {allowed_chance}")

        if allowed_chance > 0:
            if user_input > random_check:
                allowed_chance -= 1
                print(
                    f"To high and your remaining chances are {allowed_chance}")

        if allowed_chance > 0:
            if user_input == random_check:
                allowed_chance -= 1
                print("you win")
                break

        else:
            print("You don't have any remaning chaces to guess, you lose")
    allowed_chance = 0


check(random_check)
