# Import data
with open('2023/day-04/input.txt', 'r') as f:
# with open('2023/day-04/sample-input.txt', 'r') as f:
    data = f.read().splitlines()

def print_array(arr):
    for row in arr:
        print(row)

# print_array(data)

# ---------------------------------- Part 1 ---------------------------------- #


# Class Card
class Card:
    def __init__(self, card_no, numbers, winning_numbers):
        self.card_no = card_no
        self.numbers = [int(num) for num in numbers]
        self.winning_numbers = [int(num) for num in winning_numbers]
        self.copies = 1
        self.len_matched_numbers = 0
        self.calculate_points()
    def calculate_points(self):
        self.points = 0
        # Find matching win numbers
        self.matched_numbers = [num for num in self.numbers if num in self.winning_numbers]
        # Calculate points
        if len(self.matched_numbers) == 0:
            self.points = 0
        else:
            self.len_matched_numbers = len(self.matched_numbers)
            self.points = 2**(len(self.matched_numbers)-1)

    def __str__(self):
        return f'Card {self.card_no}: {self.numbers} | {self.winning_numbers} | len_matched {self.len_matched_numbers} | Copies: {self.copies}'

    def print_winning_numbers(self):
        try:
            if self.matched_numbers != []:
                print(self.matched_numbers)
            else:
                print(f'Card {self.card_no} has no winning numbers.')
        except AttributeError:
            print("No winning numbers yet, please calculate points first.")

    def print_points(self):
        try:
            print(f'Card {self.card_no} has {self.points} points.')
        except AttributeError:
            print("No points yet, please calculate points first.")

    def sum_copies(self):
        if self.copies > 0 and self.len_matched_numbers > 0:
            self.copies = self.copies * self.len_matched_numbers + 1


cards_arr = []


def create_cards(data_arr):
    # loop each row (card)
    for row in data_arr:
        # Split by ": " --> card_no_tmp, numbers_tmp
        card_no_tmp, numbers_tmp = row.split(": ")
        # Split card_no by " " --> card_no_arr []
        card_no_arr = [word.strip() for word in card_no_tmp.split(" ") if word.split()]
        # Split numbers_tmp by "|" --> numbers_tmp, winning_numbers_tmp
        numbers_tmp, winning_numbers_tmp = [word.strip() for word in numbers_tmp.split("|") if word.split()]
        # Split numbers_tmp by " " --> numbers_arr []
        numbers_arr = [num.strip() for num in numbers_tmp.split(" ") if num.split()]
        # Split winning_numbers_tmp by " " --> winning_numbers_arr []
        winning_numbers_arr = [word.strip() for word in winning_numbers_tmp.split(" ") if word.split()]
        # Create new Card object & append to cards_arr
        cards_arr.append(Card(card_no_arr[-1], numbers_arr, winning_numbers_arr))
    return cards_arr


create_cards(data)


def sum_points(cards_arr):
    # loop through cards and add the points value
    total_points = 0
    for card in cards_arr:
        total_points += card.points
    return total_points


part_1_answer = sum_points(cards_arr)
print(f'Part 1 answer: {part_1_answer}')

# ---------------------------------- Part 2 ---------------------------------- #
sum_cards = 0
# Loop through cards_arr
for i, card in enumerate(cards_arr):
    for j in range(card.len_matched_numbers):
        try:
            cards_arr[i+j+1].copies += card.copies
        except IndexError:
            pass
    sum_cards += card.copies

# print_array(cards_arr)
print(f'Part 2 answer: {sum_cards}')