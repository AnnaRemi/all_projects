import unittest
from client_code import create_factory
from units.magic_unit import MagicUnit
from units.magic_boy import MagicBoy
from units.magic_girl import MagicGirl
from units.magic_animal import MagicAnimal
from functions_for_creating import create_concrete_unit, \
    create_elements, create_list_of_units
from factories.air_element_factory import AirElementFactory
from factories.earth_element_factory import EarthElementFactory
from factories.fire_element_factory import FireElementFactory
from factories.water_element_factory import WaterElementFactory


class TestUnitMethods(unittest.TestCase):
    def test_create_concrete_unit(self):
        elements = create_elements()
        for factory in elements.values():
            units_for_creating = create_list_of_units(factory)
            self.assertIsInstance(create_concrete_unit
                                  ('girl', units_for_creating),
                                  MagicGirl)
            self.assertIsInstance(create_concrete_unit
                                  ('boy', units_for_creating),
                                  MagicBoy)
            self.assertIsInstance(create_concrete_unit
                                  ('animal', units_for_creating),
                                  MagicAnimal)
            self.assertEqual(create_concrete_unit
                             ('fdfd', units_for_creating),
                             'Please write again correctly')
            self.assertEqual(create_concrete_unit
                             ('gir', units_for_creating),
                             'Please write again correctly')
            self.assertEqual(create_concrete_unit
                             ('girl girl', units_for_creating),
                             'Please write again correctly')
            self.assertEqual(create_concrete_unit
                             ('boy girl', units_for_creating),
                             'Please write again correctly')

    def test_create_factory(self):
        elements = create_elements()
        self.assertEqual(create_factory
                         (elements, 'air'),
                         'Please write element correctly')
        self.assertEqual(create_factory
                         (elements, 'fIre'),
                         'Please write element correctly')
        self.assertEqual(create_factory
                         (elements, 'Air Fire'),
                         'Please write element correctly')
        self.assertEqual(create_factory
                         (elements, 'agsgsgf'),
                         'Please write element correctly')
        self.assertEqual(create_factory
                         (elements, 'Q'), None)
        self.assertIsInstance(create_factory
                              (elements, 'Air'), AirElementFactory)
        self.assertIsInstance(create_factory
                              (elements, 'Earth'), EarthElementFactory)
        self.assertIsInstance(create_factory
                              (elements, 'Water'), WaterElementFactory)
        self.assertIsInstance(create_factory
                              (elements, 'Fire'), FireElementFactory)
        self.assertNotIsInstance(create_factory
                                 (elements, 'Air'), EarthElementFactory)
        self.assertNotIsInstance(create_factory
                                 (elements, 'Water'), FireElementFactory)

    def test_creating_elements(self):
        self.assertIsInstance(create_elements(), dict)
        self.assertIsInstance(create_elements()['Air'], AirElementFactory)
        self.assertIsInstance(create_elements()['Earth'], EarthElementFactory)
        self.assertNotIsInstance(create_elements()['Water'],
                                 FireElementFactory)

    def test_create_list_of_units(self):
        elements = create_elements()
        for factory in elements.values():
            self.assertIsInstance(create_list_of_units(factory), dict)
            self.assertEqual(create_list_of_units(factory)['girl'],
                             factory.create_magic_girl)
            self.assertEqual(create_list_of_units(factory)['price_girl'],
                             MagicGirl.price)
            self.assertEqual(create_list_of_units(factory)['boy'],
                             factory.create_magic_boy)
            self.assertEqual(create_list_of_units(factory)['animal'],
                             factory.create_magic_animal)
            self.assertEqual(create_list_of_units(factory)['creating_unit'],
                             factory.can_create_magic_unit)

    def test_can_create_magic_unit(self):
        elements = create_elements()
        for factory in elements.values():
            self.assertEqual(factory.can_create_magic_unit(
                150,
                factory.create_magic_animal),
                "You don't have enough coins, "
                "please write Q to change element "
                "or choose another element")
            self.assertIsInstance(factory.can_create_magic_unit
                                  (15, factory.create_magic_boy), MagicBoy)
            self.assertEqual(factory.can_create_magic_unit(90, MagicUnit),
                             "You don't have enough coins, please write Q"
                             " to change element or choose another element")
            self.assertIsInstance(factory.can_create_magic_unit
                                  (25, factory.create_magic_girl), MagicGirl)
            self.assertNotIsInstance(factory.can_create_magic_unit
                                     (25, factory.create_magic_animal),
                                     MagicGirl)


if __name__ == '__main__':
    unittest.main()
