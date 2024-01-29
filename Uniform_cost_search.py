# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 18:03:08 2024

@author: Dell
"""

def UniformSearchAlgo(start_node, stop_node,Graph_nodes):
        open_set = set(start_node) 
        closed_set = set()
        g = {start_node:0} 
        parents = {start_node: start_node}
        while len(open_set) > 0:
            n = None
            for v in open_set:
                if n == None or g[v] < g[n] :
                    n = v
            if n == stop_node or Graph_nodes[n] == None:
                pass
            else:
                for (m, weight) in get_neighbors(n):
                    if m not in open_set and m not in closed_set:
                        open_set.add(m)
                        parents[m] = n
                        g[m] = g[n] + weight
                         
                    else:
                        if g[m] > g[n] + weight:
                            g[m] = g[n] + weight
                            parents[m] = n
                             
                            if m in closed_set:
                                closed_set.remove(m)
                                open_set.add(m)
            if n == None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                path = []
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
 
                path.append(start_node)
                path.reverse()
                print('Path found: {}'.format(path))
                return path
 
            open_set.remove(n)
            closed_set.add(n)
 
        print('Path does not exist!')
        return None
    
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def create_graph_with_actualcost():
    Graph_nodes = {}
    while True:
        node = input("Enter a node (or 'done' to finish): ").upper()
        if node == 'DONE':
            break
        edges = []
        while True:
            edge_input = input("Enter an edge from %s (destination, weight) or 'done' to finish: " %node)
            if edge_input.lower() == 'done':
                break

            destination, weight = map(str.strip, edge_input.split(','))
            edges.append((destination.upper(), int(weight)))
            Graph_nodes[node] = edges
            return Graph_nodes

Graph_nodes = create_graph_with_actualcost()
print("Graph Nodes:", Graph_nodes)
start=input("Enter the start node: ").upper()
end=input("Enter the last node: ").upper()
UniformSearchAlgo(start,end,Graph_nodes)