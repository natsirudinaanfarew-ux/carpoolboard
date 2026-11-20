# === Stage 8: Сортировка записей ===
# Project: CarpoolBoard
def sort_trips(trips, by_route=False, by_created=False, order="asc"):
    """
    Сортирует список поездок по маршруту и дате создания.

    Параметры:
        trips   - список записей «поездка» (словари)
        by_route - сортировать по маршруту (bool)
        by_created - сортировать по дате создания (bool)
        order - "asc" (возрастание) или "desc" (убывание)

    Возвращает новый список, исходный не изменяет.
    """
    def route_key(trip):
        return trip.get("маршрут", "")

    def created_key(trip):
        return trip.get("дата", "")

    reverse = (order == "desc")

    if by_route and by_created:
        return sorted(
            trips,
            key=lambda t: (route_key(t), created_key(t)),
            reverse=reverse,
        )
    if by_route:
        return sorted(trips, key=route_key, reverse=reverse)
    if by_created:
        return sorted(trips, key=created_key, reverse=reverse)
    return list(trips)


if __name__ == "__main__":
    sample = [
        {"маршрут": "Москва -> Казань", "дата": "2024-06-10"},
        {"маршрут": "Москва -> Самара", "дата": "2024-06-01"},
        {"маршрут": "Москва -> Казань", "дата": "2024-06-05"},
    ]
    print(sort_trips(sample, by_route=True, by_created=True))
    print(sort_trips(sample, by_route=True, by_created=True, order="desc"))
