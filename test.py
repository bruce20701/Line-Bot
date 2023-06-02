from model import Course, LinkedList
import time
import datetime
import pytz
import csv

# LinkedList基本配置
courseList = None
headNode = None
curNode = None

#讀取課程資訊
with open('test.csv', mode='r') as file:
   reader = csv.DictReader(file)
   for row in reader:
      if courseList == None:
         courseList = LinkedList(Course(row['name'], row['day'], row['startTime'], row['endTime'], row['location']))
         headNode = courseList
         curNode = headNode
      else:
         curNode.next = LinkedList(Course(row['name'], row['day'], row['startTime'], row['endTime'], row['location']))
         curNode = curNode.next
   curNode = headNode

def checkTime():
   global curNode, headNode
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
   print(f"系統時間: Hour:{curHour}Minute:{curMinute}")
   #將LinkedList的資料轉成時間
   nodeTime = datetime.datetime.strptime(tempNode.startTime, "%H:%M")
   nodeHour = nodeTime.hour
   nodeMinute = nodeTime.minute
   print(f"Node時間: Hour:{nodeHour}Minute:{nodeMinute}")
   if curWeekday == tempNode.day and (curHour * 60 + curMinute) - (nodeHour * 60 + nodeMinute) == 0:
      messageStr = f"課程通知\n課程名稱：{tempNode.name}\n教室：{tempNode.location}\n上課時間：{tempNode.startTime}\n下課時間：{tempNode.endTime}\n祝您上課愉快！"
      print(messageStr)
      curNode = curNode.next
      if curNode == None:
         curNode = headNode

if __name__ == "__main__":
   #定期偵測時間，每秒檢查一次
   while True:
      checkTime()
      time.sleep(10)
