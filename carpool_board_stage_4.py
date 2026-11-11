# === Stage 4: Удаление и восстановление ===
# Project: CarpoolBoard
import datetime


class CarpoolBoardError(Exception):
    pass


class SoftDeleteMixin:
    deleted_at = None

    def mark_deleted(self):
        self.deleted_at = datetime.datetime.now(datetime.timezone.utc)

    def restore(self):
        self.deleted_at = None

    @property
    def is_deleted(self):
        return self.deleted_at is not None

    def delete(self):
        self.mark_deleted()
        return self

    def hard_delete(self):
        self.deleted_at = None
        self.id = None
        return True


class Trip(SoftDeleteMixin):
    def __init__(self, route, date, seats, price):
        self.route = route
        self.date = date
        self.seats = seats
        self.price = price
        self.deleted_at = None

    def mark_deleted(self):
        self.deleted_at = datetime.datetime.now(datetime.timezone.utc)

    def restore(self):
        self.deleted_at = None

    @property
    def is_deleted(self):
        return self.deleted_at is not None

    def delete(self):
        self.mark_deleted()
        return self

    def hard_delete(self):
        self.deleted_at = None
        self.id = None
        return True

    def available_seats(self, passengers):
        occupied = 0
        for p in passengers:
            if p.trip_id == self.id:
                occupied += 1
        return max(0, self.seats - occupied)

    def add_passenger(self, passenger):
        if self.is_deleted:
            raise CarpoolBoardError("Поездка удалена")
        if self.available_seats([passenger]) <= 0:
            raise CarpoolBoardError("Нет свободных мест")
        passenger.trip_id = self.id
        return passenger

    def total_revenue(self):
        if self.is_deleted:
            return 0
        return self.price * self.seats
