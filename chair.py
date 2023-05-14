class Chair:
    def __init__(self, material, max_weight, owner=None, id=1):
        self.material = material
        self.max_weight = max_weight
        self.owner = owner
        self.id = id

    def occupy(self, owner):
        self.owner = owner

    def release(self):
        self.owner = None

    def is_occupied(self):
        return self.owner is not None

    def __str__(self):
        return f"Chair ID: {self.id}\nMaterial: {self.material}\nMax weight: {self.max_weight}\nOwner: {self.owner}"
