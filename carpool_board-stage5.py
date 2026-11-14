# === Stage 5: Связанная сущность ===
# Project: CarpoolBoard
import datetime

class Passenger:
    def __init__(self, name, phone):
        self.id = None
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"Passenger(id={self.id}, name={self.name!r}, phone={self.phone!r})"


class Trip:
    def __init__(self, route, date, seats, price):
        self.id = None
        self.route = route
        self.date = date
        self.seats = seats
        self.price = price
        self.passengers = []

    def __repr__(self):
        return f"Trip(id={self.id}, route={self.route!r}, date={self.date!r}, seats={self.seats}, price={self.price}, passengers={len(self.passengers)})"


class CarpoolBoard:
    def __init__(self):
        self._trips = {}
        self._passengers = {}

    def add_trip(self, route, date, seats, price):
        trip = Trip(route, date, seats, price)
        trip.id = len(self._trips) + 1
        self._trips[trip.id] = trip
        return trip

    def add_passenger(self, trip_id, name, phone):
        if trip_id not in self._trips:
            raise KeyError(f"Поездка с id={trip_id} не найдена")
        if self._trips[trip_id].seats <= len(self._trips[trip_id].passengers):
            raise ValueError("Места в поездке заняты")
        passenger = Passenger(name, phone)
        passenger.id = len(self._passengers) + 1
        self._passengers[passenger.id] = passenger
        self._trips[trip_id].passengers.append(passenger)
        return passenger

    def list_passengers(self, trip_id):
        return list(self._trips[trip_id].passengers)


if __name__ == "__main__":
    board = CarpoolBoard()
    trip = board.add_trip("Москва - Казань", "2025-03-15", 4, 1500)
    print(trip)
    p1 = board.add_passenger(trip.id, "Анна", "+79001112233")
    p2 = board.add_passenger(trip.id, "Борис", "+79004445566")
    print(p1, p2)
    print(board.list_passengers(trip.id))
    board.add_passenger(trip.id, "Виктор", "+79007778899")
    try:
        board.add_passenger(trip.id, "Гарри", "+79001234567")
    except ValueError as e:
        print("Ошибка:", e)
    print(board.list_passengers(trip.id))
