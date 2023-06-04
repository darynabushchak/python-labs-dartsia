from exceptions import RedundantHeightException
from models.decorators import logged


class ChairManager:
    """
    A class representing a chair manager.

    Attributes:
        chairs (list): A list of chairs managed by the chair manager.

    Methods:
        add_chair(chair): Adds a chair to the list of managed chairs.
        __len__(): Returns the number of chairs in the manager.
        __getitem__(index): Returns the chair at the specified index.
        __iter__(): Returns an iterator over the chairs.
        find_all_by_material(material): Finds all chairs with the specified material.
        find_all_with_max_weight_heavier_than(max_weight): Finds all chairs with a maximum weight heavier than the specified value.
        get_adjustment_results(value): Gets the adjustment results for all chairs using the specified value.
        get_attributes_by_type(data_type): Gets a dictionary of attributes with values of the specified data type.
        enumerate_chairs(): Enumerates the chairs, providing an index along with each chair.
        get_chairs_adjusted_height(): Gets a list of tuples containing each chair and its adjusted height.
        check_condition(condition): Checks whether the specified condition is satisfied for all chairs or any chair.
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
        return {
            key: value
            for key, value in self.__dict__.items()
            if isinstance(value, data_type)
        }

    def enumerate_chairs(self):
        return enumerate(self.chairs, start=1)

    def get_chairs_adjusted_height(self):
        chairs_adjusted_height = self.get_adjustment_results(value=10)
        return zip(self.chairs, chairs_adjusted_height)

    def check_condition(self, condition):
        all_condition = all(condition(chair) for chair in self.chairs)
        any_condition = any(condition(chair) for chair in self.chairs)
        return {"all": all_condition, "any": any_condition}

    @logged(RedundantHeightException, mode="console")
    def adjust_heights(self, value):
        for chair in self.chairs:
            chair.adjust_height(value)
