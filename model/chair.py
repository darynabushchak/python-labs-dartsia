from abc import ABC, abstractmethod


class Chair(ABC):
    def __init__(self, id=1, material=None, max_weight=None, owner=None):
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

    __instance = None

    def __str__(self):
        return f"{self.__class__.__name__}:{self.material}, {self.max_weight}"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, material={self.material}, max_weight={self.max_weight},"
            f", owner={self.owner})"
        )

    @abstractmethod
    def adjust_position(self, value):
        pass

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance
