import requests
from time import sleep
from enum import Enum
from Match import Match
from Account import Account
from Logger import Logger

class Riot_api: 
    def __init__(self,region,server,key):
        self.region = region
        self.server = server
        self.key = key

    def set_key(self,key):
        self.key = key

    @staticmethod
    def send_request(url):
        status_code = 429

        while status_code == 429:
            res = requests.get(url)
            status_code = res.status_code

            if status_code == 429:
                Logger.write("Sleeping 10 segs ...")
                sleep(10)
            elif status_code != 200:
                res.raise_for_status()


        return res

    def buid_server_url(self, endpoint):
        url = f"https://{self.server}.api.riotgames.com{endpoint}"
        url += self.append_api_key(endpoint)

        return url
    
    def buid_region_url(self, endpoint):
        url = f"https://{self.region}.api.riotgames.com{endpoint}"
        url += self.append_api_key(endpoint)

        return url
    
    def append_api_key(self, endpoint):
        if "?" in endpoint: api_key_param = f"&api_key={self.key}"
        else : api_key_param = f"?api_key={self.key}"

        return api_key_param

    def get_summoner_ids_in_league(self, league, tier, page):
        endpoint = f"/lol/league-exp/v4/entries/RANKED_SOLO_5x5/{league}/{tier}"
        url = self.buid_server_url(endpoint)

        res = Riot_api.send_request(url)
        summoners = res.json()

        return [summoner["summonerId"] for summoner in summoners if not summoner["inactive"]]

    def get_account_by_summoner_id(self, summoner_id) -> Account:
        url = f"https://{self.server}.api.riotgames.com/lol/summoner/v4/summoners/{summoner_id}?api_key={self.key}"
        res = Riot_api.send_request(url)
        return Account(res.json())

    def get_match_ids(self, puuid, queue, start = 0, count = 20):
        url = f"https://{self.region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?queue={queue}&start={start}&count={count}&api_key={self.key}"
        res = Riot_api.send_request(url)
        return res.json()

    def get_match(self, match_id) -> Match:
        url = f"https://{self.region}.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={self.key}"
        res = Riot_api.send_request(url)
        return Match(res.json())

class Queue(Enum):
    ARENA = 1700

class Tier(Enum):
    ONE = "I"
    TWO = "II"
    THREE = "III"
    FOUR = "IV"