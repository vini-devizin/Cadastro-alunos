class Student: # The class that will be used to register the students
    def __init__(self, name: str, notes: list[float], id: int):
        self.name: str = name
        self.notes: list[float] = notes
        self.id: int = id
        self.total: int = len(self.notes)
    def calcAverage(self) -> int:
        return sum(self.notes) / self.total