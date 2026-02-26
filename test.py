import json

class Jopa:
    def __init__(self, name):
        self.asd = 123
        self.dsa = 321
        self.name = name

    

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.jopa = Jopa('123321')
    
    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)




a = Person('bujhm', 100, 'tashkent')
print(a.__dict__)

