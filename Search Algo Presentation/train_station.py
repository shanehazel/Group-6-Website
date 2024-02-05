import heapq

class Graph:
    MRT_LINE_3 = "MRT Line 3"
    LRT_LINE_1 = "LRT Line 1"
    LRT_LINE_2 = "LRT Line 2"

    def __init__(self):
        self.adjacency_list = {}
        self.station_lines = {}

    def add_station(self, station, lines):
        if station not in self.adjacency_list:
            self.adjacency_list[station] = []
            self.station_lines[station] = lines

    def add_connection(self, station1, station2, weight, lines):
        self.adjacency_list[station1].append((station2, weight))
        self.adjacency_list[station2].append((station1, weight))
        self.station_lines[station1] = lines
        self.station_lines[station2] = lines

    def shortest_path(self, start, end):
        if start not in self.adjacency_list or end not in self.adjacency_list:
            return float('inf'), [], set()

        priority_queue = [(0, start, [], set())]
        visited = set()

        while priority_queue:
            current_distance, current_station, path, lines_taken = heapq.heappop(priority_queue)

            if current_station in visited:
                continue

            visited.add(current_station)

            if current_station == end:
                return current_distance, path + [current_station], lines_taken

            for neighbor, weight in self.adjacency_list[current_station]:
                if neighbor not in visited:
                    neighbor_lines = self.station_lines[neighbor]
                    new_lines_taken = lines_taken.union(neighbor_lines)
                    heapq.heappush(priority_queue, (current_distance + weight, neighbor, path + [current_station], new_lines_taken))

        return float('inf'), [], set()

# Creating a graph for MRT Line 3 and LRT Lines 1 and 2
manila_graph = Graph()

stations_mrt_line3 = ["North Avenue", "Quezon Avenue", "Kamuning", "Araneta Center-Cubao", "Santolan-Anapolis", "Ortigas", "Shaw Boulevard", "Boni", "Guadalupe", "Buendia", "Ayala", "Magallanes", "Taft Avenue"]
stations_lrt_line1 = ["Roosevelt", "Balintawak", "Monumento", "5th Avenue", "R. Papa", "Abad Santos", "Blumentritt", "Tayuman", "Bambang", "D. Jose", "Carriedo", "Central Terminal", "United Nations", "Pedro Gil", "Quirino", "Vito Cruz", "Gil Puyat", "Libertad", "EDSA", "Baclaran"]
stations_lrt_line2 = ["Recto", "Legarda", "Pureza", "V. Mapa", "J. Ruiz", "Gilmore", "Betty Go-Belmonte", "Araneta Center-Cubao", "Anonas", "Katipunan", "Santolan", "Marikina", "Antipolo"]

for station in stations_mrt_line3 + stations_lrt_line1 + stations_lrt_line2:
    manila_graph.add_station(station, set())

# MRT Line 3 connections
manila_graph.add_connection("North Avenue", "Quezon Avenue", 1, {Graph.MRT_LINE_3})
manila_graph.add_connection("Quezon Avenue", "Kamuning", 1, {Graph.MRT_LINE_3})
manila_graph.add_connection("Kamuning", "Araneta Center-Cubao", 1, {Graph.MRT_LINE_3})
manila_graph.add_connection("Araneta Center-Cubao", "Santolan-Anapolis", 1, {Graph.MRT_LINE_3})
manila_graph.add_connection("Santolan-Anapolis", "Ortigas", 1, {Graph.MRT_LINE_3})
manila_graph.add_connection("Ortigas", "Shaw Boulevard", 1, {Graph.MRT_LINE_3})
manila_graph.add_connection("Shaw Boulevard", "Boni", 1, {Graph.MRT_LINE_3})
manila_graph.add_connection("Boni", "Guadalupe", 1, {Graph.MRT_LINE_3})
manila_graph.add_connection("Guadalupe", "Buendia", 1, {Graph.MRT_LINE_3})
manila_graph.add_connection("Buendia", "Ayala", 1, {Graph.MRT_LINE_3})
manila_graph.add_connection("Ayala", "Magallanes", 1, {Graph.MRT_LINE_3})
manila_graph.add_connection("Magallanes", "Taft Avenue", 1, {Graph.MRT_LINE_3})

