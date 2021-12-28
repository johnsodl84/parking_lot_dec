import heapq
from collections import defaultdict, OrderedDict


class Car:
    def __init__(self, registration_number, color):
        self.registration_number = registration_number
        self.color = color

    def __str__(self):
        return "Car [registration_number=" + self.registration_number + " color =" + self.color + "]"


class ParkingLot:
    def __init__(self):
        self.registration_slot_mapping = dict()
        self.color_registration_mapping = defaultdict(list)
        self.slot_car_mapping = OrderedDict()
        self.available_parking_slots = []

    def create_parking_lot(self, total_slots):
        print("Created a parking lot with {} slots".format(total_slots))
        for i in range(1, total_slots + 1):
            heapq.heappush(self.available_parking_slots, i)
        return True

    def status(self):
        print("Slot No. Registration No. Color")
        for slot, car in self.slot_car_mapping.items():
            print("{}  {}   {}".format(slot, car.registration_number, car.color))
        return True

    def get_nearest_spot(self):
        return heapq.heappop(self.available_parking_slots) if self.available_parking_slots else None

    def leave(self, slot_to_be_open):
        found = None
        for registration_no, slot in self.registration_slot_mapping.items():
            if slot == slot_to_be_open:
                found = registration_no

        if found:
            heapq.heappush(self.available_parking_slots, slot_to_be_open)
            del self.color_registration_mapping[found]
            car_leaving = self.color_registration_mapping[slot_to_be_open]
            self.color_registration_mapping[car_leaving.color].remove(found)
            del self.slot_car_mapping[slot_to_be_open]
            print ("Slot No. {} is free".format(slot_to_be_open))
            return True

        else:
            print ("Slot is not in use")
            return False

    def park(self, car):
        slot_no = self.get_nearest_slot()
        if slot_no is None:
            print("Sorry, parking lot is full")
            return
        print("Allocated slot number: {}".format(slot_no))
        self.color_registration_mapping[slot_no] = car
        self.registration_slot_mapping[car.registration_number] = slot_no
        self.color_registration_mapping[car.color].append(car.registration_number)
        return slot_no

    def registration_numbers_cars_with_color(self, color):
        registration_numbers = self.color_registration_mapping[color]
        print (", ".join(registration_numbers))
        return self.color_registration_mapping[color]

    def slot_numbers_cars_with_color(self, color):
        registration_numbers = self.color_registration_mapping[color]
        slots = [self.registration_slot_mapping[reg_no] for reg_no in registration_numbers]
        print (", ".join(map(str, slots)))
        return slots

    def slot_number_for_registration_number(self, registration_number):
        slot_number = None
        if registration_number in self.registration_slot_mapping:
            slot_number = self.registration_slot_mapping[registration_number]
            print(slot_number)
            return slot_number
        else:
            print ("Not Found")
            return slot_number
