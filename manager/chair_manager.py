class ChairManager:
    def __init__(self):
        self.chairs = []

    def add_chair(self, chairs_to_add):
        self.chairs.append(chairs_to_add)

    def find_all_by_material(self, material):
        return list(filter(lambda chair: chair.material == material, self.chairs))

    def find_all_with_max_weight_heavier_than(self, max_weight):
        return list(filter(lambda chair: chair.max_weight > max_weight, self.chairs))
