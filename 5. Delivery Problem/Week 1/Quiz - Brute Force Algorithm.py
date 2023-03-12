import networkx as nx
from itertools import permutations

# This function takes as input a graph g.
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# The function should return the weight of a shortest Hamiltonian cycle.
# (Don't forget to add up the last edge connecting the last vertex of the cycle with the first one.)
#
# You can iterate through all permutations of the set {0, ..., n-1} and find a cycle of the minimum weight.

def cycle_weight(g, cycle):
    res = 0
    for i in range(1, len(cycle)):
        res += g[cycle[i-1]][cycle[i]]['weight']
    res += g[cycle[-1]][cycle[0]]['weight']
    return res


def all_permutations(g):
    # n is the number of vertices.
    n = g.number_of_nodes()
    res = 10 ** 11
    # Iterate through all permutations of n vertices
    for p in permutations(range(n)):
        # Write your code here.
        res = min(res, cycle_weight(g, p))
    return res
