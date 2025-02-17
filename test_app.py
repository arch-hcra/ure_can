# test_app.py

import unittest
from app import add, subtract

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(5, 5), 0)
        self.assertEqual(subtract(10**6, 10**5), 900000)
     with self.assertRaises(TypeError):
        add("a", 1)
    with self.assertRaises(TypeError):
       subtract(1, "b")

if __name__ == "__main__":
    unittest.main()
