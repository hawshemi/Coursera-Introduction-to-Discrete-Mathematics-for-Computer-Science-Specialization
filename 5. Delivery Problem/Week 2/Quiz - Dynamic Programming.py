import networkx as nx
from itertools import chain, combinations

# This function takes as input a graph g.
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# The function should return an optimal weight of a Hamiltonian cycle.

# This function returns all the subsets of the given set s in the increasing order of their sizes.
def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


# This function finds an optimal Hamiltonian cycle using the dynamic programming approach.
def dynamic_programming(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # The variable power now contains a tuple for each subset of the set {1, ..., n-1}.
    power = powerset(range(1, n))
    # The variable T is a dictionary, where the element T[s, i] for a set s and an integer i
    # equals the shortest path going through each vertex from s exactly once,
    # and ending at the vertex i.
    # Note that i must be in s.
    # Also, we will always assume that we start our cycle from the vertex number 0.
    # Thus, for convenience, we will always exclude the element 0 from the set s.
    T = {}
    # For every non-zero vertex i, we say that T[ tuple with the element i only, i]
    # equals the weight of the edge from 0 to i.
    # Indeed, by the definition of T, this element must be equal to the weight of
    # the shortest path which goes through the vertices 0 and i and ends at the vertex i.
    for i in range(1, n):
        # Syntactic note: In Python, we define a tuple of length 1 that contains the element i as (i,) *with comma*.
        T[(i,), i] = g[0][i]['weight']

    # For every subset s of [1,...,n-1]
    for s in power:
        # We have already initialized the elements of T indexed by sets of size 1, so we skip them.
        if len(s) > 1:
            # For every vertex i from s which we consider as the ending vertex of a path going through vertices from s.
            for i in s:
                # Define the tuple which contains all elements from s without *the last vertex* i.
                t = tuple([x for x in s if x != i])
                # Now we compute the optimal value of a cycle which visits all vertices from s and ends at the vertex i.

                # We first set the optimal value to infinity, and then we try every vertex j from s, other than i.
                # We update the optimal value as the minimum of the current optimal value and the value
                # of the cycle which visits all vertices from t, ends at the vertex j, and continues with an edge (j,i).
                optimal_value = float('inf')
                for j in t:
                    value = T[(t, j)] + g[j][i]['weight']
                    if value < optimal_value:
                        optimal_value = value
                # We set T[s, i] to the optimal value we just computed.
                T[(s, i)] = optimal_value


    # Return the weight of on optimal cycle - this is the minimum of the following sum:
    # weight of a path + the last edge to the vertex 0.
    return min(T[tuple(range(1, n)), i] + g[i][0]['weight'] for i in range(1, n))

