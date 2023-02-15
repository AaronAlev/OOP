"""Car operations."""
import time
current_year = int(time.strftime("%Y"))


class Car:
    """Car object."""

    def __init__(self, model, year, price):
        """Car constructor."""
        self.year = year
        self.model = model
        self.price = price

    def __repr__(self):
        """Represent self."""
        return f"'{self.model}, {self.year}, {self.price}'"


def create_car(model: str, price: int) -> 'Car':
    """Create a new car object with the current year if price is above 0."""
    if price <= 0:
        return None
    else:
        new_car = Car(model, current_year, price)
        return new_car


def get_most_expensive_car_below_price(cars: list, max_price: int) -> 'Car':
    """
    Return the most expensive car with the price lower than max_price.

    If several cars have the same price, return the first.
    If there are no cars with which have the price lower than max_price, return None.
    """
    if len(cars) > 0:
        car_dict = {}
        for car in cars:
            if car.price < max_price:
                car_dict[car] = car.price
        if len(car_dict) > 0:
            sorted_list = sorted(car_dict.items(), key=lambda x: x[1], reverse=True)
            return sorted_list[0][0]


def update_prices(cars: list, discount_per_year: int) -> None:
    """
    Update each car price so that for every year of their age they get discount_per_year lower price.

    If the car year is 2018 and currently it's 2020, then the discount is applied twice.
    The car price can never go below 0.

    Example:
        Currently it's 2020

        Car year is 2015
        Car price is 100
        discount_per_year = 5
        The new price for the car is 75

        Car year is 2000, price is 100, discount_per_year = 7
        The new price for the car is 0.
    """
    for car in cars:
        car_age = current_year - car.year
        discount_total = discount_per_year * car_age
        car.price -= discount_total
        if car.price < 0:
            car.price = 0


def get_cars_with_model(cars: list, model: str) -> list:
    """Return list of cars with the given model."""
    cars_with_model = []
    for car in cars:
        if car.model == model:
            cars_with_model.append(car)
    return cars_with_model


def get_ordered_cars(cars: list) -> list:
    """Return a new sorted list of cars by: year (newer first), price (cheaper first), model (from a to z)."""
    car_list = []
    for car in cars:
        car_list.append(car)
    sorted_dict = sorted(car_list, key=lambda x: (-x.year, x.price, x.model))
    return sorted_dict


car1 = Car("model", 2023, 500)
car2 = Car("model2", 2022, 500)
car3 = Car("ieakw", 2000, 109)
car4 = Car("fkek", 2023, 108)
car_list = [car1, car2, car3, car4]
print(get_ordered_cars(car_list))
print(get_most_expensive_car_below_price(car_list, 109))