from Riot_api import *
from DB import DB
from Game_version import Game_version
from Augments_controller import Augments_controller
from dotenv import load_dotenv
from Logger import Logger
import os

def main():
    load_dotenv()
    riot_api = Riot_api("europe","euw1",os.getenv('API_KEY'))
    
    Logger.write("CHALLENGER League ------->")
    summoner_ids = riot_api.get_summoner_ids_in_league("CHALLENGER", Tier.ONE.value, 1)
    insert_summoners_stats(summoner_ids, riot_api)

    Logger.write("GRANDMASTER League ------->")
    summoner_ids = riot_api.get_summoner_ids_in_league("GRANDMASTER", Tier.ONE.value, 1)
    insert_summoners_stats(summoner_ids, riot_api)

    Logger.write("MASTER League ------->")
    summoner_ids = riot_api.get_summoner_ids_in_league("MASTER", Tier.ONE.value, 1)
    insert_summoners_stats(summoner_ids, riot_api)

    Logger.write("DIAMOND I League ------->")
    summoner_ids = riot_api.get_summoner_ids_in_league("DIAMOND", Tier.ONE.value, 1)
    insert_summoners_stats(summoner_ids, riot_api)

    Logger.write("DIAMOND II League ------->")
    summoner_ids = riot_api.get_summoner_ids_in_league("DIAMOND", Tier.TWO.value, 1)
    insert_summoners_stats(summoner_ids, riot_api)

    Logger.write("DIAMOND III League ------->")
    summoner_ids = riot_api.get_summoner_ids_in_league("DIAMOND", Tier.THREE.value, 1)
    insert_summoners_stats(summoner_ids, riot_api)

    Logger.write("DIAMOND IV League ------->")
    summoner_ids = riot_api.get_summoner_ids_in_league("DIAMOND", Tier.FOUR.value, 1)
    insert_summoners_stats(summoner_ids, riot_api)

    Logger.write("EMERALD I League ------->")
    summoner_ids = riot_api.get_summoner_ids_in_league("EMERALD", Tier.ONE.value, 1)
    insert_summoners_stats(summoner_ids, riot_api)

    Logger.write("EMERALD II League ------->")
    summoner_ids = riot_api.get_summoner_ids_in_league("EMERALD", Tier.TWO.value, 1)
    insert_summoners_stats(summoner_ids, riot_api)

    Logger.write("EMERALD III League ------->")
    summoner_ids = riot_api.get_summoner_ids_in_league("EMERALD", Tier.THREE.value, 1)
    insert_summoners_stats(summoner_ids, riot_api)

    Logger.write("EMERALD IV League ------->")
    summoner_ids = riot_api.get_summoner_ids_in_league("EMERALD", Tier.FOUR.value, 1)
    insert_summoners_stats(summoner_ids, riot_api)

def insert_summoners_stats(summoner_ids, riot_api):
    for summoner_id in summoner_ids:
        account = riot_api.get_account_by_summoner_id(summoner_id)

        puuid = account.puuid
        if not puuid: continue

        match_ids = riot_api.get_match_ids(puuid, Queue.ARENA.value)
        insert_matches_stats(match_ids, riot_api)

def insert_matches_stats(match_ids, riot_api):
    for match_id in match_ids:
        match = riot_api.get_match(match_id)

        if not match.game_version: continue

        if match.game_version == Game_version.get_version():
            DB.insert_match_stats(match)

if __name__ == '__main__':
    while True:
        actual_version = Game_version.get_version()
        Augments_controller.set_augments_list(actual_version)
        DB.reset_db()
        Logger.clear()
        while Game_version.get_version() == actual_version:
            main()