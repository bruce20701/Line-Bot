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

class Weather:
    def __init__(self, wx, maxT, minT, ci, pop) -> None:
        # 天氣現象
        self.wx = wx
        # 最高溫
        self.maxT = maxT
        # 最低溫
        self.minT = minT
        # 舒適度
        self.ci = ci
        # 降雨機率
        self.pop = pop