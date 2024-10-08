from django.http import HttpResponse
from django.shortcuts import render
import requests

from .models import Champion

def get_game_version():
    url = "https://ddragon.leagueoflegends.com/api/versions.json"
    res = requests.get(url)
    return res.json()[0]

def categorize_champion_tier(champions):
    categorized_champions = {
        "s" : [],
        "a" : [],
        "b" : [],
        "c" : [],
        "d" : []
    }

    for champion in champions:
        if champion.winrate < 46:
            categorized_champions["d"].append(champion)
        elif champion.winrate < 50:
            categorized_champions["c"].append(champion)
        elif champion.winrate < 51:
            categorized_champions["b"].append(champion)
        elif champion.winrate < 53:
            categorized_champions["a"].append(champion)
        else:
            categorized_champions["s"].append(champion)

    return categorized_champions

def get_champion_tier(champion):
    if champion.winrate < 46: return "d"
    if champion.winrate < 50: return "c"
    if champion.winrate < 51: return "b"
    if champion.winrate < 53: return "a"
    return "s"

def index(request):
    champions = Champion.objects.order_by("name")

    champions_list = list(champions.values("name"))

    context = {"champions" : champions_list}
    return render(request, "web/index.html", context)

def ranking(request):
    champions = Champion.objects.order_by("-winrate")
    champions_list = list(champions.values("name"))
    
    categorized_champions = categorize_champion_tier(champions)

    context = {
        "champions" : champions_list,
        "champions_tier" : categorized_champions
        }
    return render(request, "web/ranking.html", context)

def champion(request, champion_name):
    champions = Champion.objects.order_by("name")
    champions_list = list(champions.values('name'))


    champion = Champion.objects.get(name = champion_name)
    tier = get_champion_tier(champion)
    items_sets = champion.items_set.all().order_by("-winrate")[:4]
    prismatics = champion.prismatic_item_set.all().order_by("-winrate")
    initial_items = champion.initial_item_set.all().order_by("-winrate")
    boots = champion.boot_item_set.all().order_by("-winrate")

    augments = {
        "prismatics" : champion.prismatic_augment_set.all().order_by("-winrate"),
        "gold" : champion.gold_augment_set.all().order_by("-winrate"),
        "silver" : champion.silver_augment_set.all().order_by("-winrate"),
    }

    context = {
        "game_version" : get_game_version(),
        "champions" : champions_list,
        "champion" : champion,
        "tier" : tier,
        "items_sets" : items_sets,
        "prismatics" : prismatics,
        "initial_items" : initial_items,
        "boots" : boots,
        "augments" :augments
        }
    return render(request, "web/champion.html", context)