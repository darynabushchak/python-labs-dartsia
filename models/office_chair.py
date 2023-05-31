from .chair import Chair
from .decorators import validate_method_name


class OfficeChair(Chair):
    def __init__(
        self,
        color: set,
        id,
        material,
        max_weight,
        owner,
        chair_upholstery,
        current_slope_in_degrees,
        max_height,
        current_height,
    ):
        super().__init__(
            color, id, material, max_weight, owner, max_height, current_height
        )
        self.chair_upholstery = chair_upholstery
        self.current_slope_in_degrees = current_slope_in_degrees
        self.max_height = max_height
        self.current_height = current_height

    @validate_method_name
    def adjust_position(self, value):
        self.current_slope_in_degrees += value
        return self.current_slope_in_degrees

    def __repr__(self):
        return (
            f"({self.__class__.__name__}(owner={self.owner}"
            f", adjusted_height: {self.adjust_height(value=10)}"
            f", available chair colors: {self.color})\n"
        )
