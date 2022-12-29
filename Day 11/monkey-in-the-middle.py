import operator

ops = {
    '+': operator.add,
    '*': operator.mul,
}


with open("input", "r") as f:
    data = f.read().splitlines()


# Monkey Class
class Monkey:
    def __init__(self, starting_items, operation_list, test_list):
        self._items = starting_items

        self._op_func = ops[operation_list[0]]
        self._op_value = operation_list[1]

        self._test = test_list

    def get_items(self):
        return self._items

    def add_item(self, item):
        self._items.append(item)

    def get_operation(self):
        return self._op_func, self._op_value

    def get_test(self):
        return self._test

    def execute_operation(self):
        if len(self._items) == 0:
            return
        if self._op_value == 'old':
            value = self._items[0]
        else:
            value = int(self._op_value)

        self._items[0] = self._op_func(self._items[0], value)
        # Floor division for monkey boredom
        self._items[0] //= 3

    def execute_test(self):
        if len(self._items) == 0:
            return
        res = self._items[0] % self._test[0] == 0

        # Save and remove from initial list
        tmp = self._items[0]
        self._items.pop(0)

        # If true
        if res:
            return tmp, self._test[1]
        # If false
        else:
            return tmp, self._test[2]


# Create a list of Monkeys
def create_monkeys(data):
    i = 0
    monkeys = []
    while i < len(data):
        if data[i][:6] == 'Monkey':
            # Create monkey

            # Get starting items for monkey
            items = data[i+1][18:].split(',')
            # List Comprehension
            items = [int(i) for i in items]

            # Get the monkey's operation
            monkey_operation = []
            monkey_operation.append(data[i+2][23])
            monkey_operation.append(data[i+2][25:])

            # Get monkey's test
            monkey_tests = []
            # Divisible number
            monkey_tests.append(int(data[i+3][21:]))
            # True target
            monkey_tests.append(int(data[i+4][-1]))
            # False target
            monkey_tests.append(int(data[i+5][-1]))

            monkeys.append(Monkey(
                items, monkey_operation, monkey_tests))
        i += 1
    return monkeys

# Print all current items held by monkeys


def print_monkey_items(monkeys):
    i = 0
    for monkey in monkeys:
        str = monkey.get_items()
        print(f'{i}: {str}')
        i += 1
    print('--------------------')


# Sort the list and multiply the two highest values together
def calc_monkey_business(list):
    list.sort()
    res = list[-1] * list[-2]
    return res


# Create list of monkey objects and their behaviour
monkeys = create_monkeys(data)
# Create counter list to track how many items they inspect
inspection_counts = [0] * len(monkeys)
round = 1
max_rounds = 20


while round <= max_rounds:
    # print(f'Round {round}')
    # Each turn:
    # Inspect and throw every item in order. Items received get added to the end
    # For each item:
    # 1. Execute the operation
    # 2. Execute the test
    # 3. Execute the test result

    for i, monkey in enumerate(monkeys):
        # # Execute operation
        # monkey.execute_operation()
        # # Execute test
        # item, target_monkey = monkey.execute_test()
        # monkeys[target_monkey].add_item(item)

        while len(monkey.get_items()) > 0:
            # Increment inspection counter
            inspection_counts[i] += 1
            # Execute operation on the item
            monkey.execute_operation()
            # Execute test
            item, target_monkey = monkey.execute_test()
            monkeys[target_monkey].add_item(item)

    # print_monkey_items(monkeys)
    # print(f'=========================\n')
    round += 1
print(round-1, inspection_counts)

monkey_business = calc_monkey_business(inspection_counts)
print(monkey_business)
