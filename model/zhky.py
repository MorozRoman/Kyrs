class Zhky:
    def __init__(self, name):
        self.name = name
        # self.id = id

    def __repr__(self):
        return "%s:%s" %(self.name)

    # Логическое сравнение
    def __eq__(self, other):
        return self.name == other.name