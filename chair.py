class Chair:
    """
    The Chair class represents a chair object, which has attributes such as material, maximum weight capacity,
    owner, and an identifier.

    Attributes:
        __material (str): The material of the chair.
        __max_weight (float): The maximum weight capacity of the chair.
        __owner (str, optional): The current owner of the chair (default is None).
        __id (int): The identifier for the chair (default is 1).

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

    instance = None

    def __init__(self, __material=None, __max_weight=None, __owner=None, __id=1):
        """
        Initializes a new instance of the Chair class.

        Args:
            __material (str): The material of the chair.
            __max_weight (float): The maximum weight capacity of the chair.
            __owner (str, optional): The current owner of the chair (default is None).
            __id (int, optional): The identifier for the chair (default is 1).
        """
        self.__material = __material
        self.__max_weight = __max_weight
        self.__owner = __owner
        self.__id = __id

    def __str__(self):
        """
        Returns a string representation of the chair.

        Returns:
            str: A formatted string containing the chair's ID, material, maximum weight, and owner (if any).
        """
        return f"Chair ID: {self.__id}\nMaterial: {self.__material}\nMax weight: {self.__max_weight}\nOwner: {self.__owner}"

    @staticmethod
    def get_instance():
        if Chair.instance is None:
            Chair.instance = Chair()
        return Chair.instance

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, value):
        self.__material = value

    @property
    def max_weight(self):
        return self.__max_weight

    @max_weight.setter
    def max_weight(self, value):
        self.__max_weight = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__owner = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def occupy(self, owner):
        """
        Occupies the chair by assigning an owner.

        Args:
            owner (str): The name of the owner.
        """
        self.__owner = owner

    def release(self):
        """
        Releases the chair by removing the current owner.
        """
        self.__owner = None

    def is_occupied(self):
        """
        Checks if the chair is currently occupied.

        Returns:
            bool: True if the chair is occupied, False otherwise.
        """
        return self.__owner is not None
