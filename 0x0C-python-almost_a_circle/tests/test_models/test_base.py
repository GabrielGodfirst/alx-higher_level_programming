#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_constructor_with_id(self):
        # Test case when id is provided
        obj = Base(id=42)
        self.assertEqual(obj.id, 42)

    def test_constructor_without_id(self):
        # Test case when id is not provided
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)


if __name__ == '__main__':
    unittest.main()
