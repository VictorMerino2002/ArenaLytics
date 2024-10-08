from Riot_api import Riot_api

class Game_version:
    _version = None

    @staticmethod
    def set_version():
        url = "https://ddragon.leagueoflegends.com/api/versions.json"
        res = Riot_api.send_request(url)
        version = res.json()[0][:5]
        Game_version._version = version

    @staticmethod
    def get_version():
        if Game_version._version == None:
            Game_version.set_version()

        return Game_version._version