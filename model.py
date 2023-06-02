class Course:
    def __init__(self, name, day, startTime, endTime, location) -> None:
        self.name = name
        self.day = day
        self.startTime = startTime
        self.endTime = endTime
        self.location = location

class LinkedList:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None