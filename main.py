import csv
import argparse

class Routes:
    def prepare_data_source(self, filename : object):
        """ Read data the CSV and prepare it to find the all routes """
        try:
            with open(filename) as csv_file:
                csv_read = csv.reader(csv_file, delimiter = ',')
                self.routes_data = [(row[0],row[1],row[2]) for row in csv_read] 
                self.unique_nodes = set()
                [self.unique_nodes.update([node[0], node[1]]) for node in self.routes_data]
                self.routes_paths = {node : {} for node in self.unique_nodes}
                [self.routes_paths[row[0]].update({row[1] : int(row[2])}) for row in self.routes_data]        

        except Exception as e:
            print(f"Prepare data source, Error: {e}")
            raise e

    def find_shortest_route(self, origin : str, dest : str) -> (int, int):
        """ finding the shortest route from origin to dest """
        try:
            self.time_to_dest = {node : float("inf") if node != origin else 0 for node in self.unique_nodes}
            self.shortest_path = []
            unmark_nodes = sorted([node for node in self.unique_nodes])
            mark_nodes_path = {node_origin : None for node_origin in self.unique_nodes}
            collecting_route_path = True
            
            while unmark_nodes:
                import pdb; pdb.set_trace()
                for node, time in self.routes_paths[unmark_nodes[0]].items():
                    time_path = self.time_to_dest[unmark_nodes[0]] + time
                    if self.time_to_dest[node] > time_path:
                        self.time_to_dest[node] = time_path
                        mark_nodes_path[node] = unmark_nodes[0]
                unmark_nodes.remove(unmark_nodes[0])

            while collecting_route_path:
                next_path = dest
                for node in mark_nodes_path:
                    if mark_nodes_path[next_path] != None:
                        self.shortest_path.append(mark_nodes_path[next_path])
                        next_path = mark_nodes_path[next_path]
                collecting_route_path = False

            if self.shortest_path:
                self.shortest_path.insert(0, dest)
                self.shortest_path.reverse()

            self.stops = [node for node in self.shortest_path if node not in [origin, dest]]
            
            return len(self.stops), self.time_to_dest[dest]

        except Exception as e:
            print(f"Finding the shortest route, Error : {e}")

        except KeyError as ke:
            print(f"Key Invalid, Error : {ke}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    args = parser.parse_args()
    try:
        r = Routes()
        r.prepare_data_source(args.file)
        input_origin = input(str("What station are you getting on the train? : "))
        input_dest = input(str("What station are you getting off the train?: "))
        stop, time = r.find_shortest_route(input_origin, input_dest)
        if time == float("inf") or time == 0:
            print(f"Your trip from {input_origin} to {input_dest}, No routes from {input_origin} to {input_dest}")
        else  :
            print(f"Your trip from {input_origin} to {input_dest} includes {stop} stops and will take {time} minutes")

    except TypeError as te:
        print(f"Invalid input type, Error : {te}")
