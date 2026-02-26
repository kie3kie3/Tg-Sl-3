import util
import telebot
import secret


class Case:
    bot = telebot.TeleBot(secret.token)

    editParse = 'a_ec'

    conditions = {
        'name': 'Имя',
        'roles': 'Роли, необходимые для этого кейса',
        'wants': 'Если нужно, чтобы этот кейс появлялся после предыдщего кейса, выбери пункт(как табачки или вент)',
        'tasks': 'Задания, которые нужно выполнить',
        'schedule': 'Расписание',
        'ping': 'Нужно ли уведомлять об опоздании',
        'pingDoer': "Нужно ли уведомлять ответственного",
        'days': 'Если необходимо работать только в определенные дни'
    }


    def __init__(
            self, 
            name,
            roles = [],
            wants = [],
            tasks = None,
            schedule = [0, 0],
            ping = True,
            pingDoer = False,
            days = []

    ):
        self.name = name
        self.roles = roles
        self.wants = wants
        self.tasks = tasks
        self.schedule = schedule
        self.ping = ping
        self.pingDoer = pingDoer
        self.days = days


    @classmethod
    def edit_condtion(cls, id, which):
        ...


    def write(self):
        util.writeData(
            obj=self,
            file_name='cases.json',
            name=self.name
        )

    
    @classmethod
    def read(cls, name):
        data = util.readData(
            'cases.json',
            name
        )
        return cls(**data)
    

    @classmethod
    def takeAll(cls):
        data = util.readData('cases.json')
        allC = []
        for value in data.values():
            allC.append(cls(**value))
        return allC
    

    @classmethod
    def show_edit(cls, id):
        markup = telebot.types.InlineKeyboardMarkup()
        for elem in cls.conditions.keys():
            button = telebot.types.InlineKeyboardButton(
                text=elem,
                callback_data=(cls.editParse + elem)
            )
            markup.add(button)
        button = telebot.types.InlineKeyboardButton(
            'Инфо о кнопках',
            callback_data=f'{cls.editParse}info'
        )
        markup.add(button)
        cls.bot.send_message(
            id,
            'Давай редактировать, если, что то непонятно, тыкни самую нижную кнопку', 
            reply_markup=markup
        )


    @classmethod
    def show_edit_info(cls, id):
        s = ''
        for key, value in cls.conditions.items():
            s += f'{key}: {value}, \n'
        cls.bot.send_message(
            id,
            s
        )
        cls.show_edit(id)


    @classmethod
    def edit(cls, id, which):
        if which == '':
            cls.show_edit(id)
        elif which == 'info':
            cls.show_edit_info(id)
        else:
            cls.edit_condition(id, which)

a = Case('a')
print(vars(a))
