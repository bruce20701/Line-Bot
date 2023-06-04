import requests
from datetime import datetime

#輸入城市以獲取天氣狀況
def weatherQurey(locationName):

    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001"

    parameters = {
    'Authorization':"CWB-111EAC52-3B14-46FE-A793-4081D3E0576D",
    'locationName':locationName
    }

    response = requests.get(url, params=parameters)

    if response.status_code == 200:
        data = response.json()

        #獲取當前時間
        searchTime = int(datetime.now().strftime("%H%M%S"))

        #取得特定城市的天氣(搜尋單一城市，所以只list內只有第0項)
        location = data['records']['location'][0]

        i=0
        weatherInit = []

        #利用weatherElement中的第0項Wx中的time取得Time
        for time in location['weatherElement'][0]['time']:

            #切出H:M:S
            selectedTime = int(time['endTime'][-8:].replace(":",""))

            #判斷時間區段
            if(selectedTime > searchTime):
                for j in range(5):
                    weatherInit.append(location['weatherElement'][j]['time'][i]['parameter']['parameterName'])
                return weatherInit
            else:
                i+=1
    else:
        print("error!")