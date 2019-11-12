from factories.air_element_factory import AirElementFactory
from factories.earth_element_factory import EarthElementFactory
from factories.fire_element_factory import FireElementFactory
from factories.water_element_factory import WaterElementFactory
from units.magic_girl import MagicGirl
from units.magic_boy import MagicBoy
from units.magic_animal import MagicAnimal


def create_elements():
    elements = {}
    elements['Air'] = AirElementFactory()
    elements['Water'] = WaterElementFactory()
    elements['Fire'] = FireElementFactory()
    elements['Earth'] = EarthElementFactory()
    return elements


def create_list_of_units(factory):
    return {
        'girl': factory.create_magic_girl,
        'boy': factory.create_magic_boy,
        'animal': factory.create_magic_animal,
        'creating_unit': factory.can_create_magic_unit,
        'price_girl': MagicGirl.price,
        'price_boy': MagicBoy.price,
        'price_animal': MagicAnimal.price,
        'message': factory.return_message
    }


def creating_units(units_for_creating):
    units = {}
    current_unit = None
    while current_unit != 'Q':
        print('Choose kind of unit: girl (30 coins), '
              'boy (30 coins) or animal (15 coins)')
        current_unit = input()
        if current_unit == 'Q':
            break
        else:
            new_unit = create_concrete_unit(current_unit, units_for_creating)
            if isinstance(new_unit, str):
                print(new_unit)
            elif new_unit is not None:
                print('Write a name of your new magic unit')
                current_name = input()
                units[current_name] = new_unit
                print(units_for_creating['message']())
    return units


def create_concrete_unit(current_unit, units_for_creating):
    try:
        new_unit = units_for_creating['creating_unit'](
            units_for_creating[f'price_{current_unit}'],
            units_for_creating[current_unit])
        return new_unit
    except KeyError:
        return 'Please write again correctly'
