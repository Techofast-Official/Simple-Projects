from random import randint
import sys

# generate a number
answer = randint(int(sys.argv[1]), int(sys.argv[2]))
while True:
    try:
        # input from user ?
        guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  '))
        if 0 < guess <= int(sys.argv[2]):
            if guess == answer:
                print("you are a genius")
                break
        else:
            print(f"we said {sys.argv[1]}~{sys.argv[2]}")
    except ValueError:
        print("please type only numbers")
        continue
