from .chair import Chair


class RockingChair(Chair):
    def __init__(
        self,
        color: set,
        id: int,
        material: str,
        max_weight: int,
        owner: str,
        current_slope_in_degrees: int,
        max_height,
        current_height,
    ):
        super().__init__(
            color, id, material, max_weight, owner, max_height, current_height
        )
        self.current_slope_in_degrees = current_slope_in_degrees
        self.max_height = max_height
        self.current_height = current_height

    def adjust_position(self, value):
        self.current_slope_in_degrees += value
        return self.current_slope_in_degrees

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
