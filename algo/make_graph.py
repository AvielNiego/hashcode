import src.busy_parser
from src import busy_parser


def distance(v1, v2):
    return 1

products = busy_parser.products
warehouses = busy_parser.warehouses
orders = []

g = dict.fromkeys(["w" + str(w) for w in xrange(len(warehouses))], [])
g.update(dict.fromkeys(["o" + str(w) for w in xrange(len(orders))], []))


for v1 in g:
    g[v1] = [(v2, distance(v1, v2)) for v2 in g]
