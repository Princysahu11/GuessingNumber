
from random import  randint
lower_num, higher_num = 1,10

random_number: int = randint(lower_num,higher_num)
print(f"Guess any number between{lower_num} to {higher_num}.")
attempts,max_attempts=0,5

while attempts <= max_attempts:
    try:
        user_guess: int = int(input("Guess the number: "))
    except ValueError as e:
        print("Please enter a valid Number.")
        continue
    attempts += 1

    if user_guess > random_number:
        print("Number is higher")
    elif user_guess < random_number:
        print("Number is lower")
    else:
        print('Yahooo, you guessed it!')
        break
else:
    print(f"Oops ! you have exceeded the {max_attempts} limits. The number was {random_number}")

