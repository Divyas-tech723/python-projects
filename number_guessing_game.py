import random

number = random.randint(1,100)
attempts = 0
max_attempts = 7

while attempts < max_attempts:

    try:
        print("guess your number (1 - 100): ")
        guess = int(input())
        if guess<1 or guess>100:
            print("please enter within the range ")
            continue
        attempts += 1
        if guess == number:
            print("yes ur right")
            break
        elif guess < number:
            print("low")
        else:
            print("high")
    except ValueError:
        print("enter valid number")   

if attempts == max_attempts and guess!=number:
    print(f"out of attempts The number is {number}")

