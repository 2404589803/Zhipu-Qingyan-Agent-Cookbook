import requests

def get_token(api_key, api_secret):
    url = "https://chatglm.cn/chatglm/assistant-api/v1/get_token"
    payload = {
        'api_key': api_key,
        'api_secret': api_secret
    }
    response = requests.post(url, json=payload)
    print(response.text)  # 打印返回结果
    if response.status_code == 200:
        data = response.json()
        access_token = data['access_token']
        expires_in = data['expires_in']
        return access_token, expires_in
    else:
        print(f"获取access token失败，状态码：{response.status_code}")
        return None, None

# 使用示例
api_key = '你的api_key'
api_secret = '你的api_secret'
access_token, expires_in = get_token(api_key, api_secret)

if access_token:
    print(f"获取成功，access_token: {access_token}")
    print(f"过期时间：{expires_in}秒")

