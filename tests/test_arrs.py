import unittest
from utils import arrs

class TestArrs(unittest.TestCase):

    def test_get_existing_index(self):
        array = [1, 2, 3, 4, 5]
        result = arrs.get(array, 2, "default")
        self.assertEqual(result, 3)

    def test_get_nonexistent_index(self):
        array = [1, 2, 3, 4, 5]
        result = arrs.get(array, 10, "default")
        self.assertEqual(result, "default")

    def test_get_negative_index(self):
        array = [1, 2, 3, 4, 5]
        result = arrs.get(array, -1, "default")
        self.assertEqual(result, 5, "Expected result to be 5")

    def test_my_slice_full_range(self):
        array = [1, 2, 3, 4, 5]
        result = arrs.my_slice(array)
        self.assertEqual(result, array)

    def test_my_slice_start_end(self):
        array = [1, 2, 3, 4, 5]
        result = arrs.my_slice(array, 1, 4)
        self.assertEqual(result, [2, 3, 4])

    def test_my_slice_negative_start_end(self):
        array = [1, 2, 3, 4, 5]
        result = arrs.my_slice(array, -3, -1)
        self.assertEqual(result, [3, 4])

    def test_my_slice_negative_start(self):
        array = [1, 2, 3, 4, 5]
        result = arrs.my_slice(array, -3)
        self.assertEqual(result, [3, 4, 5])

    def test_my_slice_negative_end(self):
        array = [1, 2, 3, 4, 5]
        result = arrs.my_slice(array, end=-2)
        self.assertEqual(result, [1, 2, 3])

    def test_get_out_of_bounds_negative_index(self):
        array = [1, 2, 3, 4, 5]
        result = arrs.get(array, -10, "default")
        self.assertEqual(result, "default", "Expected result to be 'default' for out of bounds index")


