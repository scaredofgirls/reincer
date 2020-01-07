class Player():
    def __init__(self):
        self.race = "Unselected"
        self.name = "Unnamed"
        self.guilds = []
        self.skills = {}
        self.spells = {}
        self.wishes = {
            "major": [],
            "minor": []
        }
        self.tps_spent = 0

    def add_wish(self, wish_type, wish):
        pass

    def remove_wish(self, wish_type, wish):
        pass

    def add_guild(self, guild):
        pass
