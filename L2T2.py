import random
def guess_the_number(lower,upper):
    number= random.randint(lower,upper)
    guess = None
    while guess!=number:
        guess=int(input("Enter your guess: "))
        if guess<number:
            print("too low")
        elif guess>number:
            print("too high")
        else:
            print(f"Congratulations! You've guessed the number {number} correctly!")
print("ENTER YOUR LOWER AND UPPER RANGE")
LOWER=int(input("enter lower range :"))
UPPER=int(input("enter upper range :"))
guess_the_number(LOWER,UPPER)



"""
Output:-

PS D:\cognifyz\L2> Python L2T2.py
ENTER YOUR LOWER AND UPPER RANGE
enter lower range :10
enter upper range :50
Enter your guess: 35
too high
Enter your guess: 25
Congratulations! You've guessed the number 25 correctly!
PS D:\cognifyz\L2> Python L2T2.py
ENTER YOUR LOWER AND UPPER RANGE
enter lower range :50
enter upper range :100
Enter your guess: 75
too low
Enter your guess: 85
too high
Enter your guess: 80
too low
Enter your guess: 83
too low
Enter your guess: 84
Congratulations! You've guessed the number 84 correctly!
PS D:\cognifyz\L2> 

"""