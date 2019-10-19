import unittest

from oop.homework import (Cat,
                          Wall,
                          Roof,
                          Window,
                          Door,
                          House
                          )


class TestCat(unittest.TestCase):
    def test_average_speed(self):
        my_cat1 = Cat(1)
        my_cat2 = Cat(7)
        my_cat3 = Cat(8)
        my_cat4 = Cat(10)
        my_cat5 = Cat(12)
        self.assertEqual(my_cat1.average_speed, 12)
        self.assertEqual(my_cat2.average_speed, 12)
        self.assertEqual(my_cat3.average_speed, 9)
        self.assertEqual(my_cat4.average_speed, 9)
        self.assertEqual(my_cat5.average_speed, 6)

    def test_saturation_level(self):
        self.assertEqual(Cat.saturation_level, 50)

    def test_increase_saturation_level(self):
        my_cat = Cat(1)
        my_cat2 = Cat(2)
        my_cat._increase_saturation_level(10)
        my_cat2._increase_saturation_level(60)
        self.assertEqual(my_cat.saturation_level, 60)
        self.assertEqual(my_cat2.saturation_level, 100)

    def test_reduce_saturation_level(self):
        my_cat = Cat(1)
        my_cat2 = Cat(2)
        my_cat._reduce_saturation_level(10)
        my_cat2._reduce_saturation_level(60)
        self.assertEqual(my_cat.saturation_level, 40)
        self.assertEqual(my_cat2.saturation_level, 0)

    def test_eat(self):
        my_cat = Cat(1)
        my_cat2 = Cat(2)
        my_cat3 = Cat(6)
        my_cat.eat("fodder")
        my_cat2.eat("apple")
        my_cat3.eat("milk")
        self.assertEqual(my_cat.saturation_level, 60)
        self.assertEqual(my_cat2.saturation_level, 55)
        self.assertEqual(my_cat3.saturation_level, 52)

    def test_run(self):
        my_cat1 = Cat(1)
        my_cat2 = Cat(7)
        my_cat3 = Cat(8)
        my_cat4 = Cat(10)
        my_cat5 = Cat(12)
        my_cat6 = Cat(15)
        my_cat1._set_average_speed()
        my_cat2._set_average_speed()
        my_cat3._set_average_speed()
        my_cat4._set_average_speed()
        my_cat5._set_average_speed()
        my_cat6._set_average_speed()
        my_cat6._reduce_saturation_level(40)
        my_cat1.run(2)
        my_cat2.run(5)
        my_cat3.run(10)
        my_cat4.run(20)
        my_cat5.run(40)
        my_cat6.run(40)
        self.assertEqual(my_cat1.saturation_level, 48)
        self.assertEqual(my_cat2.saturation_level, 35)
        self.assertEqual(my_cat3.saturation_level, 35)
        self.assertEqual(my_cat4.saturation_level, 25)
        self.assertEqual(my_cat5.saturation_level, 0)
        self.assertEqual(my_cat6.saturation_level, 0)

    def test_get_saturation_level(self):
        my_cat1 = Cat(12)
        my_cat1._set_average_speed()
        my_cat1._reduce_saturation_level(40)
        my_cat1.run(10)
        my_cat1.get_saturation_level()
        self.assertEqual(my_cat1.get_saturation_level(), 'Your cat is died :(')

    def test_get_average_speed(self):
        my_cat1 = Cat(12)
        my_cat1._set_average_speed()
        self.assertEqual(my_cat1.get_average_speed(), 6)


class TestWall(unittest.TestCase):
    def test_wall_square(self):
        wall1 = Wall(5, 5)
        self.assertEqual(wall1.wall_square(), 25)

    def test_number_of_rolls_of_wallpaper(self):
        wall1 = [Wall(10, 2.5), Wall(10, 2.5), Wall(14, 2.5), Wall(14, 2.5)]
        self.assertEqual(wall1[1].number_of_rolls_of_wallpaper(0.53, 10), 4.5)


class TestRoof(unittest.TestCase):
    def test_roof_type(self):
        roof1 = Roof(5, 5, 'gable')
        roof2 = Roof(10, 5, 'single-pitch')
        roof3 = Roof(3, 7, 'simple roof')
        self.assertEqual(50, roof1.roof_square())
        self.assertEqual(50, roof2.roof_square())
        with self.assertRaises(ValueError):
            roof3.roof_square()


