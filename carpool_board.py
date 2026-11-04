# === Stage 1: Каркас модуля ===
# Project: CarpoolBoard
from dataclasses import dataclass, field
from datetime import date
from typing import List


@dataclass
class Trip:
    route: str
    date: date
    seats: int
    price: float
    passengers: List = field(default_factory=list)


def create_demo_trips() -> List[Trip]:
    return [
        Trip(route="Москва -> Санкт-Петербург",
             date=date(2025, 1, 15),
             seats=4,
             price=2500.0),
        Trip(route="Санкт-Петербург -> Москва",
             date=date(2025, 1, 16),
             seats=3,
             price=2400.0),
        Trip(route="Казань -> Москва",
             date=date(2025, 1, 17),
             seats=5,
             price=1800.0),
    ]


def main() -> None:
    trips = create_demo_trips()
    print("=== CarpoolBoard: совместные поездки ===")
    print(f"Доступно поездок: {len(trips)}\n")
    for trip in trips:
        print(f"Маршрут: {trip.route}")
        print(f"Дата: {trip.date}")
        print(f"Мест: {trip.seats}")
        print(f"Цена: {trip.price} руб.")
        print("-" * 40)


if __name__ == "__main__":
    main()
