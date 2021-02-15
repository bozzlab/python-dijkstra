from typing import List, Tuple, Dict, Set, TextIO
import argparse
import csv

class Routes:
    """ Routes """
    def __init__(self):
        self.routes_data : List = list()
        self.routes_paths : Dict = dict()
        self.shortest_path : List = list()
        self.__stations : Set = set()
        self.origin : str = str()
        self.dest : str = str()

    def read_csv(
                self, 
                filename : TextIO
                ) -> None:
        """ 
        Read the csv file, Then collect to list. 
        """
        with open(filename) as csv_file:
            self.routes_data = [(row[0],row[1], int(row[2])) 
                                for row in csv.reader(csv_file, delimiter = ',')] 
    
    def __prepare_data(self):
        """ 
        counting the unique station and collecting the direct path for each station  
        """
        [self.__stations.update(row[0], row[1]) for row in self.routes_data] 
        self.routes_paths = {station : {} for station in self.__stations} 
        [self.routes_paths[row[0]].update({row[1] : row[2]}) for row in self.routes_data] 

    def __find_shortest_path(self) -> Tuple[int, int]:
        """ 
        Finding the shortest path for each origin to dest.

        Returns:
            (int, int) : stop step and total time
        """
        time_to_dest = {station : float("inf") if station != self.origin else 0 for station in self.__stations}
        unreach_stations = sorted([station for station in self.__stations])
        reach_stations = {station : None for station in self.__stations}
        is_paths_incomplete = True

        while unreach_stations:
            for station, time in self.routes_paths[unreach_stations[0]].items():
                time_path = time_to_dest[unreach_stations[0]] + time
                if time_to_dest[station] > time_path:
                    time_to_dest[station] = time_path
                    reach_stations[station] = unreach_stations[0]
            unreach_stations.remove(unreach_stations[0])

        while is_paths_incomplete:
            next_path = self.dest
            for node in reach_stations:
                if reach_stations[next_path] != None:
                    self.shortest_path.append(reach_stations[next_path])
                    next_path = reach_stations[next_path]
            is_paths_incomplete = False

        if self.shortest_path:
            self.shortest_path.insert(0, self.dest)
            self.shortest_path.reverse()
        
        return len([station for station in self.shortest_path if station not in [self.origin, self.dest]]), time_to_dest[self.dest]

    def get_shortest_path(self) -> Dict[str,int]:
        """
        Get the shortest path.  

        Returns:
            Dict(str, int) : Result of shortest path including Stop and Total time.          
        """
        self.__prepare_data()
        if self.origin not in self.__stations or self.dest not in self.__stations:
            print("Invalid Input")
            return

        stop, total_time = self.__find_shortest_path()

        if total_time == float("inf") or total_time == 0:
            print(f"Your trip from {self.origin} to {self.dest}, No routes from {self.origin} to {self.dest}")
            return

        return {"stop" : stop, "total_time" : total_time}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    args = parser.parse_args()
    try:
        r = Routes()
        r.read_csv(args.file)
        r.origin = input(str("What station are you getting on the train? : "))
        r.dest = input(str("What station are you getting off the train?: "))
        result = r.get_shortest_path()
        if result:
            print(f"Your trip from {r.origin} to {r.dest} includes {result['stop']} stops and will take {result['total_time']} minutes")
    except TypeError as te:
        print(f"Invalid input type, Error : {te}")
