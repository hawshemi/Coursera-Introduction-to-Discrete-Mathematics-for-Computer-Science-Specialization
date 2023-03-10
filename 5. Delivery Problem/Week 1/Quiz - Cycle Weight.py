import networkx as nx

# This function takes as input a graph g and a list of vertices of the cycle.
# (Each vertex given by its index starting from 0.)
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# For example, a valid input would be a graph on 3 vertices and cycle = [2, 0, 1].
#
# The function should return the weight of the cycle.
# (Don't forget to add up the last edge connecting the last vertex of the cycle with the first one.)
#
# If you want to get the weight of the edge between vertices u and v, you can take g[u][v]['weight']


def cycle_length(g, cycle):
    # Checking that the number of vertices in the graph equals the number of vertices in the cycle.
    assert len(cycle) == g.number_of_nodes()
    # Write your code here.
    res = 0
    for i in range(1, len(cycle)):
        res += g[cycle[i-1]][cycle[i]]['weight']
    res += g[cycle[-1]][cycle[0]]['weight']

    return res
    
# Here is a test case:
# Create an empty graph. 
g = nx.Graph()
# Now we will add 6 edges between 4 vertices
g.add_edge(0, 1, weight = 2)
# We work with undirected graphs, so once we add an edge from 0 to 1, it automatically creates an edge of the same weight from 1 to 0.
g.add_edge(1, 2, weight = 2)
g.add_edge(2, 3, weight = 2)
g.add_edge(3, 0, weight = 2)
g.add_edge(0, 2, weight = 1)
g.add_edge(1, 3, weight = 1)

# Now we want to compute the lengths of two cycles:
cycle1 = [0, 1, 2, 3]
cycle2 = [0, 2, 1, 3]

# assert(cycle_length(g, cycle1) == 8)
# assert(cycle_length(g, cycle2) == 6)
