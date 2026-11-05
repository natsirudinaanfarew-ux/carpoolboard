# === Stage 2: Проверка полей ===
# Project: CarpoolBoard
from datetime import datetime, date, timedelta

ROUTE_FIELDS = ("маршрут", "дата", "мест", "цена")

ROUTE = "Москва -> Санкт-Петербург"
DATE = "2025-08-15"
PLACES = 2
PRICE = 1500


def normalize_route(raw):
    route = raw.strip()
    if len(route) < 2:
        raise ValueError("Маршрут должен содержать как минимум два города")
    if "->" not in route:
        raise ValueError("Маршрут должен содержать разделитель направления (->)")
    parts = [part.strip() for part in route.split("->")]
    if len(parts) != 2 or not parts[0] or not parts[1]:
        raise ValueError("Маршрут должен быть в формате 'Город А -> Город Б'")
    return route


def normalize_date(raw):
    if not raw:
        raise ValueError("Дата обязательна")
    try:
        parsed = datetime.strptime(raw, "%Y-%m-%d").date()
    except ValueError:
        try:
            parsed = datetime.strptime(raw, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Дата должна быть в формате ГГГГ-ММ-ДД или ДД.ММ.ГГГГ")
    if parsed < date.today():
        raise ValueError("Дата поездки не может быть в прошлом")
    return parsed.isoformat()


def normalize_places(raw):
    try:
        places = int(raw)
    except (TypeError, ValueError):
        raise ValueError("Количество мест должно быть целым числом")
    if places <= 0:
        raise ValueError("Количество мест должно быть больше нуля")
    if places > 10:
        raise ValueError("Максимальное количество мест за раз — 10")
    return places


def normalize_price(raw):
    try:
        price = float(raw)
    except (TypeError, ValueError):
        raise ValueError("Цена должна быть числом")
    if price <= 0:
        raise ValueError("Цена должна быть положительной")
    return round(price, 2)


def validate_trip(route, date, places, price):
    errors = []
    for field, value in (
        ("маршрут", route),
        ("дата", date),
        ("мест", places),
        ("цена", price),
    ):
        try:
            normalized = NORMALIZE_FUNCS[field](value)
        except ValueError as exc:
            errors.append(f"Поле '{field}': {exc}")
    if errors:
        raise ValueError("\n".join(errors))
    return {
        "route": normalize_route(route),
        "date": normalize_date(date),
        "places": normalize_places(places),
        "price": normalize_price(price),
    }


NORMALIZE_FUNCS = {
    "маршрут": normalize_route,
    "дата": normalize_date,
    "мест": normalize_places,
    "цена": normalize_price,
}


if __name__ == "__main__":
    raw_route = "Москва -> Санкт-Петербург"
    raw_date = "15.08.2025"
    raw_places = "3"
    raw_price = "1500"

    normalized = validate_trip(raw_route, raw_date, raw_places, raw_price)

    print("Маршрут:", normalized["route"])
    print("Дата:", normalized["date"])
    print("Мест:", normalized["places"])
    print("Цена:", normalized["price"])

    for field in ROUTE_FIELDS:
        print(f"Нормализованное значение поля '{field}': {normalized[field]}")
