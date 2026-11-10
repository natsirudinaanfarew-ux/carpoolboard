# === Stage 3: Хранилище в памяти ===
# Project: CarpoolBoard
import uuid


class RideNotFoundError(Exception):
    def __init__(self, ride_id):
        self.ride_id = ride_id
        super().__init__(f"Поездка с id {ride_id} не найдена")


class InMemoryRideStore:
    def __init__(self):
        self._rides = {}

    def add_ride(self, ride_id, route, date, seats, price):
        if ride_id in self._rides:
            raise ValueError(f"Поездка с id {ride_id} уже существует")
        ride = {
            "ride_id": ride_id,
            "route": route,
            "date": date,
            "seats": seats,
            "price": price,
        }
        self._rides[ride_id] = ride
        return ride

    def get_ride(self, ride_id):
        ride = self._rides.get(ride_id)
        if ride is None:
            raise RideNotFoundError(ride_id)
        return ride

    def list_rides(self):
        return list(self._rides.values())


def generate_ride_id():
    return str(uuid.uuid4())


if __name__ == "__main__":
    store = InMemoryRideStore()

    ride1 = store.add_ride(
        ride_id="ride-001",
        route="Москва -> Санкт-Петербург",
        date="2025-07-15",
        seats=4,
        price=1500,
    )
    print("Добавлена поездка:", ride1)

    found = store.get_ride("ride-001")
    print("Получена по id:", found)

    rides = store.list_rides()
    print(f"Всего поездок: {len(rides)}")

    try:
        store.get_ride("ride-999")
    except RideNotFoundError as exc:
        print("Не найдена:", exc)
