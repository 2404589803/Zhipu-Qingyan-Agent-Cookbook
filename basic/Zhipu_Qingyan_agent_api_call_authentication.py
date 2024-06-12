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
api_key = '8f56297340d49c41'
api_secret = '7b835faace25445957facc440a012bd4'
access_token, expires_in = get_token(api_key, api_secret)

