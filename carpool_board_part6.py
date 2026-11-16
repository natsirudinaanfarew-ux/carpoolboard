# === Stage 6: Связи между сущностями ===
# Project: CarpoolBoard
from dataclasses import dataclass
from typing import List, Optional, Iterable, Iterator


@dataclass(frozen=True)
class Route:
    origin: str
    destination: str

    def __str__(self) -> str:
        return f"{self.origin} -> {self.destination}"


@dataclass
class Trip:
    route: Route
    date: str
    seats: int
    price: float

    @property
    def key(self) -> str:
        return f"{self.route.origin}|{self.route.destination}|{self.date}"


@dataclass
class Passenger:
    name: str
    id: Optional[str] = None


class TripDatabase:
    def __init__(self, trips: Iterable[Trip] = ()):
        self._trips: dict[str, Trip] = {trip.key: trip for trip in trips}

    def get_trip(self, key: str) -> Optional[Trip]:
        return self._trips.get(key)

    def all_trips(self) -> List[Trip]:
        return list(self._trips.values())


class PassengerBoard:
    def __init__(self, passengers: Iterable[Passenger] = ()):
        self._passengers: dict[str, Passenger] = {}
        for passenger in passengers:
            self.register(passenger)

    def register(self, passenger: Passenger) -> None:
        key = passenger.id or passenger.name
        self._passengers[key] = passenger

    def get(self, key: str) -> Optional[Passenger]:
        return self._passengers.get(key)

    def all(self) -> List[Passenger]:
        return list(self._passengers.values())

    def for_trip(self, trip: Trip) -> List[Passenger]:
        return [
            passenger
            for passenger in self._passengers.values()
            if passenger.id in (trip.route.origin, trip.route.destination)
        ]

    def validate(self, trip: Trip) -> bool:
        origin = self.get(trip.route.origin)
        destination = self.get(trip.route.destination)
        return origin is not None and destination is not None


def calculate_earnings(
    trip: Trip,
    passengers: Iterable[Passenger],
) -> float:
    return len(list(passengers)) * trip.price


def check_trip_integrity(trip: Trip) -> bool:
    return (
        isinstance(trip.route, Route)
        and trip.route.origin
        and trip.route.destination
        and trip.date
        and trip.seats > 0
        and trip.price >= 0
    )
