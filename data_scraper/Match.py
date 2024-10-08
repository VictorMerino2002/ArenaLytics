from Player import Player

class Match:
    def __init__(self, data):
        self.match_id = data.get("metadata", {}).get("matchId", None)
        self.participants_puuid = data.get("metadata", {}).get("participants", [])

        self.game_creation = data.get("info", {}).get("gameCreation", None)
        self.game_duration = data.get("info", {}).get("gameDuration", None)
        self.game_id = data.get("info", {}).get("gameId", None)
        self.game_mode = data.get("info", {}).get("gameMode", None)
        self.game_version = data.get("info", {}).get("gameVersion", "")[:5]
        
        if self.game_version.endswith("."):
            self.game_version = self.game_version[:-1]
        
        self.players = [Player(player) for player in data.get("info", {}).get("participants", [])]
