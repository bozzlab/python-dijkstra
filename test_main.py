from main import Routes
import unittest

class TestRoutes(unittest.TestCase):
    def test_case_a_b(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "A"
        r.dest = "B"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 0)
        self.assertEqual(result["total_time"], 5)
        self.assertEqual(r.shortest_path, ["A","B"])

    def test_case_a_c(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "A"
        r.dest = "C"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 1)
        self.assertEqual(result["total_time"], 10)
        self.assertEqual(r.shortest_path, ["A","B","C"])

    def test_case_a_d(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "A"
        r.dest = "D"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 0)
        self.assertEqual(result["total_time"], 15)
        self.assertEqual(r.shortest_path, ["A","D"])

    def test_case_a_e(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "A"
        r.dest = "E"
        result = r.get_shortest_path()
        self.assertEqual(result, None)
        self.assertEqual(r.shortest_path, [])        

    def test_case_b_c(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "B"
        r.dest = "C"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 0)
        self.assertEqual(result["total_time"], 5)
        self.assertEqual(r.shortest_path, ['B','C'])

    def test_case_b_d(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "B"
        r.dest = "D"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 1)
        self.assertEqual(result["total_time"], 12)
        self.assertEqual(r.shortest_path, ['B','C','D'])

    def test_case_c_d(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "C"
        r.dest = "D"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 0)
        self.assertEqual(result["total_time"], 7)
        self.assertEqual(r.shortest_path, ['C','D'])

    def test_case_e_f(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "E"
        r.dest = "F"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 0)
        self.assertEqual(result["total_time"], 5)
        self.assertEqual(r.shortest_path, ['E','F'])

    def test_case_e_g(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "E"
        r.dest = "G"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 1)
        self.assertEqual(result["total_time"], 10)
        self.assertEqual(r.shortest_path, ['E','F','G'])

    def test_case_e_h(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "E"
        r.dest = "H"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 2)
        self.assertEqual(result["total_time"], 20)
        self.assertEqual(r.shortest_path, ['E','F','G','H'])

    def test_case_e_i(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "E"
        r.dest = "I"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 3)
        self.assertEqual(result["total_time"], 30)
        self.assertEqual(r.shortest_path, ['E','F','G','H','I'])

    def test_case_e_j(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "E"
        r.dest = "J"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 2)
        self.assertEqual(result["total_time"], 30)
        self.assertEqual(r.shortest_path, ['E', 'F', 'G', 'J'])

    def test_case_f_g(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "F"
        r.dest = "G"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 0)
        self.assertEqual(result["total_time"], 5)
        self.assertEqual(r.shortest_path, ['F','G'])

    def test_case_f_h(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "F"
        r.dest = "H"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 1)
        self.assertEqual(result["total_time"], 15)
        self.assertEqual(r.shortest_path, ['F','G','H'])
    
    def test_case_f_i(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "F"
        r.dest = "I"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 2)
        self.assertEqual(result["total_time"], 25)
        self.assertEqual(r.shortest_path, ['F','G','H','I'])

    def test_case_f_j(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "F"
        r.dest = "J"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 1)
        self.assertEqual(result["total_time"], 25)
        self.assertEqual(r.shortest_path, ['F','G','J'])

    def test_case_g_h(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "G"
        r.dest = "H"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 0)
        self.assertEqual(result["total_time"], 10)
        self.assertEqual(r.shortest_path, ['G','H'])

    def test_case_g_i(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "G"
        r.dest = "I"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 1)
        self.assertEqual(result["total_time"], 20)
        self.assertEqual(r.shortest_path, ['G','H','I'])

    def test_case_g_j(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "G"
        r.dest = "J"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 0)
        self.assertEqual(result["total_time"], 20)
        self.assertEqual(r.shortest_path, ['G','J'])

    def test_case_h_i(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "H"
        r.dest = "I"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 0)
        self.assertEqual(result["total_time"], 10)
        self.assertEqual(r.shortest_path, ["H", "I"])

    def test_case_h_j(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "H"
        r.dest = "J"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 1)
        self.assertEqual(result["total_time"], 15)
        self.assertEqual(r.shortest_path, ["H", "I","J"])

    def test_case_i_j(self):
        r = Routes()
        r.read_csv("routes.csv")
        r.origin = "I"
        r.dest = "J"
        result = r.get_shortest_path()
        self.assertEqual(result["stop"], 0)
        self.assertEqual(result["total_time"], 5)
        self.assertEqual(r.shortest_path, ['I','J'])