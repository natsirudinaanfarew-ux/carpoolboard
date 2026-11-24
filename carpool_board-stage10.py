# === Stage 10: Поиск по нескольким словам ===
# Project: CarpoolBoard
import re


def parse_query(text):
    """Разбирает строку запроса на список слов с поддержкой исключений.

    Исключения задаются через префикс «-», например:
        «Москва-Санкт-Петербург-Катер»
    означает: Москва и Санкт-Петербург, но не Катер.
    """
    if not text:
        return []

    tokens = re.findall(r"-?\w+", text)
    includes = []
    excludes = []

    for token in tokens:
        if token.startswith("-"):
            excludes.append(token[1:])
        else:
            includes.append(token)

    return {"includes": includes, "excludes": excludes}


def matches(query, value):
    """Проверяет, соответствует ли значение запросу из parse_query."""
    parsed = parse_query(query)
    includes = parsed["includes"]
    excludes = parsed["excludes"]

    if not includes and not excludes:
        return True

    found = set()
    for word in includes:
        if word in value:
            found.add(word)

    for word in excludes:
        if word in value:
            return False

    return not includes or includes.issubset(found)


def search_trips(query, trips):
    """Ищет поездки по тексту запроса среди списка поездок.

    Поле «route» — это строка, содержащая маршрут (например:
    «Москва -> Санкт-Петербург»), поэтому совпадение ищётся по
    полному описанию маршрута.
    """
    results = []
    for trip in trips:
        route = trip.get("route", "")
        if matches(query, route):
            results.append(trip)
    return results
