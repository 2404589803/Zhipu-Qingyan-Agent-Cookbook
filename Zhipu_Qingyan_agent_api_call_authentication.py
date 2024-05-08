import requests

# 填入你的api_key和api_secret
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"

# 构造请求数据
data = {
    "api_key": api_key,
    "api_secret": api_secret
}

# 发送POST请求
url = "https://chatglm.cn/chatglm/assistant-api/v1/get_token"
response = requests.post(url, data=data)

# 检查响应状态码
if response.status_code == 200:
    # 请求成功，获取access_token和expires_in
    result = response.json()
    access_token = result["access_token"]
    expires_in = result["expires_in"]
    print(f"Access Token: {access_token}")
    print(f"Expires In: {expires_in} seconds")
else:
    # 请求失败，打印错误信息
    print(f"Error: {response.status_code} - {response.text}")

