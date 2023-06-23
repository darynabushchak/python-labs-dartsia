from .chair import Chair


class DentalChair(Chair):
    def __init__(
            self,
            color: set,
            id,
            material,
            max_weight,
            owner,
            max_height,
            current_height,
            min_height,
    ):
        super().__init__(
            color, id, material, max_weight, owner, max_height, current_height
        )
        self.min_height = min_height

    def adjust_position(self, value):
        if value <= self.max_height - self.current_height:
            self.current_height += value
        self.current_height = self.max_height
        return self.current_height

    def get_set_items(self):
        set_items = set()
        set_items.add(self.id)
        return set_items

    def __repr__(self):
        return (
            f"({self.__class__.__name__}(owner={self.owner}"
            f", adjusted_height: {self.adjust_height(value=10)}"
            f", available chair colors: {self.color})\n"
        )
