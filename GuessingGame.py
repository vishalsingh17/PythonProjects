# to import random module
import random
# to create a range of random numbers between 1-100
num = random.randrange(1,100)
# to take a user input to enter a number
guess = int(input("Enter any number: "))
while num!= guess: # means if n is not equal to the input guess
    # if guess is smaller than n
    if guess < num:
        print("OOPS.. Too low. Try Again!!")
        # to again ask for input
        guess = int(input("Enter number again: "))
    # if guess is greater than n
    elif guess > num:
        print("OOPS.. Too high. Try Again!!")
        # to again ask for the user input
        guess = int(input("Enter number again: "))
    # if guess gets equals to n terminate the while loop
    else:
        break
print("WOW.. You guessed it right!!")