from abc import ABC, abstractmethod

from redundant_height_exception import RedundantHeightException


class Chair(ABC):
    """
    Abstract base class representing a chair.

    Attributes:
    id (int): The unique identifier of the chair.
    material (str): The material of the chair.
    max_weight (float): The maximum weight that the chair can support.
    owner (str): The owner of the chair.
    current_height (float): The current height of the chair.
    max_height (float): The maximum height of the chair.
    color (set): The set of colors of the chair.

    Methods:
    adjust_position(value): Abstract method to adjust the position of the chair.
    adjust_height(value): Adjusts the height of the chair.
    get_instance(): Returns a singleton instance of the chair.
    __str__(): Returns a string representation of the chair.
    __repr__(): Returns a string representation of the chair suitable for reproduction.

    """
    def __init__(
        self,
        color: set,
        id=1,
        material=None,
        max_weight=None,
        owner=None,
        max_height=None,
        current_height=None,
    ):

        self.id = id
        self.material = material
        self.max_weight = max_weight
        self.owner = owner
        self.current_height = current_height
        self.max_height = max_height
        self.color = color

    def __iter__(self):
        return iter(self.color)

    __instance = None

    @abstractmethod
    def adjust_position(self, value):
        pass

    def adjust_height(self, value):
        if value <= self.max_height - self.current_height:
            self.current_height += value
        else:
            raise RedundantHeightException("the height is not adjustable. redundant height!")

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def __str__(self):
        return (
            f"\n{self.__class__.__name__} (material - {self.material}, "
            f"max weight that the chair can support - {self.max_weight})"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, material={self.material}, max_weight={self.max_weight},"
            f", owner={self.owner})"
        )
