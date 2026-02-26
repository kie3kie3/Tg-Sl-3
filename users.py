import util
import telebot


class User:
    conditions = [
        'Имя',
        "Список ролей",
        "Штраф",
        "Месячный счетчик"
    ]


    def __init__(
            self, 
            name,
            id,
            roles = [],
            penalty = 0,
            monthCounter = 1,
            admin = False
    ):
        self.name = name
        self.id = str(id)
        self.roles = roles
        self.penalty = penalty
        self.monthCounter = monthCounter
        self.admin = admin


    def write(self):
        util.writeData(
            self,
            'users.json',
            self.id
        )


    @classmethod
    def read(cls, name):
        data = util.readData(
            'users.json',
            name
        )
        return cls(**data)
    

    def editShowAll():
        ...


    def edit(id, which):
        ...
