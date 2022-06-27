import datetime
from Graph import Graph
from Package import Package
from Vertex import Vertex



class Truck:
    def __init__(self):
        self.package_list = []
        self.graph = Graph()
        self.start_vertex = Vertex(int(0))
        self.graph.add_vertex(self.start_vertex)
        self.time = datetime.datetime(2000,1,1,8,0,0)
        self.mpm = 60/18
        self.current_address = Vertex(int(0))
        self.distance_traveled = None

# The deliver algorithm takes an array that is the fastest path and delivers packages according to the fastest path.
# This algorithm also takes the distance between addresses and adds it to the trucks mileage and clock.
# This algorithm has a runtime of O(n^2)
    def deliver_algo(self, address_array, hashtable, matrix):
        total_distance = 0
        start_address = 0
        for address in address_array:
            for package in self.package_list:
                if package.address_id == address.label:
                    if package.address_id < start_address:
                        distance = matrix[package.address_id][start_address]
                        total_distance += float(distance)
                    else:
                        distance = matrix[start_address][package.address_id]
                        total_distance += float(distance)
                    start_address = address.label
                    self.package_list.remove(package)
                    hashtable.search(package.package_id).set_delivery_status("delivered")
                    t_delta = datetime.timedelta(minutes=(self.mpm * float(distance)))
                    self.time += t_delta
                    hashtable.search(package.package_id).set_delivery_time(self.time)
        self.distance_traveled = total_distance



















