# === Stage 11: Теги ===
# Project: CarpoolBoard
class TripTag:
    def __init__(self, name):
        self.name = name.lower().strip()

    def __eq__(self, other):
        if isinstance(other, TripTag):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"TripTag({self.name!r})"


class TagRepository:
    def __init__(self):
        self._tags = {}

    def add(self, name):
        tag = TripTag(name)
        if tag.name in self._tags:
            return self._tags[tag.name]
        self._tags[tag.name] = tag
        return tag

    def remove(self, name):
        removed = self._tags.pop(name.lower().strip(), None)
        return removed is not None

    def get(self, name):
        return self._tags.get(name.lower().strip())

    def search(self, name):
        return self._tags.get(name.lower().strip())

    def all(self):
        return list(self._tags.values())
