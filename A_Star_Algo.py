# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:16:00 2024

@author: Dell
"""

def aStarAlgo(start_node, stop_node,Graph_nodes,heuristic_values):
         
        open_set = set(start_node) 
        closed_set = set()
        g = {} 
        parents = {}
 
        g[start_node] = 0
        parents[start_node] = start_node
         
         
        while len(open_set) > 0:
            n = None
 
            for v in open_set:
                if n == None or g[v] + heuristic(v,heuristic_values) < g[n] + heuristic(n,heuristic_values):
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

def heuristic(node,heuristic_values):
       return heuristic_values[node]
 
def create_graph_with_heuristic():
    Graph_nodes = {}
    heuristic_values = {}

    while True:
        node = input("Enter a node (or 'done' to finish): ").upper()
        if node == 'DONE':
            break
        heuristic_value = int(input(f"Enter the heuristic value for {node}: "))
        
        heuristic_values[node] = heuristic_value
        heuristic(node,heuristic_values)

        edges = []
        while True:
            edge_input = input(f"Enter an edge from {node} (destination, weight) or 'done' to finish: ")
            if edge_input.lower() == 'done':
                break

            destination, weight = map(str.strip, edge_input.split(','))
            edges.append((destination.upper(), int(weight)))

        Graph_nodes[node] = edges

    return Graph_nodes,heuristic_values


Graph_nodes,heuristic_values = create_graph_with_heuristic()
print("Graph Nodes:", Graph_nodes)
start=input("Enter the start node: ").upper()
end=input("Enter the last node: ").upper()
aStarAlgo(start,end,Graph_nodes,heuristic_values)