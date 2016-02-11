def parse_warehouse(input_file):
    return [(input_file.readline().split()), enumerate(input_file.readline().split())]


input_file = open("D:\\Projects\\hashcode\\resources\\busy_day.in")

line = input_file.readline()
(rows, colms, drones_count, deadline, max_weight) = line.split()
qwe, asd = [1, 1]

product_count = input_file.readline()
products = enumerate(input_file.readline().split())

warehouses_count = input_file.readline()

warehouses = [parse_warehouse(input_file) for _ in range(int(warehouses_count))]
