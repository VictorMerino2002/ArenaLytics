class Account:
    def __init__(self,data):
        self.summoner_id = data.get("id", None)
        self.account_id = data.get("accountId", None)
        self.puuid = data.get("puuid", None)
        self.profile_icon_id = data.get("profileIconId", None)
        self.revision_date = data.get("revisionDate", None)
        self.summoner_level = data.get("summonerLevel", None)