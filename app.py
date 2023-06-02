from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage

app = Flask(__name__)

@app.route("/")
def home():
  line_bot_api = LineBotApi('你的 access token')
  try:
    # 網址被執行時，等同使用 GET 方法發送 request，觸發 LINE Message API 的 push_message 方法
    line_bot_api.push_message('你的 User ID', TextSendMessage(text='Hello World!!!'))
    return 'OK'
  except:
    print('error')

if __name__ == "__main__":
    app.run()