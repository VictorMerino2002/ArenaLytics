class Player:
    def __init__(self, data):
        self.puuid = data.get("puuid", None)
        self.champion_id = data.get("championId", None)
        self.champion_name = data.get("championName", None)

        self.items = [data.get(f"item{i}", None) for i in range(6)]
        self.augments = [data.get(f"playerAugment{i+1}", None) for i in range(4)]

        self.kills = data.get("kills", 0)
        self.assists = data.get("assists", 0)

        self.win = data.get("win", False)