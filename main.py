from manager.chair_manager import ChairManager
from model.dental_chair import DentalChair
from model.feeding_table import FeedingTable
from model.office_chair import OfficeChair
from model.rocking_chair import RockingChair

chair_list = ChairManager()
chair_list.add_chair(OfficeChair("vata", 45, 2, "wood", 140, "bilka 1"))
chair_list.add_chair(OfficeChair("pinoplast", 50, 3, "plastic", 150, "bilka 2"))
chair_list.add_chair(FeedingTable(100, 145, 120, 2, 4, "wood", 50, "bilka 3"))
chair_list.add_chair(FeedingTable(90, 150, 110, 1, 5, "plastic", 40, "bilka 4"))
chair_list.add_chair(RockingChair(50, 6, "wood", 150, "bilka 5"))
chair_list.add_chair(RockingChair(52, 7, "plastic", 200, "bilka 6"))
chair_list.add_chair(DentalChair(140, 90, 115, 8, "wood", 200, "bilka 7"))
chair_list.add_chair(DentalChair(130, 95, 110, 9, "plastic", 150, "bilka 8"))

for chair in chair_list.chairs:
    print(chair)

wood_chairs = chair_list.find_all_by_material("wood")
for wood_chair in wood_chairs:
    print(wood_chair)

weight_chairs = chair_list.find_all_with_max_weight_heavier_than(100)
for heavier_weight_chair in weight_chairs:
    print(heavier_weight_chair)
