# pylint: disable=too-few-public-methods
"Singleton Concept Sample Code"
import copy

class Singleton:
    "The Singleton Class"
    value = []

    def __new__(cls):
        return cls
    
    # def __init__(self):
    #     print('in init')

    @staticmethod
    def static_method():
        "Use @staticmethod if no inner variables required"

    @classmethod
    def class_method(cls):
        "Use @classmethod to access class level variables"
        print(cls.value)

# The Client
# All uses of singleton point to the same memory address (id)
print(f'id(Singleton)\t= {id(Singleton)}')

object1 = Singleton()
print(f'id(object1)\t= {id(object1)}')

object2 = copy.deepcopy(object1)
print(f'id(object2)\t= {id(object2)}')

object3 = Singleton()
print(f'id(object3)\t= {id(object3)}')