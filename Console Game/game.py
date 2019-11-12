from behavior.handler import Handler, CreateElementHandler, CreateUnitsHandler, CreateArmyHandler, CreateSquadHandler
from structure.proxy import Proxy
from structure.component import Component, Composite
from behavior.command import Invoker, AttackReceiver, TreatReceiver, HealthReceiver, ComplexCommand


class Game(object):
    def client_code_creating(self):
        print("Hello, my friend!!"
              " If you want to exit, write 'Q'. Please, choose an element: Air, Earth, Fire or Water.")
        request = input()
        if request == 'Q':
            print("Good bye!")
            return None
        choose_element = CreateElementHandler()
        self.factory = choose_element.handle(request)
        create_units = CreateUnitsHandler(self.factory)
        print("Choose a magic unit: girl(30 coins), boy(30 coins) or animal(15 coins)")
        print(self.factory.return_message())
        request = input()
        self.units = create_units.handle(request)

    def client_code_create_army(self):
        create_army = CreateArmyHandler(self.units)
        create_squad = CreateSquadHandler(self.units)
        create_army.set_next(create_squad)
        # print("Do you want to create a squad? (Yes/no)")
        # request = input()
        new_army = create_army.handle('')
        print("Write a name of your army")
        name = input()
        new_army.name = name
        return Proxy(new_army)

    def client_code_war(self):
        self._invoker = Invoker()
        self._invoker.set_command(ComplexCommand(AttackReceiver()), 'attack')
        self._invoker.set_command(ComplexCommand(TreatReceiver()), 'treat')
        self._invoker.set_command(ComplexCommand(HealthReceiver()), 'health')
        print("Choose a command: attack, treat or health")
        current = input()
        while (current != 'Q'):
            new_armies = self._invoker.do(current.lower(), self._army_1, self._army_2)
            self._army_1 = new_armies[0]
            self._army_2 = new_armies[1]
            print("Choose a command: attack, treat or health")
            current = input()
        print("Good bye!")

    def play(self):
        self.client_code_creating()
        self._army_1 = self.client_code_create_army()
        self.client_code_creating()
        self._army_2 = self.client_code_create_army()
        self.client_code_war()
