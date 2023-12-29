from common import helpers

input_path = "2023/day-05/input.txt"
sample_path = "2023/day-05/sample-input.txt"

# data = helpers.read_data(input_path)
data = helpers.read_data(sample_path)

helpers.print_array_rows(data)

# NOTE 
# Maps start at 0, so no need to offset
# Need a converter class = almanac

# How do I want to clean the data? Inside the class?

# class Almanac:
    # def __init__(self, data_input):

# class Map:
    # def __init__(self, name):
        # self.name = name
        # self.mappings = []

# def clean_data(data_input):
    # Clean seeds data
    # Start mapping
    # Loop through rows
        # If row is "", continue
        # If row[0] is not digit, create new map
            # split row on " ", and use map_name on the first element
