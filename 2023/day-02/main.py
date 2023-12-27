# Import data
with open('input.txt', 'r') as f:
# with open('s1-input.txt', 'r') as f:
    data = f.read().splitlines()

# ---------------------------------- Part 1 ---------------------------------- #

# Cubes
# Red: 12
# Green: 13
# Blue: 14
bag_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

class Game:
    # cubes will be an array
    def __init__(self, id, cubes_arr):
        self.id = id
        self.cubes_arr = cubes_arr

        self.red = 0
        self.green = 0
        self.blue = 0

        self.min_red = 0
        self.min_green = 0
        self.min_blue = 0

        self.set_counts = []

    def __str__(self):
        return f'Game {self.id}: {self.cubes_arr}'

    def count_cubes(self):
        # Loop through cubes_arr for each set
        for set in self.cubes_arr:
        # # For each set, split into colour and number and save into variables
            split_arr = set.split(', ')            
            # For each split_arr, search for colour and assign to variable
            for item in split_arr:
                print(item)
                # Split item
                try:
                    cube_count, cube_colour = item.split(' ')
                except:
                    cube_count, cube_colour = item[1:].split(' ')
                # print(self.id, item)
                if cube_colour == 'red':
                    self.red = int(cube_count)
                elif cube_colour == 'green':
                    self.green = int(cube_count)
                else: 
                    self.blue = int(cube_count)
            # print(self.red, self.green, self.blue)
            self.set_counts.append([self.red, self.green, self.blue])

    def check_valid(self):
        for set in self.set_counts:
            # check if the game is valid
            # print(set)
            if set[0] > bag_cubes['red'] or set[1] > bag_cubes['green'] or set[2] > bag_cubes['blue']:
                return False
        return True
    
    def check_min_cubes(self):
        print(self.set_counts)
        for set in self.set_counts:
            if set[0] > self.min_red:
                self.min_red = set[0]
            if set[1] > self.min_green:
                self.min_green = set[1]
            if set[2] > self.min_blue:
                self.min_blue = set[2]
        # print(self.min_red, self.min_green, self.min_blue)
                

# Initialise games array
valid_games = []
all_games = []

# Loop through each game
for game in data:
    # Read game id = line[5]
    game_id = game.split(':')
    game_id = game_id[0].split(' ')
    game_id = game_id[-1]
    # print(f'Game ID: {game_id}')
    # Read cube data
    # Split semicolons into sets, starting from index 8(?)
    cube_data = game.split(':')
    cube_data = cube_data[1].split('; ')
    # Create Game object
    current_game = Game(game_id, cube_data)
    current_game.count_cubes()
    # print(current_game.set_counts)
    # print(current_game.check_valid())
    if current_game.check_valid():
        valid_games.append(current_game)
    # Create array of all games for part 2
    all_games.append(current_game)


# Loop through games array
sum = 0
for games in valid_games:
    sum += int(games.id)
    # Sum the game id
print(sum)

# ---------------------------------- Part 2 ---------------------------------- #
sum_power = 0
for game in all_games:
    game.check_min_cubes()
    print(game.min_red, game.min_green, game.min_blue)
    sum_power += game.min_red * game.min_green * game.min_blue

print(sum_power)