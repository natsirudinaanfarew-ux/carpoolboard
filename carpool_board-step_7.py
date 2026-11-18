# === Stage 7: Фильтрация записей ===
# Project: CarpoolBoard
import datetime


def parse_date(value):
    """Преобразует строку формата 'YYYY-MM-DD' в объект datetime.date."""
    return datetime.datetime.strptime(value, "%Y-%m-%d").date()


def filter_trips_by_date(trips, date):
    """Возвращает поездки, дата которых совпадает с указанным значением."""
    result = []
    for trip in trips:
        if trip["date"] == date:
            result.append(trip)
    return result


def filter_trips_by_date_range(trips, start_date, end_date):
    """Возвращает поездки, даты которых попадают в заданный диапазон [start, end]."""
    result = []
    for trip in trips:
        if start_date <= trip["date"] <= end_date:
            result.append(trip)
    return result


def get_date_range(trips, start_date, end_date):
    """Помогает уточнить диапазон, подсказывая ближайшие доступные даты."""
    available_dates = sorted({trip["date"] for trip in trips})
    start = start_date
    end = end_date
    while start not in available_dates and available_dates:
        start = start + datetime.timedelta(days=1)
        if start > end:
            break
    while end not in available_dates and available_dates:
        end = end - datetime.timedelta(days=1)
        if end < start:
            break
    return start, end
