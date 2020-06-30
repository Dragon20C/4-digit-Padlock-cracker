padlock_password = [9, 0, 1, 9]

number = 0
number1 = 0
number2 = 0
number3 = 0
guess = [number, number1, number2, number3]

while True:
    if guess == padlock_password:
        print("The padlock password is: " + str(guess))
        break
    else:
        guess[0] = number3
        guess[1] = number2
        guess[2] = number1
        guess[3] = number
        number += 1
        if number == 10:
            number = 0
            number1 += 1
            if number1 == 10:
                number1 = 0
                number2 += 1
                if number2 == 10:
                    number2 = 0
                    number3 += 1
                    if number3 == 10:
                        number3 = 0
        print(guess)
