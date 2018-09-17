class MarvelCharacter:
    """
    Creates a character from the Marvel universe
    """

    # class atribute
    location = "Earth"

    def __init__(self, name: str, birthyear: int, sex: str):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, birthyear: {self.birthyear})"

    def says(self, words):
        return f"{self._name} says {words}"

    @staticmethod
    def StanLee():
        return MarvelCharacter("Stan Lee", 1922, "Male")


class Hero(MarvelCharacter):
    """
    Create a Marvel hero
    """

    def __init__(self, name: str, birthyear: int, sex: str, species: str, alias: str, weapon: tuple = None):
        super().__init__(name, birthyear, sex)
        self.species = species
        self.alias = alias

        if weapon is not None:
            self.weapon_name, self.weapon_type = weapon

        self._current_affilitions = {
            "Asgardian Royal Family": True,
            "Avengers": True,
            "Revengers": False}

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, birthyear: {self.birthyear}, alias: {self.alias})"


    @staticmethod
    def fight_outcome(fight):
        """
        Determine if the Hero won fights as an Avengers
        """
        fights = {
            "Ebony Maw": True,
            "Cull Obsidian": True,
            "Ultron": True,
            "Proxima Midnight": True,
            "Thanos": False}
        return fights.get(fight, False)

    @classmethod
    def spider_man(cls):
        return cls("Peter Benjamin Parker", 2001, "Male", "Human", "Spider-Man", ("Web-Shooters", "Mechanical Device"))

    @classmethod
    def iron_man(cls):
        return cls("Anthony Edward Stark", 1970, "Male", "Human", "Iron-Man", ("Arc Reactor", "Power source"))

    @classmethod
    def hulk(cls):
        return cls("Robert Bruce Banner", 1969, "Male", "Human", "The Incredible Hulk", ("Stretchable Pants", "Clothing"))


class Villain(MarvelCharacter):
    """
    Creates a Marvel villain
    """

    def __init__(self, name: str, birthyear: int, sex: str, species: str, villain_to: str, affiliation: str = None):
        super().__init__(name, birthyear, sex)
        self.species = species
        self.villain_to = villain_to

        if affiliation is not None:
            self.affiliation = affiliation

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, birthyear: {self.birthyear}, villain to: {self.villain_to})"

    @classmethod
    def ultron(cls):
        return cls("Ultron", 2015, "Male", "Android", "Avengers", None)

    @classmethod
    def whiplash(cls):
        return cls("Ivan Antonovich Vanko", 1968, "Male", "Human", "Iron Man", "Hammer Industries")


class MinorCharacter(MarvelCharacter):
    """
    Creates a Marvel minor character
    """

    def __init__(self, name: str, birthyear: int, sex: str, species: str, related_to: str = None):
        super().__init__(name, birthyear, sex)
        self.species = species

        if related_to is not None:
            self.related_to = related_to

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, birthyear: {self.birthyear}, related to: {self.related_to})"

if __name__ is "__main__":
    iron_man = MarvelCharacter("Anthony Edward Stark", 1970, "Male")
    print("Iron man: ", iron_man)
    spider_man = Hero(name="Peter Benjamin Parker", birthyear=2001, sex="Male",
                      species="Human", alias="Spider-Man", weapon=("Web-Shooters", "Mechanical Device"))
    print("Spiderman: ", spider_man)
    stan_lee = spider_man.StanLee()
    print("Stan Lee: ", stan_lee)

    ultron = Villain.ultron()
    print("Ultron: ", ultron)
    whiplash = Villain.whiplash()
    print("Whiplash: ", whiplash)
    spider_man = Hero.spider_man()
    print("Spiderman: ", spider_man)
    iron_man = Hero.iron_man()
    print("Iron man: ", iron_man)
    hulk = Hero.hulk()
    print("Hulk: ", hulk)
