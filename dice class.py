#practice object-oriented program. This is a bad example because the only
#difference between classes is 'sides', which could easily be passed as
#an argument instead (plus then users can define the number of sides)
import random

class dice(object):
    def __init__(self, name):
        self.name = name
        # self.sides = sides

    def roll(self):
        list_results = []
        result = random.randint(1, self.sides)
        list_results.append(result)
        return list_results

    def print_roll(self, list_results):
        for i, x in enumerate(list_results):
            print(self.name + ' rolled ' + str(x) + '\n----------')

class d_six(dice):
    sides = 6

class d_ten(dice):
    sides = 10

class d_twenty(dice):
    sides = 20

def instructions():
    print('Roll one of your dice by entering a, s, or d for the following dice.\n'
          'Enter q at any time to quit.\n'
          'a - six-sided die\n'
          's - ten-sided die\n'
          'd - twenty-sided die\n')

def user_choice(options, message = 'Roll which die?\n'):
    while True:
        choice = input(message)
        if choice in options:
            return choice
        else:
            print('That\'s not a valid option!')

def main_loop():
    while True:
        opts = DEFAULT_OPTS
        choice = user_choice(opts)
        if choice != 'q':
            results = DICE_DICT[choice].roll()
            DICE_DICT[choice].print_roll(results)
        elif choice == 'q':
            break

DEFAULT_OPTS = ('a', 's', 'd', 'q')
sides = 0
DICE_DICT = {'a': d_six('D6'), 's': d_ten('D10'), 'd': d_twenty('D20')}

instructions()
main_loop()

print('bye')