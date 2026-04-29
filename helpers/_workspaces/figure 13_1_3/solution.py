
class Item:
    def __init__(self):
        self.name = ""
        self.quantity = 0

    def set_name(self, nm):
        self.name = nm

    def set_quantity(self, qnty):
        self.quantity = qnty

    def display(self):
        print(self.name, self.quantity)

class Book(Item):
    def __init__(self):
        Item.__init__(self)
        self.title = ""

    def set_title(self, ttl):
        self.title = ttl

    def get_title(self):
        return self.title

class Textbook(Book):
    def __init__(self):
        Book.__init__(self)
        self.edition = ""

    def set_edition(self, edition):
        self.edition = edition

    def get_edition(self):
        return self.edition

class Audiobook(Book):
    def __init__(self):
        Book.__init__(self)
        self.reader = ""

    def set_reader(self, reader):
        self.reader = reader

    def get_reader(self):
        return self.reader

class Produce(Item):
    def __init__(self):
        Item.__init__(self)
        self.expiration = ""

    def set_expiration(self, expir):
        self.expiration = expir

    def get_expiration(self):
        return self.expiration



class Fruit(Produce):
    def __init__(self):
        Produce.__init__(self)
        self.has_seeds = True

    def set_has_seeds(self, sds):
        self.has_seeds = sds

    def get_has_seeds(self):
        return self.has_seeds


class Dairy(Produce):
    def __init__(self):
        Produce.__init__(self)
        self.percent_fat = 3

    def set_percent_fat(self, percent_fat):
        self.percent_fat = percent_fat

    def get_percent_fat(self):
        return self.percent_fat
    