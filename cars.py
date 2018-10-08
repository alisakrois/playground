import os
import csv


class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        __, file_extension = os.path.splitext(self.photo_file_name)
        return file_extension


class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_width, body_height, body_length):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.body_width = body_width
        self.body_height = body_height
        self.body_length = body_length

    def get_body_volume(self):
        volume = self.body_length * self.body_width * self.body_height
        return volume


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            if len(row) == 7:
                car_type = row[0]
                brand = row[1]
                passenger_seats_count = row[2]
                photo_file_name = row[3]
                body_whl = row[4].split('x') if row[4] else [0, 0, 0]
                carrying = row[5]
                extra = row[6]
                if car_type == 'car':
                    car_list.append(Car(car_type, brand, photo_file_name, carrying, passenger_seats_count))
                elif car_type == 'truck':
                    car_list.append(Truck(car_type, brand, photo_file_name,
                                          carrying, float(body_whl[0]), float(body_whl[1]), float(body_whl[2])))
                else:
                    car_list.append(SpecMachine(car_type,brand, photo_file_name, carrying, extra))
            else:
                continue

    return car_list

