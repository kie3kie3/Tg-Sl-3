import util


class Roles:
    conditions = [
        
    ]


    def __init__(
            self,
            name,
            roles = []
    ):
        self.name = name
        self.roles = roles
    

    def write(self):
        util.writeData(
            self,
            'roles.json',
            self.name
        )


    @classmethod
    def read(cls, name):
        data = util.writeData(
            'roles.json',
            name
        )
        return cls(**data)
    

    def write(self):
        util.writeData(
            obj=self,
            file_name='roles.json',
            name=self.name
        )

    
    def edit(id, which):
        ...