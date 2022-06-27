#David Grimsley, Student #001529692
import csv
import datetime
from Dijkstra import Dijkstra
from HashTable import HashTable
from Package import Package
from Truck import Truck
from Vertex import Vertex

# Create a hashtable, three truck objects, and a distance matrix.
hashtable = HashTable()
truck_1 = Truck()
truck_2 = Truck()
truck_3 = Truck()
matrix = []

# Filling my matrix with the the distance between all the different addresses.
# This data comes from a CSV file which contains an "address ID" for each unique address, instead of the full address.
for i in range(30):
    matrix.append([0] * 30)
# This has a runtime of O(n*m) where n is the size of the matrix and m is number of values in the CSV file.
with open('distance_with_keys_only.csv', 'r') as csv_file:
    num = 0
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        for i in range(27):
            j = num
            matrix[i][j] = line[i]
        num = num + 1

# Creating package objects from a CSV file and inserting those values into the hashtable
# This has a runtime of O(n) where n is the number of rows in the CSV file
with open('WGUPS_Package_File.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    for line in csv_reader:
        package = Package(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])
        hashtable.insert(package.package_id, package)

# Loading truck 1. Each truck has its own CSV file with 16 packages, or less.
# Each package has an address ID. This ID then becomes a vertex (i.e. node) in the trucks graph.
# When the package is loaded on the truck, the status in the hashtable is changed to "on truck".
# Runtime is O(n)
with open('WGUPS_Package_File_Truck1.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    for line in csv_reader:
        package = Package(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])
        i = package.address_id
        j = Vertex(i)
        truck_1.graph.add_vertex(j)
        truck_1.package_list.append(package)
        hashtable.search(package.package_id).set_delivery_status("on truck")

# Placing the nodes in the trucks graph into a list data structure
package_list = []
for g in truck_1.graph.adjacency_list:
    package_list.append(g)
# Adding edge weight for all the different combinations of addresses in the graph.
# This algorithm has a runtime of O(n^2) where n is the number of packages on the truck
for i in range(len(package_list) - 1):
    for j in range(i+1, len(package_list)):
        if package_list[i].label > package_list[j].label:
            truck_1.graph.add_undirected_edge(package_list[i], package_list[j], float(matrix[package_list[j].label][package_list[i].label]))
        else:
            truck_1.graph.add_undirected_edge(package_list[i], package_list[j], float(matrix[package_list[i].label][package_list[j].label]))
# The truck uses its delivery algorithm to deliver packages
# This has a runtime of O(n^2) where n is the number of packages.
truck_1.deliver_algo(Dijkstra.greedy_paths(truck_1.graph), hashtable, matrix)


# The same process for truck 1 is repeated with truck 2
with open('WGUPS_Package_File_Truck2.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    for line in csv_reader:
        package = Package(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])
        i = package.address_id
        j = Vertex(i)
        truck_2.graph.add_vertex(j)
        truck_2.package_list.append(package)
        hashtable.search(package.package_id).set_delivery_status("on truck")

package_list = []
for g in truck_2.graph.adjacency_list:
    package_list.append(g)

for i in range(len(package_list) - 1):
    for j in range(i+1, len(package_list)):
        if package_list[i].label > package_list[j].label:
            truck_2.graph.add_undirected_edge(package_list[i], package_list[j], float(matrix[package_list[j].label][package_list[i].label]))
        else:
            truck_2.graph.add_undirected_edge(package_list[i], package_list[j], float(matrix[package_list[i].label][package_list[j].label]))

truck_2.deliver_algo(Dijkstra.greedy_paths(truck_2.graph), hashtable, matrix)

# Truck 3 isSince the driver from truck 1 now takes truck 3, the start time on truck is the end time on truck 1
truck_3.time = truck_1.time
with open('WGUPS_Package_File_Truck3.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    for line in csv_reader:
        package = Package(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])
        i = package.address_id
        j = Vertex(i)
        truck_3.graph.add_vertex(j)
        truck_3.package_list.append(package)
        hashtable.search(package.package_id).set_delivery_status("on truck")

package_list = []
for g in truck_3.graph.adjacency_list:
    package_list.append(g)
# For the package with the wrong address, if the time is before 10:20 A.M, the package is not delivered
if truck_3.time < datetime.datetime(2000,1,1,10,20,0,0):
    for i in range(len(package_list)):
        if package_list[i].label == 9:
            package_list.pop(i)
