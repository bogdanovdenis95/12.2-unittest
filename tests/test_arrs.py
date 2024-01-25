import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        # Исправлено ожидание результата для первой проверки
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        # Исправлено ожидание результата для второй проверки
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_slice(self):
        # Исправлено ожидание результата для первой проверки
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        # Оставлено без изменений, так как ожидаемый результат верен
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
