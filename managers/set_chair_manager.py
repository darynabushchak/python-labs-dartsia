from managers.chair_manager import ChairManager


class SetManager:
    def __init__(self, regular_manager: ChairManager):
        self.regular_manager = regular_manager

    def __iter__(self):
        for chair in self.regular_manager:
            yield from chair.available_chair_colors_set

    def __len__(self):
        return sum(len(chair.color) for chair in self.regular_manager)

    def __getitem__(self, index):
        for chair in self.regular_manager:
            if index < len(chair.color):
                return list(chair.color)[index]
            index -= len(chair.color)
        raise IndexError("index out of range")

    def __next__(self):
        for chair in self.regular_manager:
            for color in chair.color:
                yield color
