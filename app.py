from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage
from model import Course, LinkedList
import threading
import time
import datetime
import pytz
import csv

app = Flask(__name__)

# LinkedList基本配置
courseList = None
headNode = courseList
curNode = headNode

#line_bot的Token
line_bot_api = LineBotApi('c/2axBtAYZQkLSDHOVVnBLXdJLs0RabigC1tvKtEbNb8/8P6f14yLRrfAQKKiUH6KgcdQp+bDHEyI7qP0/zHpvJflIKqIFRl/l2fbVvQS3txUy1LcNpHR/iCIjjmshTzt5zQQrjEGbsLx2MorQ6CcAdB04t89/1O/w1cDnyilFU=')

#讀取課程資訊
with open('test.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if courseList == None:
           courseList = LinkedList(Course(row['name'], row['day'], row['endTime'], row['location']))
           headNode = courseList
           curNode = headNode
        else:
           curNode.next = LinkedList(Course(row['name'], row['day'], row['endTime'], row['location']))
           curNode = curNode.next

def checkTime():
   global curNode, headNode
   while True:
      #讀取LinedList物件
      tempNode = curNode.value
      # 取得當前的系統時間
      curTime = datetime.datetime.now()
      # 設定 GMT+8 的時區
      timezone = pytz.timezone("Asia/Taipei")
      # 將系統時間轉換為 GMT+8 時區的時間
      curTime = curTime.astimezone(timezone)
      curWeekday = curTime.strftime("%w")
      curHour = curTime.hour
      curMinute = curTime.minute
      #將LinkedList的資料轉成時間
      nodeTime = datetime.datetime.strptime(tempNode.startTime, "%H:%M")
      nodeHour = nodeTime.hour
      nodeMinute = nodeTime.minute
      if curWeekday == tempNode.day and (curHour * 60 + curMinute) - (nodeHour * 60 + nodeMinute) == 0:
         messageStr = f"課程通知\n課程名稱：{tempNode.name}\n教室：{tempNode.location}\n上課時間：{tempNode.startTime}\n下課時間：{tempNode.endTime}\n祝您上課愉快！"
         line_bot_api.push_message('U3b706ee724da7f1ccaf51c2fb357d507', TextSendMessage(text=messageStr))
         curNode = curNode.next
         if curNode == None:
            curNode = headNode
      time.sleep(1)

#接受使用者訊息(還沒動工)
@app.route("/")
def home():
  global line_bot_api
  try:
    # 網址被執行時，等同使用 GET 方法發送 request，觸發 LINE Message API 的 push_message 方法
    line_bot_api.push_message('U3b706ee724da7f1ccaf51c2fb357d507', TextSendMessage(text='使用者ID讀取成功'))
    return 'OK'
  except:
    print('error')

if __name__ == "__main__":
   # 啟動應用程式
   app_thread = threading.Thread(target=app.run)
   app_thread.start()

   # 定期偵測時間，每秒檢查一次
   check_thread = threading.Thread(target=checkTime)
   check_thread.start()