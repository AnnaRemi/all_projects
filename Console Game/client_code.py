from functions_for_creating import create_list_of_units, creating_units
from factories.element_factory import ElementFactory


def create_factory(elements, element):
    try:
        if element == 'Q':
            return None
        return elements[element]
    except KeyError:
        return 'Please write element correctly'


def client_code(factory: ElementFactory):
    print('If you want to change element, print Q')
    print(factory.return_message())
    units_for_creating = create_list_of_units(factory)
    units = creating_units(units_for_creating)
