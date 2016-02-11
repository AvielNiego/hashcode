from src.our_classes import Warehouse, Costumer


def parse_warehouse(input_file):
    return Warehouse([int(k) for k in input_file.readline().split()],
                     [int(_) for _ in input_file.readline().split()])


def parse_costumers(input_file):
    cos_location = [int(_) for _ in input_file.readline().split()]
    input_file.readline()
    products_index = [int(_) for _ in input_file.readline().split()]
    return Costumer(cos_location, products_index)


input_file = open(r'..\resources\busy_day.in')
line = input_file.readline()

(rows, cols, drones_count, deadline, max_weight) = [int(_) for _ in line.split()]
product_count = int(input_file.readline())

products = [int(w) for w in input_file.readline().split()]
warehouses_count = int(input_file.readline())

warehouses = [parse_warehouse(input_file) for _ in range(int(warehouses_count))]

costumers_count = int(input_file.readline())

costumers = [parse_costumers(input_file) for _ in range(int(costumers_count))]
