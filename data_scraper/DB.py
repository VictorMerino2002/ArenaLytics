from Logger import Logger
from Items_controller import Items_controller
from Augments_controller import Augments_controller
import os
import sys
import django

# Agrega la ruta al directorio principal del proyecto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ArenaLytics.settings")
django.setup()

from web.models import *

class DB:

    @staticmethod
    def reset_db():
        Champion.objects.all().delete()
        Match.objects.all().delete() 

    @staticmethod
    def insert_match_stats(match):
        if not DB.is_match_already_inserted(match.match_id):
            Logger.write("inserting match : " + match.match_id)
            DB.insert_match_id(match.match_id)
            for player in match.players:
                DB.insert_player_stats(player)

    @staticmethod
    def is_match_already_inserted(match_id):
        return Match.objects.filter(code = match_id).exists()

    @staticmethod
    def insert_match_id(match_id):
        match = Match(code=match_id)
        match.save()

    @staticmethod
    def insert_player_stats(player):
        if not player.puuid: return
        
        champion = DB.insert_champion(player)
        DB.insert_items(player, champion)
        DB.insert_augments(player, champion)

    @staticmethod
    def insert_champion(player):
        champion_id = player.champion_id
        champion_name = player.champion_name

        win = 1 if player.win else 0

        if not Champion.objects.filter(code=champion_id).exists():
            champion = Champion(champion_id, champion_name.lower(), 0,0)
        else:
            champion = Champion.objects.get(code = champion_id)

        champion.games = champion.games + 1
        champion.wins = champion.wins + win
        champion.save()

        return champion
    
    @staticmethod
    def insert_items(player, champion):

        categorized_items = Items_controller.categorize_items(player.items)

        DB.insert_item_set(categorized_items["item_set"], player, champion)

        DB.insert_prismatic_items(categorized_items["prismatics"], player, champion)

        DB.insert_initial_item(categorized_items["initial"], player, champion)

        DB.insert_boot_item(categorized_items["boot"], player, champion)

    @staticmethod
    def insert_item_set(item_set, player, champion):
        champion_id = player.champion_id
        win = 1 if player.win else 0

        if not Items.objects.filter(item1 = item_set[0], item2 = item_set[1], item3 = item_set[2], item4 = item_set[3], champion = champion_id).exists():
            champion.items_set.create(item1 = item_set[0], item2 = item_set[1], item3 = item_set[2], item4 = item_set[3], games = 0, wins = 0)
        
        items = champion.items_set.get(item1 = item_set[0], item2 = item_set[1], item3 = item_set[2], item4 = item_set[3])
        
        items.games += 1
        items.wins += win

        items.save()

    @staticmethod
    def insert_prismatic_items(prismatics, player, champion):
        if not prismatics:
            return

        champion_id = player.champion_id
        win = 1 if player.win else 0

        for prismatic_code in prismatics:
            if not Prismatic_item.objects.filter(code=prismatic_code,champion=champion_id).exists():
                champion.prismatic_item_set.create(code=prismatic_code,games=0,wins=0)

            prismatic_item = champion.prismatic_item_set.get(code=prismatic_code)

            prismatic_item.games += 1
            prismatic_item.wins += win 

            prismatic_item.save()

    @staticmethod
    def insert_initial_item(initial_item, player, champion):
        if not initial_item:
            return

        champion_id = player.champion_id
        win = 1 if player.win else 0

        if not Initial_item.objects.filter(code=initial_item,champion=champion_id).exists():
            champion.initial_item_set.create(code=initial_item,games=0,wins=0)
        
        initial = champion.initial_item_set.get(code=initial_item)

        initial.games += 1
        initial.wins += win

        initial.save()

    @staticmethod
    def insert_boot_item(boot_code, player, champion):
        if not boot_code:
            return

        champion_id = player.champion_id
        win = 1 if player.win else 0

        if not Boot_item.objects.filter(code=boot_code,champion=champion_id).exists():
            champion.boot_item_set.create(code=boot_code,games=0,wins=0)
        
        boot = champion.boot_item_set.get(code=boot_code)

        boot.games += 1
        boot.wins += win

        boot.save()

    @staticmethod
    def insert_augments(player, champion):
        for augment_code in player.augments:
            augment = Augments_controller.get_augment(augment_code)
            
            if not augment: return

            if augment.tier == "prismatic": 
                DB.insert_prismatic_augment(augment, player, champion)
            elif augment.tier == "gold":
                DB.insert_gold_augment(augment, player, champion)
            elif augment.tier == "silver":
                DB.insert_silver_augment(augment, player, champion)

    @staticmethod
    def insert_prismatic_augment(augment, player, champion):
        win = 1 if player.win else 0

        if not champion.prismatic_augment_set.filter(code=augment.id).exists():
            champion.prismatic_augment_set.create(code=augment.id, name=augment.name, api_name=augment.api_name,games=0, wins=0)
        
        prismatic_augment = champion.prismatic_augment_set.get(code=augment.id)

        prismatic_augment.games +=1
        prismatic_augment.wins += win

        prismatic_augment.save()

    @staticmethod
    def insert_gold_augment(augment, player, champion):
        win = 1 if player.win else 0

        if not champion.gold_augment_set.filter(code=augment.id).exists():
            champion.gold_augment_set.create(code=augment.id, name=augment.name, api_name=augment.api_name, games=0, wins=0)
        
        gold_augment = champion.gold_augment_set.get(code=augment.id)

        gold_augment.games +=1
        gold_augment.wins += win

        gold_augment.save()
        
    @staticmethod
    def insert_silver_augment(augment, player, champion):
        win = 1 if player.win else 0

        if not champion.silver_augment_set.filter(code=augment.id).exists():
            champion.silver_augment_set.create(code=augment.id, name=augment.name, api_name=augment.api_name, games=0, wins=0)
        
        silver_augment = champion.silver_augment_set.get(code=augment.id)

        silver_augment.games +=1
        silver_augment.wins += win

        silver_augment.save()