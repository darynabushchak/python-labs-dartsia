from .chair import Chair


class FeedingTable(Chair):
    def __init__(
        self,
        min_height,
        max_height,
        current_height,
        child_age,
        id,
        material,
        max_weight,
        owner,
    ):
        super().__init__(id, material, max_weight, owner)
        self.min_height = min_height
        self.max_height = max_height
        self.current_height = current_height
        self.child_age = child_age

    def adjust_position(self, value):
        if value <= self.max_height - self.current_height:
            self.current_height += value
        self.current_height = self.max_height

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(min_height={self.min_height}, max_height={self.max_height}, "
            f"current_height={self.current_height}, id={self.id}, material={self.material}, "
            f"max_weight={self.max_weight}, owner={self.owner})"
        )
