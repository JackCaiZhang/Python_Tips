from collections import OrderedDict

class OrderedMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases):
        """Returns the namespace dict for class creation."""
        print(f'Preparing namespace for class {name}')
        return OrderedDict()    # Preserve order
    
    def __new__(metacls, name, bases, namespace):
        # namespace is the OrderedDict from __prepare__
        result = super().__new__(metacls, name, bases, namespace)
        result._field_order = list(namespace.keys())
        return result
    
class DatabaseModel(metaclass=OrderedMeta):
    """Column order matters for SQL generation."""
    id  = 'INT PRIMARY KEY'
    name = 'VARCHAR(100)'
    email = 'VARCHAR(100)'
    created_at = 'TIMESTAMP'

print(DatabaseModel._field_order)  
# ['__module__', '__qualname__', '__firstlineno__', '__doc__', 'id', 
# 'name', 'email', 'created_at', '__static_attributes__']