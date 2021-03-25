from art import logo, vs
from game_data import data
from random import choice
import logging

'''
{
    'name': 'Instagram',
    'follower_count': 346,
    'description': 'Social media platform',
    'country': 'United States'
},
'''

#logging.basicConfig(level = logging.DEBUG)

def description(record):
    message = f"{record['name']}, "\
        f"{record['description']}, "\
        f"from {record['country']}"

    return message

def display_characters(record1, record2):
    print(f"Compare A: {description(record1)}")
    print(vs)
    print(f"Against B: {description(record2)}")

def check_answer(guess, item1, item2):
    if item1 > item2:
        return guess == 'A'
    else:
        return guess == 'B'



def main():
    print(logo)
    score = 0
    item2 = choice(data)

    end_game = False
    while not end_game:
        values = {}

        item1 = item2
        item2 = choice(data)
        while item1 == item2:
            item2 = choice(data)

        values['A'] = item1['follower_count']
        values['B'] = item2['follower_count']

        logging.info(f"{values['A']}:{values['B']}")

        display_characters(item1, item2)
        print(f"\nYour current score: {score}")
        guess = input("Who has more followers? Type A or B\n  > ").upper()[:1]
        logging.info(f"{guess}")

        is_correct = check_answer(guess, values['A'], values['B'])

        if is_correct:
            score += 1
            print( "Well done, you are right.")

        else:
            print(f"Oops, better luck next time.")
            end_game = True

        print(f"score is {score}")


if __name__ == '__main__':
    main()

# logging.debug(stuff)
