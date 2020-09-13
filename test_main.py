from main import Routes
import unittest

r = Routes()
r.prepare_data_source("routes.csv")

class TestRoutes(unittest.TestCase):
    """ Testing only origin routing possible """
    def test_case_a_b(self):
        stop, time = r.find_shortest_route("A", "B")
        self.assertEqual(stop, 0)
        self.assertEqual(time, 5)
        self.assertEqual(r.shortest_path, ['A','B'])

    def test_case_a_c(self):
        stop, time = r.find_shortest_route("A", "C")
        self.assertEqual(stop, 1)
        self.assertEqual(time, 10)
        self.assertEqual(r.shortest_path, ['A','B','C'])

    def test_case_a_d(self):
        stop, time = r.find_shortest_route("A", "D")
        self.assertEqual(stop, 0)
        self.assertEqual(time, 15)
        self.assertEqual(r.shortest_path, ['A','D'])

    def test_case_a_e(self):
        stop, time = r.find_shortest_route("A", "E")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_a_f(self):
        stop, time = r.find_shortest_route("A", "F")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_a_h(self):
        stop, time = r.find_shortest_route("A", "H")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_a_i(self):
        stop, time = r.find_shortest_route("A", "I")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_a_j(self):
        stop, time = r.find_shortest_route("A", "J")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_b_a(self):
        stop, time = r.find_shortest_route("B", "A")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_b_c(self):
        stop, time = r.find_shortest_route("B", "C")
        self.assertEqual(stop, 0)
        self.assertEqual(time, 5)
        self.assertEqual(r.shortest_path, ['B','C'])

    def test_case_b_d(self):
        stop, time = r.find_shortest_route("B", "D")
        self.assertEqual(stop, 1)
        self.assertEqual(time, 12)
        self.assertEqual(r.shortest_path, ['B','C','D'])

    def test_case_b_e(self):
        stop, time = r.find_shortest_route("B", "E")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_b_f(self):
        stop, time = r.find_shortest_route("B", "F")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_b_g(self):
        stop, time = r.find_shortest_route("B", "G")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_b_h(self):
        stop, time = r.find_shortest_route("B", "H")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_b_i(self):
        stop, time = r.find_shortest_route("B", "I")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_b_j(self):
        stop, time = r.find_shortest_route("B", "J")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_c_a(self):
        stop, time = r.find_shortest_route("C", "A")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_c_b(self):
        stop, time = r.find_shortest_route("C", "B")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_c_d(self):
        stop, time = r.find_shortest_route("C", "D")
        self.assertEqual(stop, 0)
        self.assertEqual(time, 7)
        self.assertEqual(r.shortest_path, ['C','D'])

    def test_case_c_e(self):
        stop, time = r.find_shortest_route("C", "E")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_c_f(self):
        stop, time = r.find_shortest_route("C", "F")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_c_h(self):
        stop, time = r.find_shortest_route("C", "H")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_c_i(self):
        stop, time = r.find_shortest_route("C", "I")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_d_error(self):
        """ D not in origin """
        stop, time = r.find_shortest_route("D", "A")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_e_a(self):
        stop, time = r.find_shortest_route("E", "A")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_e_b(self):
        stop, time = r.find_shortest_route("E", "B")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_e_c(self):
        stop, time = r.find_shortest_route("E", "C")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_e_d(self):
        stop, time = r.find_shortest_route("E", "D")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_e_f(self):
        stop, time = r.find_shortest_route("E", "F")
        self.assertEqual(stop, 0)
        self.assertEqual(time, 5)
        self.assertEqual(r.shortest_path, ['E','F'])

    def test_case_e_g(self):
        stop, time = r.find_shortest_route("E", "G")
        self.assertEqual(stop, 1)
        self.assertEqual(time, 10)
        self.assertEqual(r.shortest_path, ['E','F','G'])

    def test_case_e_h(self):
        stop, time = r.find_shortest_route("E", "H")
        self.assertEqual(stop, 2)
        self.assertEqual(time, 20)
        self.assertEqual(r.shortest_path, ['E','F','G','H'])

    def test_case_e_i(self):
        stop, time = r.find_shortest_route("E", "I")
        self.assertEqual(stop, 3)
        self.assertEqual(time, 30)
        self.assertEqual(r.shortest_path, ['E','F','G','H','I'])

    def test_case_e_j(self):
        stop, time = r.find_shortest_route("E", "J")
        self.assertEqual(stop, 2)
        self.assertEqual(time, 30)
        self.assertEqual(r.shortest_path, ['E', 'F', 'G', 'J'])

    def test_case_f_a(self):
        stop, time = r.find_shortest_route("F", "A")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_f_b(self):
        stop, time = r.find_shortest_route("F", "B")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_f_c(self):
        stop, time = r.find_shortest_route("F", "C")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_f_d(self):
        stop, time = r.find_shortest_route("F", "D")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_f_e(self):
        stop, time = r.find_shortest_route("F", "E")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_f_g(self):
        stop, time = r.find_shortest_route("F", "G")
        self.assertEqual(stop, 0)
        self.assertEqual(time, 5)
        self.assertEqual(r.shortest_path, ['F','G'])

    def test_case_f_h(self):
        stop, time = r.find_shortest_route("F", "H")
        self.assertEqual(stop, 1)
        self.assertEqual(time, 15)
        self.assertEqual(r.shortest_path, ['F','G','H'])

    def test_case_f_i(self):
        stop, time = r.find_shortest_route("F", "I")
        self.assertEqual(stop, 2)
        self.assertEqual(time, 25)
        self.assertEqual(r.shortest_path, ['F','G','H','I'])

    def test_case_f_j(self):
        stop, time = r.find_shortest_route("F", "J")
        self.assertEqual(stop, 1)
        self.assertEqual(time, 25)
        self.assertEqual(r.shortest_path, ['F','G','J'])

    def test_case_g_a(self):
        stop, time = r.find_shortest_route("G", "A")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])
        
    def test_case_g_b(self):
        stop, time = r.find_shortest_route("G", "B")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_g_c(self):
        stop, time = r.find_shortest_route("G", "C")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_g_d(self):
        stop, time = r.find_shortest_route("G", "D")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_g_f(self):
        stop, time = r.find_shortest_route("G", "F")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_g_h(self):
        stop, time = r.find_shortest_route("G", "H")
        self.assertEqual(stop, 0)
        self.assertEqual(time, 10)
        self.assertEqual(r.shortest_path, ['G','H'])

    def test_case_g_i(self):
        stop, time = r.find_shortest_route("G", "I")
        self.assertEqual(stop, 1)
        self.assertEqual(time, 20)
        self.assertEqual(r.shortest_path, ['G','H','I'])

    def test_case_g_j(self):
        stop, time = r.find_shortest_route("G", "J")
        self.assertEqual(stop, 0)
        self.assertEqual(time, 20)
        self.assertEqual(r.shortest_path, ['G','J'])

    def test_case_h_a(self):
        stop, time = r.find_shortest_route("H", "A")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_h_b(self):
        stop, time = r.find_shortest_route("H", "B")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_h_c(self):
        stop, time = r.find_shortest_route("H", "C")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_h_d(self):
        stop, time = r.find_shortest_route("H", "D")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_h_e(self):
        stop, time = r.find_shortest_route("H", "E")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_h_f(self):
        stop, time = r.find_shortest_route("H", "F")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_h_g(self):
        stop, time = r.find_shortest_route("H", "G")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_h_i(self):
        stop, time = r.find_shortest_route("H", "I")
        self.assertEqual(stop, 0)
        self.assertEqual(time, 10)
        self.assertEqual(r.shortest_path, ["H", "I"])

    def test_case_h_j(self):
        stop, time = r.find_shortest_route("H", "J")
        self.assertEqual(stop, 1)
        self.assertEqual(time, 15)
        self.assertEqual(r.shortest_path, ["H", "I","J"])

    def test_case_i_a(self):
        stop, time = r.find_shortest_route("I", "A")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_i_b(self):
        stop, time = r.find_shortest_route("I", "B")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_i_c(self):
        stop, time = r.find_shortest_route("I", "C")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_i_d(self):
        stop, time = r.find_shortest_route("I", "D")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_i_e(self):
        stop, time = r.find_shortest_route("I", "E")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_i_f(self):
        stop, time = r.find_shortest_route("I", "F")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_i_g(self):
        stop, time = r.find_shortest_route("I", "G")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_i_h(self):
        stop, time = r.find_shortest_route("I", "H")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

    def test_case_i_j(self):
        stop, time = r.find_shortest_route("I", "J")
        self.assertEqual(stop, 0)
        self.assertEqual(time, 5)
        self.assertEqual(r.shortest_path, ['I','J'])

    def test_case_j_error(self):
        """ J not in origin """
        stop, time = r.find_shortest_route("J", "A")
        self.assertEqual(stop, 0)
        self.assertEqual(time, float("inf"))
        self.assertEqual(r.shortest_path, [])

if __name__ == "__main__":
    TestRoutes()