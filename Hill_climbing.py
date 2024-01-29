# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 18:20:48 2024

@author: Dell
"""

def hillClimbingAlgo(start_node, stop_node, Graph_nodes, heuristic_values):
    def get_neighbors(v):
        if v in Graph_nodes:
            return Graph_nodes[v]
        else:
            return []
    curr_node = start_node
    path = [curr_node]
    while curr_node != stop_node:
        neighbors = get_neighbors(curr_node)
        if not neighbors:
            print('Path does not exist!')
            return None
        neighbor_values= [(neighbor, heuristic_values.get(neighbor, 0)) for neighbor in neighbors]
        if not neighbor_values:
            print('Path does not exist!')
            return None
        neighbor_values.sort(key=lambda x: x[1])
        next_node, _ = neighbor_values[0]
        if heuristic_values[next_node] >= heuristic_values[curr_node]:
            print('Local maximum reached. Path does not exist!')
            return None
        path.append(next_node)
        curr_node = next_node
    print('Path found:', path)
    return path
    
def heuristic(node,heuristic_values):
       return heuristic_values[node]
  
def create_graph_with_heuristic():
    Graph_nodes = {}
    heuristic_values={}
    while True:
        node = input("Enter a node (or 'done' to finish): ").upper()
        if node == 'DONE':
            break
        heuristic_value = int(input("Enter the heuristic value for %s: "%node))
        heuristic_values[node] = heuristic_value
        heuristic(node,heuristic_values)
        edges = []
        while True:
            edge_input = input("Enter an edge from %s (destination) or 'done' to finish: "%node)
            if edge_input.lower() == 'done':
                break
            destination = edge_input
            edges.append((destination.upper()))
        Graph_nodes[node] = edges
    return Graph_nodes,heuristic_values

Graph_nodes, heuristic_values = create_graph_with_heuristic()
print("Graph Nodes:", Graph_nodes)
start = input("Enter the start node: ").upper()
end = input("Enter the last node: ").upper()
hillClimbingAlgo(start, end, Graph_nodes, heuristic_values)
