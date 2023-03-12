import networkx as nx

# This function takes as input a graph g.
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# The function should return a 2-approximation of an optimal Hamiltonian cycle.

def approximation(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # You might want to use the function "nx.minimum_spanning_tree(g)"
    # which returns a Minimum Spanning Tree of the graph g
    mst = nx.minimum_spanning_tree(g)
    # You also might want to use the command "list(nx.dfs_preorder_nodes(graph, 0))"
    # which gives a list of vertices of the given graph in depth-first preorder.
    dfs = list(nx.dfs_preorder_nodes(mst, 0))

    res = 0
    for i in range(1, len(dfs)):
        res += g[dfs[i-1]][dfs[i]]['weight']
    res += g[dfs[-1]][dfs[0]]['weight']
    
    return res

