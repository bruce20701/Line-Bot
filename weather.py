class Weather():
    def __init__(self,weatherData):
        self.wx = weatherData[0]
        self.pop = weatherData[1]
        self.minT = weatherData[2]
        self.ci = weatherData[3]
        self.maxT = weatherData[4]

    def printWeather(self):
        print(f'天氣現象:{self.wx}')
        print(f'降雨機率:{self.pop}%')
        print(f'最低溫度:{self.minT}°C')
        print(f'最高溫度:{self.maxT}°C')
        print(f'舒適度:{self.ci}')
        
        