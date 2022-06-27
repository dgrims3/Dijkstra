class Dijkstra:

    # This greedy algorithm takes the nodes in a graph and uses their edge weights to find the nearest neighbor.
    def greedy_paths(graph):
        unvisited_queue = []
        for node in graph.adjacency_list:
            unvisited_queue.append(node)
        fastest_path = []
        total_miles = 0
        while len(unvisited_queue) > 1:
            lowest_weight = 1000
            i = 0
            nearest_neighbors = None
            for j in range(i + 1, len(unvisited_queue)):
                temp_neighbor = None
                if graph.edge_weights[(unvisited_queue[i], unvisited_queue[j])] < lowest_weight:
                    lowest_weight = graph.edge_weights[(unvisited_queue[i], unvisited_queue[j])]
                    temp_neighbor = j
                    nearest_neighbors = temp_neighbor
            total_miles = total_miles + lowest_weight
            temp = unvisited_queue[nearest_neighbors]
            unvisited_queue[i] = temp
            fastest_path.append(unvisited_queue.pop(nearest_neighbors))
        return fastest_path

    # This is similar to the above algorithm but return the last visited stop.
    # This is used for package 9, to see where the truck must wait until 10:20

    def last_address(graph):
        last_address = None
        unvisited_queue = []
        for node in graph.adjacency_list:
            unvisited_queue.append(node)
        fastest_path = []
        total_miles = 0
        while len(unvisited_queue) > 1:
            lowest_weight = 1000
            i = 0
            nearest_neighbors = None
            for j in range(i + 1, len(unvisited_queue)):
                temp_neighbor = None
                if graph.edge_weights[(unvisited_queue[i], unvisited_queue[j])] < lowest_weight:
                    lowest_weight = graph.edge_weights[(unvisited_queue[i], unvisited_queue[j])]
                    temp_neighbor = j
                    nearest_neighbors = temp_neighbor
            total_miles = total_miles + lowest_weight
            temp = unvisited_queue[nearest_neighbors]
            unvisited_queue[i] = temp
            fastest_path.append(unvisited_queue.pop(nearest_neighbors))
        last_address = unvisited_queue[0]
        return last_address


