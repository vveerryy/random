# подключаем модуль random
import random

# генерируем случайное число
random_number = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')
print('Ты готов?')
answer = input()
if answer == 'да':
    print('Угадай число')
flag = True
while flag == True:

    def is_valid(number):
        if number >= 1 and number <= 100:
            if number < random_number:
                print('Слишком мало, попробуйте ещё раз')
            elif number > random_number:
                print('Слишком много, попробуйте ещё раз')
            else:
                print('Вы угадали, поздравляю!')
        else:
            print('А может быть все-таки введем число от 1 до 100?')


    new_number = int(input())
    examination = is_valid(new_number)
    continue
    break
