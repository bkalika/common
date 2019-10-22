import unittest

from oop.homework import (Cat,
                          Cheetah,
                          Wall,
                          Roof,
                          Window,
                          Door,
                          House
                          )


class TestCat(unittest.TestCase):
    def setUp(self) -> None:
        self.passed_cats = [
            Cat(1),
            Cat(7),
            Cat(8),
            Cat(10),
            Cat(12),
            Cat(15),
        ]

    def test_average_speed(self):
        expected = [12, 12, 9, 9, 6]
        result = zip(self.passed_cats, expected)
        for cat, exp in result:
            with self.subTest():
                self.assertEqual(cat.average_speed, exp)

    def test_saturation_level(self):
        for cat in self.passed_cats:
            with self.subTest():
                self.assertEqual(cat.saturation_level, 50)

    def test_increase_saturation_level(self):
        expected = [60, 70, 75, 65, 100]
        increase_list = [10, 20, 25, 15, 60]
        all_values = zip(increase_list, expected, self.passed_cats)
        for inc, exp, cat in all_values:
            with self.subTest():
                cat._increase_saturation_level(inc)
                self.assertEqual(cat.saturation_level, exp)

    def test_reduce_saturation_level(self):
        expected = [40, 30, 15, 0]
        reduce_list = [10, 20, 35, 60]
        all_values = zip(reduce_list, expected, self.passed_cats)
        for red, exp, cat in all_values:
            with self.subTest():
                cat._reduce_saturation_level(red)
                self.assertEqual(cat.saturation_level, exp)

    def test_eat(self):
        foods = ["fodder", "apple", "milk", "other food"]
        expected = [60, 55, 52, 50]
        combine = zip(foods, expected, self.passed_cats)
        for food, exp, cat in combine:
            with self.subTest():
                cat.eat(food)
                self.assertEqual(cat.saturation_level, exp)

    def test_run(self):
        reduce_values = [40, 20, 10, 25, 0, 5]
        run_values = [2, 5, 10, 20, 4, 2]
        expected = [8, 15, 25, 0, 48, 43]
        all_values = zip(run_values, expected, reduce_values, self.passed_cats)
        for run, exp, red, cat in all_values:
            with self.subTest():
                cat._reduce_saturation_level(red)
                cat.run(run)
                self.assertEqual(cat.saturation_level, exp)

    def test_get_saturation_level(self):
        reduce_values = [40, 20, 10, 0, 5, 25]
        run_values = [2, 5, 10, 4, 2, 20]
        expected = [8, 15, 25, 45, 43, 'Your cat is died :(']
        all_values = zip(reduce_values, run_values, expected, self.passed_cats)
        for red, run, exp, cat in all_values:
            with self.subTest():
                cat._reduce_saturation_level(red)
                cat.run(run)
                self.assertEqual(cat.get_saturation_level(), exp)

    def test_get_average_speed(self):
        expected = [12, 12, 9, 9, 6, 6]
        all_values = zip(expected, self.passed_cats)
        for exp, cat in all_values:
            with self.subTest():
                cat._set_average_speed()
                self.assertEqual(cat.get_average_speed(), exp)


class TestWall(unittest.TestCase):
    def setUp(self) -> None:
        self.walls = [
            Wall(5, 5), Wall(10, 10), Wall(15, 15), Wall(5, 10),
            Wall(10, 2.5), Wall(10, 2.5), Wall(14, 2.5), Wall(14, 2.5)]

    def test_wall_square(self):
        expected = [25, 100, 225, 50, 25, 25, 35, 35]
        all_values = zip(expected, self.walls)
        for exp, wall in all_values:
            with self.subTest():
                self.assertEqual(wall.wall_square(), exp)

    def test_number_of_rolls_of_wallpaper(self):
        expected = [4.5, 18, 42, 9, 4.5, 4.5, 6.5, 6.5]
        all_values = zip(expected, self.walls)
        for exp, wall in all_values:
            with self.subTest():
                self.assertEqual(wall.number_of_rolls_of_wallpaper(0.53, 10), exp)


class TestRoof(unittest.TestCase):
    def setUp(self) -> None:
        self.roofs = [
            Roof(5, 5, 'gable'),
            Roof(10, 5, 'single-pitch'),
            Roof(3, 7, 'simple roof')
        ]

    def test_roof_type(self):
        expected = [50, 50, "Sorry there is only two types of roofs"]
        all_values = zip(expected, self.roofs)
        for exp, roof in all_values:
            with self.subTest():
                self.assertEqual(roof.roof_square(), exp)


class TestWindow(unittest.TestCase):
    def test_window_square(self):
        window = Window(2, 2)
        self.assertEqual(4, window.window_square())


