import math

from src import busy_parser


def distance(ver1, ver2):
    return math.sqrt(math.pow(ver1.location[0] - ver2.location[0], 2) + math.pow(ver1.location[1] - ver2.location[1], 2))

products = busy_parser.products
warehouses = busy_parser.warehouses
costumers = busy_parser.costumers

g = dict.fromkeys([w for w in warehouses], [])
g.update(dict.fromkeys([c for c in costumers], []))


for v1 in g.keys():
    g[v1] = [(v2, distance(v1, v2)) for v2 in g.keys()]

print 1
