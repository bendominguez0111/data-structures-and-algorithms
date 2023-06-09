# Given a graph, use depth first search to find a valid search path
# https://ucarecdn.com/a67cb888-aa0c-424b-8c7f-847e38dd5691/
from __future__ import annotations

class Node:
    def __init__(self, key:str):
        self.key = key
        self.neighbors = {}

    def add_neighbor(self, neighbor:Node, weight:int=0):
        self.neighbors[neighbor] = weight

    def __repr__(self):
        return "<Node {}>".format(self.key)

class Graph:
    def __init__(self):
        self.nodes = {} # key: Node(key)

    def add_node(self, key:str):
        new_node = Node(key=key)
        self.nodes[key] = new_node

    def add_edge(self, from_key:str, to_key:str, weight:int=0):
        if from_key not in self.nodes:
            self.add_node(from_key)
        if to_key not in self.nodes:
            self.add_node(to_key)

        self.nodes[from_key].add_neighbor(self.nodes[to_key], weight)
        self.nodes[to_key].add_neighbor(self.nodes[from_key], weight) # add bidirectionality

    def get_node(self, key:str):
        return self.nodes.get(key)

def dfs(graph, node=None, visited=[]):
    if node not in visited:
        visited.append(node)
        for neighbor in node.neighbors:
            dfs(graph, neighbor, visited)

    return visited

def dfs_choose_highest_weight(graph, node=None, visited=[]):
    """Find the search path based off the highest weights
    """
    if node not in visited:
        visited.append(node)
        search_space = sorted(node.neighbors.items(), key=lambda x:x[1], reverse=True)
        for elem in search_space:
            dfs_choose_highest_weight(graph, elem[0], visited)

    return visited

if __name__ == '__main__':

    graph = Graph()

    graph.add_edge(from_key="0", to_key="4", weight=8)
    graph.add_edge(from_key="0", to_key ="1", weight=3)
    graph.add_edge(from_key="0", to_key="3", weight=7)
    graph.add_edge(from_key="1", to_key="3", weight=4)
    graph.add_edge(from_key="3", to_key="2", weight=2)
    graph.add_edge(from_key="1", to_key="2", weight=1)

    visited = dfs(graph, graph.get_node("0"))
    visited = ', '.join([node.key for node in visited])
    
    print(visited) # 0, 4, 1, 3, 2

    visited = dfs_choose_highest_weight(graph, graph.get_node("0"))
    visited = ', '.join([node.key for node in visited])

    print(visited) # 0, 4, 3, 1, 2