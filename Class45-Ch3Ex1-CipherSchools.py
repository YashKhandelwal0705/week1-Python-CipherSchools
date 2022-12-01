import random
winning_number=random.randint(0,100)
guessed_number=int(input())
if guessed_number==winning_number:
    print("You Win")
elif guessed_number>winning_number:
    print("Too High")
else:
    print("Too Low")

