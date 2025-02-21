import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Я загадал число от 1 до 100. Попробуйте угадать его!")

    while not guessed:
        user_guess = input("Введите ваше предположение: ")

        # Проверка, является ли ввод числом
        if not user_guess.isdigit():
            print("Пожалуйста, введите действительное число.")
            continue

        user_guess = int(user_guess)
        attempts += 1

        if user_guess < number_to_guess:
            print("Слишком низко! Попробуйте снова.")
        elif user_guess > number_to_guess:
            print("Слишком высоко! Попробуйте снова.")
        else:
            guessed = True
            print(f"Поздравляю! Вы угадали число {number_to_guess} за {attempts} попыток.")

if __name__ == "__main__":
    guess_number()