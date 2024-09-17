import random
def guess_the_number():
    number= random.randint(1, 100)
    guess = None
    while guess!=number:
        guess=int(input("Enter your guess: "))
        if guess<number:
            print("too low")
        elif guess>number:
            print("too high")
        else:
            print(f"Congratulations! You've guessed the number {number} correctly!")
guess_the_number()

"""
Output:-

PS D:\cognifyz\L2> Python L2T1.py
Enter your guess: 50
too low
Enter your guess: 75
too low
Enter your guess: 90
too low
Enter your guess: 95
too high
Enter your guess: 92
too low
Enter your guess: 93
Congratulations! You've guessed the number 93 correctly!
PS D:\cognifyz\L2> Python L2T1.py
Enter your guess: 50
too high
Enter your guess: 25
too high
Enter your guess: 15
too high
Enter your guess: 10
Congratulations! You've guessed the number 10 correctly!
PS D:\cognifyz\L2>


"""