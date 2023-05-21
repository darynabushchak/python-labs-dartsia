from .chair import Chair


class DentalChair(Chair):
    def __init__(
        self,
        max_height,
        min_height,
        current_height,
        id,
        material,
        max_weight,
        owner,
    ):
        super().__init__(id, material, max_weight, owner)
        self.max_height = max_height
        self.min_height = min_height
        self.current_height = current_height

    def adjust_position(self, value):
        if value <= self.max_height - self.current_height:
            self.current_height += value
        self.current_height = self.max_height

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(max_height={self.max_height}, min_height={self.min_height}, "
            f"current_height={self.current_height}, id={self.id}, material={self.material}, "
            f"max_weight={self.max_weight}, owner={self.owner})"
        )
