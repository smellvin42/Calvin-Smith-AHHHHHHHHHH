import random

team_name = 'AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH'
strategy_name = 'fuck idk'
strategy_description = 'something something responsive algorythm'

print((1, 20))

def move(my_history, their_history, my_score, their_score):
    b = 'b'
    c = 'c'
    rounds = len(my_history)
    if their_score > my_score:
       return b
    if b in their_history[:1]:
        return b
    else:
        if random.randint(123, 200) <= rounds:
            if c not in my_history[:5]:
                return b
            else:
                return c

