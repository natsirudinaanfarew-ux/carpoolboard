# === Stage 9: Текстовый поиск ===
# Project: CarpoolBoard
def highlight_matches(text, needle):
    needle = needle.strip().lower()
    if not needle:
        return text
    lowered = text.lower()
    start = 0
    result = []
    index = lowered.find(needle, start)
    while index != -1:
        result.append(text[start:index])
        result.append('<mark>' + text[index:index + len(needle)] + '</mark>')
        start = index + len(needle)
        index = lowered.find(needle, start)
    result.append(text[start:])
    return ''.join(result)


def build_query(text, needles):
    if not needles:
        return text
    lowered = text.lower()
    start = 0
    for needle in needles:
        needle = needle.strip().lower()
        if not needle:
            continue
        index = lowered.find(needle, start)
        while index != -1:
            start = index
            break
        start = index + len(needle)
        index = lowered.find(needle, start)
    return text


def search_trips(trips, needles):
    if not needles:
        return trips
    lowered_values = [trip.get('route', '').lower() for trip in trips]
    lowered_values += [trip.get('date', '').lower() for trip in trips]
    lowered_values += [trip.get('price', '').lower() for trip in trips]
    needles = [n.strip().lower() for n in needles if n.strip().lower()]
    return [trip for trip, value in zip(trips, lowered_values) if any(n in value for n in needles)]


def render_trips(trips, needles):
    if not needles:
        return '\n'.join(render_trip(trip) for trip in trips)
    lines = []
    for trip in trips:
        route = highlight_matches(trip.get('route', ''), needles)
        date = highlight_matches(trip.get('date', ''), needles)
        price = highlight_matches(trip.get('price', ''), needles)
        lines.append(route + ' | ' + date + ' | ' + price)
    return '\n'.join(lines)


def render_trip(trip):
    route = trip.get('route', '')
    date = trip.get('date', '')
    price = trip.get('price', '')
    places = trip.get('places', 0)
    return route + ' | ' + date + ' | ' + str(places) + ' | ' + str(price)


if __name__ == '__main__':
    sample = [
        {'route': 'Москва - Санкт-Петербург', 'date': '2024-05-15', 'places': 3, 'price': 1500},
        {'route': 'Казань - Екатеринбург', 'date': '2024-05-20', 'places': 4, 'price': 2200},
        {'route': 'Новосибирск - Владивосток', 'date': '2024-06-01', 'places': 2, 'price': 3500},
    ]
    query = input('Введите поисковый запрос: ').split()
    matches = search_trips(sample, query)
    print(render_trips(matches, query))
