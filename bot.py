def bot_count(user_n):
    for number in range(user_n + 1):
        print('{} !'.format(number))


def bot_quiz():
    print('Why do we use methods?')
    print('1. To repeat a statement multiple times.')
    print('2. To decompose a program into several small subroutines.')
    print('3. To determine the execution time of a program.')
    print('4. To interrupt the execution of a program.')
    user_answer = input()
    while user_answer != '2':
        print('Please, try again.')
        user_answer = input()
    print('Completed, have a nice day!')


bot_name = 'Aid'
birth_year = 2020
print('Hello! My name is {}'.format(bot_name))
print('I was created in {}'.format(birth_year))
print('Please, remind me your name.')
user_name = input()
print('What a great name you have, {}'.format(user_name))
print('Let me guess your age.')
print('Enter remainder of dividing your age by 3, 5 and 7.')
remainder_3 = int(input())
remainder_5 = int(input())
remainder_7 = int(input())
result = (remainder_3 * 70 + remainder_5 * 21 + remainder_7 * 15) % 105
print("Your age is {}: that's a good time to start programming!".format(result))
print('Now I will prove to you that I can count to any number you want.')
user_number = int(input())
bot_count(user_number)
print("Let's test your programming knowledge.")
bot_quiz()
print('Congratulations, have a nice day!')
