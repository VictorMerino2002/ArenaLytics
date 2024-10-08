import requests
from Augment import Augment

class Augments_controller:
    _augments_list = None

    @staticmethod
    def set_augments_list(game_version):
        url = f"https://raw.communitydragon.org/{game_version}/cdragon/arena/en_us.json"
        res = requests.get(url)
        Augments_controller._augments_list = res.json()["augments"]

    def get_augment(augment_id):
        for augment in Augments_controller._augments_list:
            if augment["id"] == augment_id:
                return Augment(augment)
            
        return None
    