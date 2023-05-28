class ChairManager:
    """
       """

    def __init__(self):
        self.chairs = []

    def add_chair(self, chair):
        self.chairs.append(chair)

    def __len__(self):
        return len(self.chairs)

    def __getitem__(self, index):
        return self.chairs[index]

    def __iter__(self):
        return iter(self.chairs)

    def find_all_by_material(self, material):
        return list(filter(lambda chair: chair.material == material, self.chairs))

    def find_all_with_max_weight_heavier_than(self, max_weight):
        return list(filter(lambda chair: chair.max_weight > max_weight, self.chairs))

    def get_adjustment_results(self, value):
        return [chair.adjust_height(value) for chair in self.chairs]

    def get_attributes_by_type(self, data_type):
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

    def enumerate_chairs(self):
        return list(enumerate(self.chairs, start=1))

    def get_chairs_adjusted_height(self):
        chairs_adjusted_height = self.get_adjustment_results(value=10)
        return list(zip(self.chairs, chairs_adjusted_height))

    def check_condition(self, condition):
        all_condition = all(condition(chair) for chair in self.chairs)
        any_condition = any(condition(chair) for chair in self.chairs)
        return {"all": all_condition, "any": any_condition}
