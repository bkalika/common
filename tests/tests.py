import unittest
from math import sqrt

from homework import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.passed = [Rectangle(2, 2), Rectangle(2, 3), Rectangle(25, 25), Rectangle(20, 30), Rectangle(True, True),
                       Rectangle(True, False), Rectangle(-1, -1), Rectangle(20, -20), Rectangle(20, -10)]
        self.failed = [Rectangle(0, 0), Rectangle(False, False), Rectangle(False, True), Rectangle(True, False),
                       Rectangle(10, None), Rectangle(None, 10), Rectangle(None, None)]

    def test_get_rectangle_perimeter_passed(self):
        expected = [8, 10, 100, 100, 4, 2, -4, 0, 20]
        result = zip(self.passed, expected)
        for rect, exp in result:
            with self.subTest():
                self.assertEqual(rect.get_rectangle_perimeter(), exp)
                self.assertIsInstance(rect.get_rectangle_perimeter(), int)
                self.assertIsNotNone(rect.get_rectangle_perimeter())

    def test_get_rectangle_square_passed(self):
        expected = [4, 6, 625, 600, 1, 0, 1, -400, -200]
        result = zip(self.passed, expected)
        for rect, exp in result:
            with self.subTest():
                self.assertEqual(rect.get_rectangle_square(), exp)
                self.assertIsInstance(rect.get_rectangle_square(), int)
                self.assertIsNotNone(rect.get_rectangle_square())

    def test_get_sum_of_corners_passed(self):
        for all_rect in range(9):
            for sum_of_corners in range(1, 5):
                self.assertEqual(self.passed[all_rect].get_sum_of_corners(sum_of_corners), sum_of_corners*90)
                self.assertIsInstance(self.passed[all_rect].get_sum_of_corners(sum_of_corners), int)
                self.assertIsNotNone(self.passed[all_rect].get_sum_of_corners(sum_of_corners))

    def test_get_rectangle_diagonal_passed(self):
        expected = [8, 13, 1250, 1300, 2]
        result = zip(self.passed, expected)
        for rect, exp in result:
            with self.subTest():
                self.assertAlmostEqual(rect.get_rectangle_diagonal(), sqrt(exp), places=2)
                self.assertIsNotNone(rect.get_rectangle_diagonal())

    def test_get_radius_of_circumscribed_circle_passed(self):
        expected = [8, 13, 1250, 1300, 2]
        result = zip(self.passed, expected)
        for rect, exp in result:
            with self.subTest():
                self.assertAlmostEqual(rect.get_radius_of_circumscribed_circle(), sqrt(exp)/2, places=2)
                self.assertIsNotNone(rect.get_radius_of_circumscribed_circle())

    def test_get_rectangle_perimeter_failed(self):
        expected = [0] * 2
        result = zip(self.failed, expected)
        result_for_none = list(zip(self.failed[4:6:1], expected))
        for rect, exp in result:
            with self.subTest():
                self.assertLessEqual(rect.get_rectangle_perimeter(), exp)
                self.assertFalse(rect.get_rectangle_perimeter(), exp)
        for rect_for_none, exp in result_for_none:
            with self.subTest():
                with self.assertRaises(TypeError):
                    rect_for_none.get_rectangle_perimeter()

    def test_get_rectangle_square_failed(self):
        expected = [0] * 2
        result = zip(self.failed, expected)
        result_for_none = self.failed[4:7]
        for rect, exp in result:
            with self.subTest():
                self.assertFalse(rect.get_rectangle_square(), exp)
        for rect in result_for_none:
            with self.subTest():
                with self.assertRaises(TypeError):
                    rect.get_rectangle_square()

    def test_get_sum_of_corners_failed(self):
        for all_rect in self.failed:
            with self.subTest():
                for sum_of_corners in range(5, 20):
                    with self.assertRaises(ValueError):
                        all_rect.get_sum_of_corners(sum_of_corners), sum_of_corners * 90

    def test_get_rectangle_diagonal_failed(self):
        for rect in self.failed[0:2]:
            with self.subTest():
                with self.assertRaises(ValueError):
                    rect.get_rectangle_diagonal()

    def test_get_radius_of_circumscribed_circle_failed(self):
        for rect in self.failed[3:4]:
            with self.subTest():
                with self.assertRaises(ValueError):
                    rect.get_radius_of_circumscribed_circle()
        for rect2 in self.failed[4:7]:
            with self.subTest():
                with self.assertRaises(TypeError):
                    rect2.get_radius_of_circumscribed_circle()

    def test_get_radius_of_inscribed_circle_failed(self):
        for rect in self.failed[:6]:
            with self.subTest():
                with self.assertRaises(ValueError):
                    rect.get_radius_of_inscribed_circle()
        with self.assertRaises(TypeError):
            self.failed[6].get_radius_of_inscribed_circle()


if __name__ == "__main__":
    unittest.main()
