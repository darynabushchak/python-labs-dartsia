class ChairManager:
    """
       A class that manages a collection of chairs.

       Attributes:
           chairs (list): A list of chairs managed by the ChairManager.

       Methods:
           add_chair(chairs_to_add):
               Adds a chair or a list of chairs to the collection.

           find_all_by_material(material):
               Finds all chairs in the collection with the specified material.

           find_all_with_max_weight_heavier_than(max_weight):
               Finds all chairs in the collection with a maximum weight heavier than the specified value.
       """
    def __init__(self):
        self.chairs = []

    def add_chair(self, chairs_to_add):
        self.chairs.append(chairs_to_add)

    def find_all_by_material(self, material):
        return list(filter(lambda chair: chair.material == material, self.chairs))

    def find_all_with_max_weight_heavier_than(self, max_weight):
        return list(filter(lambda chair: chair.max_weight > max_weight, self.chairs))