class TestDoor(unittest.TestCase):
    def setUp(self) -> None:
        self.doors = [
            Door(2, 3),
            Door(2, 4),
            Door(2, 2),
            Door(1, 2)
        ]

    def test_wood_price(self):
        expected = [10] * 4
        all_values = zip(expected, self.doors)
        for exp, door in all_values:
            with self.subTest():
                self.assertEqual(door.wood_price, exp)

    def test_metal_price(self):
        expected = [3] * 4
        all_values = zip(expected, self.doors)
        for exp, door in all_values:
            with self.subTest():
                self.assertEqual(door.metal_price, exp)

    def test_door_square(self):
        expected = [6, 8, 4, 2]
        all_values = zip(expected, self.doors)
        for exp, door in all_values:
            with self.subTest():
                self.assertEqual(door.door_square(), exp)

    def test_door_price(self):
        wood_material = ["wood"] * 4
        metal_material = ["metal"] * 4
        other_material = ["plastic"] * 4
        expected_wood = [60, 80, 40, 20]
        expected_metal = [18, 24, 12, 6]
        expected_plastic = ["Sorry we don't have such material"] * 4
        all_values_wood = zip(wood_material, expected_wood, self.doors)
        all_values_metal = zip(metal_material, expected_metal, self.doors)
        all_values_plastic = zip(other_material, expected_plastic, self.doors)
        for wood, exp, door in all_values_wood:
            with self.subTest():
                self.assertEqual(exp, door.door_price(wood))
        for metal, exp, door in all_values_metal:
            with self.subTest():
                self.assertEqual(exp, door.door_price(metal))
        for plastic, exp, door in all_values_plastic:
            with self.subTest():
                self.assertEqual(exp, door.door_price(plastic))

    def test_update_wood_price(self):
        price = Door(2, 3)
        price.update_wood_price(5)
        self.assertEqual(5, price.wood_price)

    def test_update_metal_price(self):
        price = Door(2, 1)
        price.update_metal_price(7)
        self.assertEqual(7, price.metal_price)


class TestHouse(unittest.TestCase):
    def setUp(self) -> None:
        self.house = [
            House(),
        ]

    def test_get_count_of_walls(self):
        wall = House()
        wall_meter = [wall.create_wall(2, 2), wall.create_wall(2, 3), wall.create_wall(5, 2), wall.create_wall(5, 5)]
        self.assertEqual(4, wall.get_count_of_walls())

    def test_get_count_of_windows(self):
        window = House()
        window.create_window(2, 1)
        self.assertEqual(1, window.get_count_of_windows())

    def test_get_door_price(self):
        price = House()
        price.create_door(2, 2)
        self.assertEqual(40, price.get_door_price("wood"))

    def test_update_wood_price(self):
        price = House()
        price.create_door(2, 2)
        price.update_wood_price(40)
        self.assertEqual(160, price.get_door_price("wood"))

    def test_update_metal_price(self):
        price = House()
        price.create_door(2, 2)
        price.update_metal_price(15)
        self.assertEqual(60, price.get_door_price("metal"))

    def test_roof_square(self):
        roof = House()
        roof.create_roof(2, 2, "gable")
        self.assertEqual(8, roof.get_roof_square())

    def test_sum_of_walls_square(self):
        result = [4, 29, 38, 54]
        wall_h_w = [2, 5, 3, 4]
        wall = House()
        split = zip(wall_h_w, result)
        for w, res in split:
            with self.subTest():
                wall.create_wall(w, w)
                self.assertEqual(res, wall.get_walls_square())
        for w, res in split:
            result.append(2)
            wall_h_w.append(2)
            with self.assertRaises(ValueError):
                wall.create_wall(w, w)

    def test_get_windows_square(self):
        result = [4, 29, 38, 54]
        window_h_w = [2, 5, 3, 4]
        window = House()
        split = zip(window_h_w, result)
        for w, res in split:
            window.create_window(w, w)
            self.assertEqual(res, window.get_windows_square())
        for w in split:
            result.append(0)
            window_h_w.append(0)
            with self.assertRaises(ValueError):
                window.create_window(w, w)

    def test_get_door_square(self):
        door = House()
        result = [4]
        door_h_w = [2]
        split = zip(door_h_w, result)
        for d, res in split:
            door.create_door(d, d)
            self.assertEqual(res, door.get_door_square())
        for d in split:
            result.append(5)
            door_h_w.append(5)
            with self.assertRaises(ValueError):
                door.create_door(d, d)

    def test_number_of_rolls_of_wallpapers(self):
        roll = House()
        roll.create_wall(20, 10)
        self.assertEqual(25.0, roll.get_number_of_rolls_of_wallpapers(2, 4))


if __name__ == "__main__":
    unittest.main()
