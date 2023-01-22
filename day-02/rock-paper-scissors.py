# Part 1

# Column 1
# Opponent hand
# A = Rock
# B = Paper
# C = Scissors

# Column 2
# My hand
# X = Rock (1 point)
# Y = Paper (2 points)
# Z = Scissors (3 points)#

# Scoring
# Lose = 0 points
# Draw = 3 points
# Win = 6 points

# Match opponent hands with the player's hands
HAND_SHAPES = {
    'a': 'x',
    'b': 'y',
    'c': 'z'
}

# Key = Opponent hand, Value = What you play to win
WIN_CONDITIONS = {
    'a': 'y',
    'b': 'z',
    'c': 'x'
}

LOSE_CONDITIONS = {
    'a': 'z',
    'b': 'x',
    'c': 'y',
}

# Points gained from playing each hand shape
POINTS_HAND = {
    'x': 1,
    'y': 2,
    'z': 3
}


# Open file and save to `data`
file = open('input.txt', 'r')
data = file.readlines()
file.close


# Take 1 line and return an array of [opponent hand, your hand]
def get_hand(game):
    opponent_hand = game[0].casefold()
    your_move = game[2].casefold()
    hands = [opponent_hand, your_move]
    return hands


# Return points from game result and what hand was played
def calculate_points(hands):
    points = 0
    # Draw condition
    if HAND_SHAPES[hands[0]] == hands[1]:
        points += 3
    # Win condition
    if WIN_CONDITIONS[hands[0]] == hands[1]:
        points += 6
    # Hand played
    points += POINTS_HAND[hands[1]]
    return points


sum_points = 0
# Go through every game
for game in data:
    hands = get_hand(game)
    sum_points += calculate_points(hands)
print(sum_points)

# Part 2

# Column 2
# X = Need to lose
# Y = Need to draw
# Z = Need to win

# I just need to set my hand depending on column 2


# Return sum of the points using the 2nd column as a win condition
def part_2_calculate_points(hands):
    points = 0
    opponent_hand = hands[0]
    # Lose condition
    if hands[1] == 'x':
        my_hand = LOSE_CONDITIONS[hands[0]]
        points += POINTS_HAND[my_hand]
    # Draw condition
    elif hands[1] == 'y':
        points += 3
        my_hand = HAND_SHAPES[opponent_hand]
        points += POINTS_HAND[my_hand]
    # Win condition
    elif hands[1] == 'z':
        points += 6
        my_hand = WIN_CONDITIONS[hands[0]]
        points += POINTS_HAND[my_hand]
    return points


part_2_sum_points = 0
# Go through every match and sum the points from each game.
for game in data:
    hands = get_hand(game)
    part_2_sum_points += part_2_calculate_points(hands)
print(part_2_sum_points)