for i in range(len(package_list) - 1):
    for j in range(i+1, len(package_list)):
        if package_list[i].label > package_list[j].label:
            truck_3.graph.add_undirected_edge(package_list[i], package_list[j], float(matrix[package_list[j].label][package_list[i].label]))
        else:
            truck_3.graph.add_undirected_edge(package_list[i], package_list[j], float(matrix[package_list[i].label][package_list[j].label]))
truck_3.deliver_algo(Dijkstra.greedy_paths(truck_3.graph), hashtable, matrix)


# Prints package information
def search_package(id, hashtables):
    hashtable = hashtables
    a = "Package ID: " + str(hashtable.search(id).package_id) + ", "
    b = "Package Address: " + hashtable.search(id).package_address
    c = hashtable.search(id).package_city
    d = str(hashtable.search(id).package_zip) + ", "
    e = "Package deadline: " + hashtable.search(id).package_deadline + "' "
    f = "Package Weight: " + hashtable.search(id).package_weight + "' "
    g = "Delivery Status: " + hashtable.search(id).delivery_status
    print(a,b,c,d,e,f,g)

# Search by time to see the all information of a specific package.
def search_by_time_specific (id, hour, minute, hashtable):
    try:
        copy_hash = hashtable
        if copy_hash.search(id).delivery_time > datetime.time(hour, minute, 0, 0):
            copy_hash.search(id).delivery_status = "On Truck"
        search_package(id, copy_hash)
    except:
        print("Package not found")

# Search by time to see the package delivery and time of ALL packages.
def search_by_time(hashtable, hour, minute):
    copy_hash = hashtable
    packages = []
    for i in range(10):
        for j in copy_hash.table[i]:
            if j[1].delivery_time > datetime.time(hour,minute,0,0):
                j[1].delivery_status = "On Truck"
                packages.append([j[1].package_id, j[1].delivery_status])
            else:
                packages.append([j[1].package_id, j[1].delivery_status, str(j[1].delivery_time)])
    packages.sort()
    for i in range(len(packages)):
        print("Status at "+str(hour)+":"+str(minute)+" = "+str(packages[i]))

# Takes input from a user to search package status in a user interface.
def package_status_UI():
    a = None
    b = None
    c = None
    while a not in range(41):
        try:
            a = int(input("please enter ID of the package you would like to search: "))
            if a not in range(41):
                print("package not found")
        except ValueError:
            pass

    while b not in range(24):
        try:
            b = int(input("for what hour of the day would the status of package " + str(a) + " ?: "))
            if b not in range(24):
                b = int(input("please enter an integer between 0 and 23: "))
        except ValueError:
            pass

    while c not in range(61):
        try:
            c = int(input("for what minute of the day would the status of package " + str(a) + " ?: "))
            if c not in range(61):
                c = int(input("please enter an integer between 0 and 60: "))
        except ValueError:
            pass
    print(" ")
    search_by_time_specific(a,b,c,hashtable)

def all_package_status_UI():
    b = None
    c = None

    while b not in range(24):
        try:
            b = int(input("for what hour of the day would the status of all packages?: "))
            if b not in range(24):
                b = int(input("please enter an integer between 0 and 23: "))
        except ValueError:
            pass

    while c not in range(61):
        try:
            c = int(input("for what minute of the day would the status of all packages?: "))
            if c not in range(61):
                c = int(input("please enter an integer between 0 and 60: "))
        except ValueError:
            pass
    print(" ")
    search_by_time(hashtable,b ,c)

# Takes user input to search truck mileage in a user interface.
def truck_mileage_UI():
   a = truck_1.distance_traveled
   b = truck_2.distance_traveled
   c = truck_3.distance_traveled
   d = a+b+c
   print("\nTruck 1 mileage:" + str(a))
   print("Truck 2 mileage:" + str(b))
   print("Truck 3 milage: " + str(c))
   print("Combined mileage: " + str(d))


# User interface
print("Welcome to the WGU Parcel Service user interface")
run = True
while run:
    try:
        a = None
        while a not in (1,2,3,4):
            a = int(input("\ntype 1 to view the status of a specific package, 2 to view the status of all packages at a certain time, 3 to view truck mileage, or 4 to terminate the program: "))
        if a == 1:
            package_status_UI()
        elif a ==2:
            all_package_status_UI()
        elif a == 3:
            truck_mileage_UI()
        elif a == 4:
            print("Goodbye...")
            run = False
    except ValueError:
        pass

'''for i in range(10):
    for j in hashtable.table[i]:
        print(j[1])'''


