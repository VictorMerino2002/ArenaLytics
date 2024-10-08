class Items_controller:

    _initial = [222051, 223112, 223184, 223177, 223185, 2050, 2049]
    _boots = [223047, 223111, 223020, 223009, 223006, 223005, 223158]

    @staticmethod
    def is_prismatic(item_id):
        return item_id >= 443000
    
    @staticmethod
    def is_initial(item_id):
        return item_id in Items_controller._initial
    
    @staticmethod
    def is_boot(item_id):
        return item_id in Items_controller._boots
    
    @staticmethod
    def categorize_items(items):
        initial = None
        boot = None
        prismatics = []
        item_set = []

        for item in items:
            if Items_controller.is_boot(item):
                boot = item
            elif Items_controller.is_initial(item):
                initial = item
            elif Items_controller.is_prismatic(item):
                prismatics.append(item)
            else:
                item_set.append(item)

        while len(item_set) < 4:
            item_set.append(0)

        return {"initial":initial,"boot":boot,"prismatics":prismatics,"item_set":item_set}