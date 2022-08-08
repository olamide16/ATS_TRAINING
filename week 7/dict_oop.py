class Country(object):
    data = {}

    def __init__(self, name, immigrants, population, disease_numbers):
        self.name = name
        self.immigrants = immigrants
        self.infected = population
        self.disease_numbers = disease_numbers

    @classmethod
    def add_data(cls, year, *args, **kwargs):
        obj = cls(*args, **kwargs)
        cls.data[obj.name, year] = obj

    # ...

Country.add_data("Venezuela", 1989, 100, 20, 50)
Country.add_data("Nigeria", 2022, 78956, 167045670, 12300)