class TestWindow(unittest.TestCase):
    def test_window_square(self):
        window1 = Window(2, 2)
        self.assertEqual(4, window1.window_square())


class TestDoor(unittest.TestCase):
    def test_wood_price(self):
        price1 = Door(2, 3)
        self.assertEqual(10, price1.wood_price)

    def test_metal_price(self):
        price1 = Door(2, 4)
        self.assertEqual(3, price1.metal_price)

    def test_door_square(self):
        door1 = Door(2, 3)
        self.assertEqual(6, door1.door_square())

    def test_door_price(self):
        price1 = Door(2, 3)
        price2 = Door(2, 2)
        price3 = Door(1, 2)
        self.assertEqual(60, price1.door_price('wood'))
        self.assertEqual(12, price2.door_price('metal'))
        with self.assertRaises(ValueError):
            price3.door_price("plastic")

    def test_update_wood_price(self):
        price1 = Door(2, 3)
        price1.update_wood_price(5)
        self.assertEqual(5, price1.wood_price)

    def test_update_metal_price(self):
        price1 = Door(2, 1)
        price1.update_metal_price(7)
        self.assertEqual(7, price1.metal_price)


class TestHouse(unittest.TestCase):
    def test_get_count_of_walls(self):
        wall1 = House()
        # wall2 = House()
        # wall3 = House()
        wall1.create_wall(3, 2)
        # wall2.create_wall(2, 2)
        # wall3.create_wall(2, 3)
        self.assertEqual(1, wall1.get_count_of_walls())
        # self.assertEqual(1, wall2.get_count_of_walls())
        # self.assertEqual(2, wall3.get_count_of_walls())

    def test_get_count_of_windows(self):
        window1 = House()
        window1.create_window(2, 1)
        self.assertEqual(1, window1.get_count_of_windows())

    def test_get_door_price(self):
        price1 = House()
        price1.create_door(2, 2)
        self.assertEqual(40, price1.get_door_price("wood"))

    def test_update_wood_price(self):
        price1 = House()
        price1.create_door(2, 2)
        price1.update_wood_price(40)
        self.assertEqual(160, price1.get_door_price("wood"))

    def test_update_metal_price(self):
        price1 = House()
        price1.create_door(2, 2)
        price1.update_metal_price(15)
        self.assertEqual(60, price1.get_door_price("metal"))

    def test_roof_square(self):
        roof1 = House()
        roof1.create_roof(2, 2, "gable")
        self.assertEqual(8, roof1.get_roof_square())

    def test_sum_of_walls_square(self):
        wall1 = House()
        # wall2 = House()
        # wall3 = House()
        # wall4 = House()
        # wall5 = House()
        wall1.create_wall(2, 2)
        # wall2.create_wall(5, 5)
        # wall3.create_wall(3, 2)
        # wall4.create_wall(4, 4)
        # wall5.create_wall(2, 3)
        # self.assertEqual(4, wall1.get_walls_square())
        # self.assertEqual(29, wall2.get_walls_square())
        # self.assertEqual(35, wall3.get_walls_square())
        # self.assertEqual(5, wall4.get_walls_square())
        # with self.assertRaises(ValueError):
        #     wall5.create_wall(2, 3)

    def test_get_windows_square(self):
        window1 = House()
        # window2 = House()
        # window3 = House()
        window1.create_window(2, 1)
        # window2.create_window(2, 2)
        # self.assertEqual(2, window1.get_windows_square())
        self.assertEqual(4, window1.get_windows_square())
        # with self.assertRaises(ValueError):
        #     window3.create_window(0, 0)

    def test_get_door_square(self):
        door1 = House()
        door2 = House()
        door1.create_door(2, 2)
        # door1.create_door(2, 3)
        # self.assertEqual(5, door1.get_door_square())
        with self.assertRaises(ValueError):
            door1.create_door(0, 0)

    def test_number_of_rolls_of_wallpapers(self):
        roll1 = House()
        # roll = Wall()
        roll1.create_wall(20, 10)
        # roll.number_of_rolls_of_wallpaper(1, 5)
        self.assertEqual(25.5, roll1.get_number_of_rolls_of_wallpapers(2, 4))


if __name__ == "__main__":
    unittest.main()

