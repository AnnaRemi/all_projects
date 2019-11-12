from abc import ABC, abstractmethod
from factories.element_factory import ElementFactory


class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass


class ComplexCommand(Command):
    def __init__(self, reciever):
        self._reciever = reciever

    def execute(self, *args):
        return self._reciever.do(*args)


class AttackReceiver(ABC):
    def do(self, component_1, component_2):
        loss = component_1.attack()
        component_2.damage(loss)
        loss = component_2.attack()
        component_1.damage(loss)
        return [component_1, component_2]


class TreatReceiver(ABC):
    def do(self, component_1, component_2):
        component_1.treat()
        component_2.treat()
        return [component_1, component_2]


class HealthReceiver(ABC):
    def do(self, component_1, component_2):
        component_1.info_health()
        component_1.die()
        component_2.info_health()
        component_2.die()
        return [component_1, component_2]


class Invoker(ABC):
    command = {}

    def set_command(self, command, name):
        self.command[name] = command

    def do(self, name_of_command, *args):
        try:
            return self.command[name_of_command].execute(*args)
        except Exception:
            print('Please write a command correctly')
            return args
