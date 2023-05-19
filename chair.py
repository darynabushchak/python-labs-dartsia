class Chair:
    """
    The Chair class represents a chair object, which has attributes such as material, maximum weight capacity,
    owner, and an identifier.

    Attributes:
        material (str): The material of the chair.
        max_weight (float): The maximum weight capacity of the chair.
        owner (str, optional): The current owner of the chair (default is None).
        id (int): The identifier for the chair (default is 1).

    Methods:
        occupy(self, owner):
            Occupies the chair by assigning an owner.
            Args:
                owner (str): The name of the owner.

        release(self):
            Releases the chair by removing the current owner.

        is_occupied(self):
            Checks if the chair is currently occupied.
            Returns:
                bool: True if the chair is occupied, False otherwise.
    """

    __instance = None

    def __init__(self, __material=None, __max_weight=None, __owner=None, __id=1):
        """
        Initializes a new instance of the Chair class.

        Args:
            __material (str): The material of the chair.
            __max_weight (float): The maximum weight capacity of the chair.
            __owner (str, optional): The current owner of the chair (default is None).
            __id (int, optional): The identifier for the chair (default is 1).
        """
        self.material = __material
        self.max_weight = __max_weight
        self.owner = __owner
        self.id = __id

    def __str__(self):
        """
        Returns a string representation of the chair.

        Returns:
            str: A formatted string containing the chair's ID, material, maximum weight, and owner (if any).
        """
        return f"Chair ID: {self.id}, Material: {self.material}, Max weight: {self.max_weight}, Owner: {self.owner}"

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def occupy(self, owner):
        """
        Occupies the chair by assigning an owner.

        Args:
            owner (str): The name of the owner.
        """
        self.owner = owner

    def release(self):
        """
        Releases the chair by removing the current owner.
        """
        self.owner = None

    def is_occupied(self):
        """
        Checks if the chair is currently occupied.

        Returns:
            bool: True if the chair is occupied, False otherwise.
        """
        return self.owner is not None
