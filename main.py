from managers.chair_manager import ChairManager
from managers.set_chair_manager import SetManager
from models.dental_chair import DentalChair
from models.feeding_table import FeedingTable
from models.office_chair import OfficeChair
from models.rocking_chair import RockingChair

chair_list = ChairManager()
chair_list.add_chair(OfficeChair({"pink"}, 3, "wood", 140, "bilka 1", "vata", 35, 80, 50))
chair_list.add_chair(OfficeChair({"black"}, 4, "plastic", 150, "bilka 2", "pinoplast", 50, 100, 30))
chair_list.add_chair(FeedingTable({"pink"}, 5, "wood", 50, "bilka 3", 145, 100))
chair_list.add_chair(FeedingTable({"pink"}, 6, "plastic", 40, "bilka 4", 150, 90))
chair_list.add_chair(RockingChair({"pink"}, 7, "wood", 150, "bilka 5", 50, 150, 85))
chair_list.add_chair(RockingChair({"pink"}, 8, "plastic", 200, "bilka 6", 52, 120, 95))
chair_list.add_chair(DentalChair({"pink"}, 9, "wood", 200, "bilka 7", 140, 90, 115))
chair_list.add_chair(DentalChair({"pink"}, 10, "plastic", 150, "bilka 8", 130, 95, 110))

for result in chair_list.enumerate_chairs():
    print(result)

all_wood_chairs = chair_list.check_condition(lambda chair: chair.material == "wood")
print("\nall chairs are made of wood:\n", all_wood_chairs)

set_manager = SetManager(chair_list)
print("\ncolor chair at index 6: ", set_manager[5])
