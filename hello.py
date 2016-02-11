def parse_warehouse(input_file):
    return [(int(k) for k in input_file.readline().split()), enumerate(int(z) for z in input_file.readline().split())]


input_file = open("D:\\Projects\\hashcode\\resources\\busy_day.in")

line = input_file.readline()
(rows, cols, drones_count, deadline, max_weight) = [int(x) for x in line.split()]

product_count = int(input_file.readline())
products = enumerate([int(w) for w in input_file.readline().split()])

warehouses_count = int(input_file.readline())

warehouses = [parse_warehouse(input_file) for _ in range(int(warehouses_count))]
