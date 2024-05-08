import requests

def get_token(api_key, api_secret):
    url = "https://chatglm.cn/chatglm/assistant-api/v1/get_token"
    payload = {
        'api_key': api_key,
        'api_secret': api_secret
    }
    response = requests.post(url, json=payload)
    print(response.text)  # 打印返回结果

# 使用示例
api_key = '51d5350a075931c7'
api_secret = 'fa2eab916c0705fd6b120434ddd98e96'
access_token, expires_in = get_token(api_key, api_secret)

