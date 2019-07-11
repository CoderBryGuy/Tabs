_author_ = "Dev"

# for i in range(0, 10):
#     print("No {} squared is {} and cubed is {:4}".format(i+1, i**2, i**4))
#     print("calculation complete")
#
# print("\n\nThis is out of the block")
#

# name = input("please enter your name")
#
# age = int(input("how old are you, {0}".format(name)))
#
# print(age)
#
# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("Please come back in {0}".format(18-age))


print("please guess a number between 1 and 10:")
guess = int(input())

# if guess < 5:
#     print("please guess higher")
#     guess = int(input())
#     if guess == 5:
#         print("well done you guessed it")
#     else:
#         print("Sorry you have not guessed correctly")
# elif guess > 5:
#     print("please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("well done you guessed it:")
#     else:
#         print("sorry you have not guessed correctly")
# else:
#     print("you got it the first time")

if guess !=5:
    if guess < 5:
        print("Please guess higher")
    else:
        print("Please guess lower")

    guess = int(input())
    if guess ==  5:
        print("Well done you guessed it")
    else:
        print("sorry you did not guess it")

else:
    print("you got it the first time")
