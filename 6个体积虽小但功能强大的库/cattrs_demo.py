from dataclasses import dataclass
import cattrs

@dataclass
class User:
    name: str
    score: int

user = User('Jackzhang', 100)
converter = cattrs.Converter()

data = converter.unstructure(user)
print(data) # {'name': 'Jackzhang', 'score': 100}

obj = converter.structure(data, User)
print(obj)  # User(name='Jackzhang', score=100)