#LRT Line 1 connections
manila_graph.add_connection("Roosevelt", "Balintawak", 1, {Graph.LRT_LINE_1})
manila_graph.add_connection("Balintawak", "Monumento", 1, {Graph.LRT_LINE_1})
manila_graph.add_connection("Monumento", "5th Avenue", 1, {Graph.LRT_LINE_1})
manila_graph.add_connection("5th Avenue", "R. Papa", 1, {Graph.LRT_LINE_1})
manila_graph.add_connection("R. Papa", "Abad Santos", 1, {Graph.LRT_LINE_1})
manila_graph.add_connection("Abad Santos", "Blumentritt", 1, {Graph.LRT_LINE_1})
manila_graph.add_connection("Blumentritt", "Tayuman", 1, {Graph.LRT_LINE_1})
manila_graph.add_connection("Tayuman", "Bambang", 1, {Graph.LRT_LINE_1})
manila_graph.add_connection("Bambang", "D. Jose", 1, {Graph.LRT_LINE_1})
manila_graph.add_connection("D. Jose", "Carriedo", 1, {Graph.LRT_LINE_1})
manila_graph.add_connection("Carriedo", "Central Terminal", 1, {Graph.LRT_LINE_1})
manila_graph.add_connection("Central Terminal", "United Nations", 1, {Graph.LRT_LINE_1})
manila_graph.add_connection("United Nations", "Pedro Gil", 1, {Graph.LRT_LINE_1})
manila_graph.add_connection("Pedro Gil", "Quirino", 1, {Graph.LRT_LINE_1})
manila_graph.add_connection("Quirino", "Vito Cruz", 1, {Graph.LRT_LINE_1})
manila_graph.add_connection("Vito Cruz", "Gil Puyat", 1, {Graph.LRT_LINE_1})
manila_graph.add_connection("Gil Puyat", "Libertad", 1, {Graph.LRT_LINE_1})
manila_graph.add_connection("Libertad", "EDSA", 1, {Graph.LRT_LINE_1})
manila_graph.add_connection("EDSA", "Baclaran", 1, {Graph.LRT_LINE_1})

# LRT Line 2 connections
manila_graph.add_connection("Recto", "Legarda", 1, {Graph.LRT_LINE_2})
manila_graph.add_connection("Legarda", "Pureza", 1, {Graph.LRT_LINE_2})
manila_graph.add_connection("Pureza", "V. Mapa", 1, {Graph.LRT_LINE_2})
manila_graph.add_connection("V. Mapa", "J. Ruiz", 1, {Graph.LRT_LINE_2})
manila_graph.add_connection("J. Ruiz", "Gilmore", 1, {Graph.LRT_LINE_2})
manila_graph.add_connection("Gilmore", "Betty Go-Belmonte", 1, {Graph.LRT_LINE_2})
manila_graph.add_connection("Betty Go-Belmonte", "Araneta Center-Cubao", 1, {Graph.LRT_LINE_2})
manila_graph.add_connection("Araneta Center-Cubao", "Anonas", 1, {Graph.LRT_LINE_2})
manila_graph.add_connection("Anonas", "Katipunan", 1, {Graph.LRT_LINE_2})
manila_graph.add_connection("Katipunan", "Santolan", 1, {Graph.LRT_LINE_2})
manila_graph.add_connection("Santolan", "Marikina", 1, {Graph.LRT_LINE_2})
manila_graph.add_connection("Marikina", "Antipolo", 1, {Graph.LRT_LINE_2})

# Example of finding the shortest path
start_station = "Boni"
end_station = "V. Mapa"
shortest_distance, shortest_path, lines_taken = manila_graph.shortest_path(start_station, end_station)

if shortest_distance != float('inf'):
    transfer_station = None
    
    # Find the station where the transfer occurs
    for i in range(len(shortest_path) - 1):
        current_station = shortest_path[i]
        next_station = shortest_path[i + 1]
        if manila_graph.station_lines[current_station] != manila_graph.station_lines[next_station]:
            transfer_station = next_station
            break

    # Print the result with the transfer station
    if transfer_station:
        print(f"Shortest distance from {start_station} to {end_station}: {shortest_distance} stations.")
        print(f"Shortest path: {shortest_path}")
        print(f"Lines: Transfer from {' to '.join(lines_taken)} at {transfer_station}")
    else:
        print(f"Shortest distance from {start_station} to {end_station}: {shortest_distance} stations.")
        print(f"Shortest path: {shortest_path}")
        print(f"Lines: Direct route - No transfer needed.")
else:
    print(f"No path found from {start_station} to {end_station}")
