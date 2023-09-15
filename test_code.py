import unittest
from main_programm import Ch3 

class TestCh3(unittest.TestCase):
    # Existing test

    def test_move_forward(self):
        chandrayaan = Ch3()
        chandrayaan.move('f','N')
        self.assertEqual(chandrayaan.getPosition(), [0, 1, 0])

    def test_move_backward(self):
        chandrayaan = Ch3()
        chandrayaan.move('b','N')
        self.assertEqual(chandrayaan.getPosition(), [0, -1, 0])

    def test_turn_left(self):
        chandrayaan = Ch3()
        chandrayaan.turn('l','N')
        self.assertEqual(chandrayaan.getDirection(), 'W')

    def test_turn_right(self):
        chandrayaan = Ch3()
        chandrayaan.turn('r','E')
        self.assertEqual(chandrayaan.getDirection(), 'S')

    def test_tilt_up(self):
        chandrayaan = Ch3()
        chandrayaan.tilt('u','N')
        self.assertEqual(chandrayaan.getDirection(), 'U')

    def test_tilt_down(self):
        chandrayaan = Ch3()
        chandrayaan.tilt('d','S')
        self.assertEqual(chandrayaan.getDirection(), 'D')

    def test_sequence_of_commands(self):
        chandrayaan = Ch3()
        commands = ['f', 'r', 'u', 'b', 'l']
        chandrayaan.execute_commands(commands)
        self.assertEqual(chandrayaan.getPosition(), [0, 1, -1])
        self.assertEqual(chandrayaan.getDirection(), 'N')

        cmd=['b','l','u','r','f','f','l']
        chandrayaan.execute_commands(cmd)
        self.assertEqual(chandrayaan.getPosition(), [0, 2, -1])
        self.assertEqual(chandrayaan.getDirection(), 'W')

        cmd2=['f','f','u','u','l','l','b','b']
        chandrayaan.execute_commands(cmd2)
        self.assertEqual(chandrayaan.getPosition(), [-4, 2, -1])
        self.assertEqual(chandrayaan.getDirection(), 'E')

