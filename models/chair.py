from abc import ABC, abstractmethod


class Chair(ABC):
    def __init__(
            self,
            color: set,
            id=1,
            material=None,
            max_weight=None,
            owner=None,
            max_height=None,
            current_height=None):
        """
        Initializes a new instance of the Chair class.

        Args:
            material (str): The material of the chair.
            max_weight (float): The maximum weight capacity of the chair.
            owner (str, optional): The current owner of the chair (default is None).
            id (int, optional): The identifier for the chair (default is 1).
        """
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
            self.current_height = self.max_height
        return self.current_height

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def __str__(self):
        return f"\n{self.__class__.__name__} (material - {self.material}, " \
               f"max weight that the chair can support - {self.max_weight})"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, material={self.material}, max_weight={self.max_weight},"
            f", owner={self.owner})"
        )
