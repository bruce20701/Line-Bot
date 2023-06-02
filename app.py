from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage
from model import Course
import threading
import time
import datetime
import pytz
import csv

app = Flask(__name__)

#儲存course的陣列
courseList = []

#line_bot的Token
line_bot_api = LineBotApi('c/2axBtAYZQkLSDHOVVnBLXdJLs0RabigC1tvKtEbNb8/8P6f14yLRrfAQKKiUH6KgcdQp+bDHEyI7qP0/zHpvJflIKqIFRl/l2fbVvQS3txUy1LcNpHR/iCIjjmshTzt5zQQrjEGbsLx2MorQ6CcAdB04t89/1O/w1cDnyilFU=')

#讀取課程資訊
with open('courseInfo.csv', mode='r') as file:
   reader = csv.DictReader(file)
   for row in reader:
      courseList.append(Course(row['name'], row['day'], row['startTime'], row['endTime'], row['location']))

def checkTime():
   global courseList, line_bot_api
   while True:
      # 取得當前的系統時間
      curTime = datetime.datetime.now()
      # 設定 GMT+8 的時區
      timezone = pytz.timezone("Asia/Taipei")
      # 將系統時間轉換為 GMT+8 時區的時間
      curTime = curTime.astimezone(timezone)
      curWeekday = curTime.strftime("%w")
      curHour = curTime.hour
      curMinute = curTime.minute
      print(f"系統時間： Hour:{curHour} Minute:{curMinute}")
      #走訪陣列資料
      for course in courseList:
         courseTime = datetime.datetime.strptime(course.startTime, "%H:%M")
         courseHour = courseTime.hour
         courseMinute = courseTime.minute
         print()
         if curWeekday == course.day and (curHour * 60 + curMinute) - (courseHour * 60 + courseMinute) == 30:
            messageStr = f"課程通知\n課程名稱：{course.name}\n教室：{course.location}\n上課時間：{course.startTime}\n下課時間：{course.endTime}\n祝您上課愉快！"
            line_bot_api.push_message('U3b706ee724da7f1ccaf51c2fb357d507', TextSendMessage(text=messageStr))
            break
      #系統休息10秒
      time.sleep(10)

#接受使用者訊息(還沒動工)
@app.route("/")
def home():
   global line_bot_api
   try:
      # 網址被執行時，等同使用 GET 方法發送 request，觸發 LINE Message API 的 push_message 方法
      line_bot_api.push_message('U3b706ee724da7f1ccaf51c2fb357d507', TextSendMessage(text='你好!'))
      return 'OK'
   except:
      print('error')

if __name__ == "__main__":
   # 定期偵測時間，每秒檢查一次
   check_thread = threading.Thread(target=checkTime)
   check_thread.start()

   # 啟動應用程式
   app_thread = threading.Thread(target=app.run)
   app_thread.start()