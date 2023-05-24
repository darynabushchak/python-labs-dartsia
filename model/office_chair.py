from .chair import Chair


class OfficeChair(Chair):
    def __init__(
        self,
        chair_upholstery,
        current_slope_in_degrees,
        id,
        material,
        max_weight,
        owner,
    ):
        super().__init__(id, material, max_weight, owner)
        self.chair_upholstery = chair_upholstery
        self.current_slope_in_degrees = current_slope_in_degrees

    def adjust_position(self, value):
        self.current_slope_in_degrees += value

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(chair_upholstery={self.chair_upholstery}, "
            f"current_slope_in_degrees={self.current_slope_in_degrees}, id={self.id}, "
            f"material={self.material}, max_weight={self.max_weight}, owner={self.owner})"
        )
