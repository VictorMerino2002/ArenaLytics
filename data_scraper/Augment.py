class Augment:
    def __init__(self, data):
        self.data = data
        self.id = data["id"]
        self.name = data["name"]
        self.desc = data["desc"]
        self.set_tier()
        self.set_api_name()

    def set_tier(self):
        if self.data["rarity"] == 0:
            self.tier = "silver"
        elif self.data["rarity"] == 1:
            self.tier = "gold"
        elif self.data["rarity"] == 2:
            self.tier = "prismatic"

    def set_api_name(self):
        self.api_name = self.data["iconLarge"][32:]
