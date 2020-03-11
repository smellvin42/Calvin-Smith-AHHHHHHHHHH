team_name = '2AHHHHHHHHHHHHHH'
strategy_name = 'RE:spond'
strategy_description = 'Respond to answers'


def move(my_history, their_history, my_score, their_score, opponent_name):
    b = 'b'
    c = 'c'
    rounds = len(my_history)
    if rounds == 0:
        return c
    if b not in their_history[:13]:
        return c




