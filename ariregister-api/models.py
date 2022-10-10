class Company:
    def __init__(self, id, name, code, reg_dt):
        self.id = id
        self.name = name
        self.code = code
        self.reg_dt = reg_dt
        self.owners = []
    
    def add_owner(self, owner):
        self.owners.append(owner)

class Owner:
    def __init__(self, id, name, surname, type, code, role, amount):
        self.id = id
        self.name = name
        self.surname = surname
        self.type = type
        self.code = code
        self.role = role
        self.amount = amount