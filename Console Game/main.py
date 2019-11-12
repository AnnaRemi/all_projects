from client_code import create_factory, client_code
from functions_for_creating import create_elements


class Game(object):
    elements = create_elements()
    new_element = None
    new_factory = None

    def play(self):
        while self.new_element != 'Q':
            print('If you want to exit, write Q\nChoose element: '
                  'Air, Earth, Water or Fire')
            self.new_element = input()
            self.new_factory = create_factory(self.elements, self.new_element)
            if isinstance(self.new_factory, str):
                print(self.new_factory)
            elif self.new_factory is None:
                break
            else:
                client_code(self.new_factory)


if __name__ == '__main__':
    Game().play()
