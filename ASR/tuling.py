# coding=utf-8
import requests
import json
 
 
def tuling(text='I said nothing'):
    # 与图灵机器人对话
    tuling_url = 'http://www.tuling123.com/openapi/api'
    tuling_date = {
        'key': '4527c40a4ee64b2bb4ca92cf020847be',
        'info': text
    }  # 使用时请将key更换为你自己的
    r = requests.post(tuling_url, data=tuling_date)
    return json.loads(r.text)['text']
 
# 调用示例
#reply = tuling('你吃饭了吗？')
#print(reply)
