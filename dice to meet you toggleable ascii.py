import random

DICE_PICS = ['''
 _______ 
|       |
|       |
|   •   |
|       |
|_______|''',
'''
 _______ 
|       |
| •     |
|       |
|     • |
|_______|''',
'''
 _______ 
|       |
| •     |
|   •   |
|     • |
|_______|''',
'''
 _______ 
|       |
| •   • |
|       |
| •   • |
|_______|''',
'''
 _______ 
|       |
| •   • |
|   •   |
| •   • |
|_______|''',
'''
 _______ 
|       |
| •   • |
| •   • |
| •   • |
|_______|
''']

DEFAULT_OPTS = ('r', 'n', 's', 'k', 'h', 'q', 'a')
ASCII_OPTS = ('r', 'n', 'k', 'h', 'q', 'a')

def instructions(ascii_on=False):
    print('Enter "r" to roll the dice.')
    print('Enter "n" to change the number of dice to roll.')
    if ascii_on == False:
        print('Enter "s" to change the number of sides the dice have.')
        print('Enter "a" to enable ASCII art. Can only display dice with 6 sides.')
    else:
        print('Enter "a" to disable ASCII art.')
    print('Enter "k" or "h" to display the key list again.')
    print('Enter "q" to quit.')

def user_choice(options, message = 'What would you like to do?\n'):
    while True:
        choice = input(message)
        if choice in options:
            return choice
        else:
            print('That\'s not a valid option!')

def number_choice(message='Please enter a number:\n'):
    while True:
        try:
            num = int(input(message))
            if num <= 0:
                print('You must enter a number greater than 0!')
                continue
            return num
        except ValueError:
            print('That\'s not a number!')

def roll(dice, sides):
    list_results = []
    for i in range(0, dice):
        result = random.randint(1, sides)
        list_results.append(result)
    return list_results

def print_roll(list_results, ascii=False):
    if ascii == False:
        for i, x in enumerate(list_results, 1):
            print('Die {0} rolled {1}.'.format(i,x))
            # print('Die %d rolled %d.' % (i, x))
    else:
        chunks = [list_results[i:i+5] for i in range(0, len(list_results), 5)]
        for chunk in chunks:
            for line in range(1, 7):
                for result in chunk:
                    pic = (DICE_PICS[result - 1])
                    print(pic.split('\n')[line], end='')
                print()
    # else:
    #     for line in range(1, 7):
    #         for result in list_results:
    #             pic = (DICE_PICS[result - 1])
    #             print(pic.split('\n')[line], end='')
    #         print()

def default_loop():
    number_sides = 6
    number_dice = 1
    ascii = False
    while True:
        opts = DEFAULT_OPTS
        if ascii:
            opts = ASCII_OPTS
        choice = user_choice(opts)
        if choice == 'r':
            result = roll(number_dice, number_sides)
            print_roll(result, ascii)
        elif choice == 'n':
            number_dice = number_choice(message='How many dice would you like to roll?\n')
        elif choice == 's':
            number_sides = number_choice(message='How many sides do your dice have?\n')
        elif choice == 'a':
            ascii = not ascii
            if ascii:
                number_sides = 6
            continue
        elif choice == 'h' or choice == 'k':
            instructions(ascii)
        elif choice == 'q':
            break


print('Welcome to Dice to Meet you!')

instructions()

default_loop()
    
print('Until next time; it was very dice to meet you!')
