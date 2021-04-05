# Use python to base the base test cases
# implement the competition algorithm in C or C++ in order to greatly improve run time performance

class Game:
    def __init__(self):
        

class State:
    def __init__(self):



def minmax_search(state):
    return -1

def alphabeta_seatch(state):
    return -1





def utility(state):
    if red == wins:
        return 10000
    else:
        return -10000

def evaluation(state):
    return score(state, player.red) - score(state, player.yellow)


def score(state, player):
    return -1
    # returns number of tokens of players colour
    # + 10 * NUM_IN_A_ROW(2, state, player) +
    # 100 * NUM_IN_A_ROW(3, state, player) +
    # 1000 * NUM_IN_A_ROW(4 or more, state, player)

def num_in_a_row(count, state, player):
    return -1
    # returns the number of times that <state> contains a <count>-in-a-row for the given players
