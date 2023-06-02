from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage   # 載入 TextSendMessage 模組
from linebot.models import StickerSendMessage   # 載入 StickerSendMessage 模組
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        line_bot_api = LineBotApi('c/2axBtAYZQkLSDHOVVnBLXdJLs0RabigC1tvKtEbNb8/8P6f14yLRrfAQKKiUH6KgcdQp+bDHEyI7qP0/zHpvJflIKqIFRl/l2fbVvQS3txUy1LcNpHR/iCIjjmshTzt5zQQrjEGbsLx2MorQ6CcAdB04t89/1O/w1cDnyilFU=') #Channel access token
        handler = WebhookHandler('124fa4bcf00b1166c14eeea6bc6f2d00') #LINE Channel secret
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']         # 取得 reply token
        stickerId = json_data['events'][0]['message']['stickerId'] # 取得 stickerId
        packageId = json_data['events'][0]['message']['packageId'] # 取得 packageId
        sticker_message = StickerSendMessage(sticker_id=10855, package_id=789) # 設定要回傳的表情貼圖
        line_bot_api.reply_message(tk,sticker_message)  # 回傳訊息
    except:
        print('error')
    return 'OK'

if __name__ == "__main__":
    app.run()