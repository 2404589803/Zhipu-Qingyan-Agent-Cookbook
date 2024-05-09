import json
import requests

def handle_response(data_dict):
    message = data_dict.get("message")
    if len(message) > 0:
        content = message.get("content")
        if len(content) > 0:
            response_type = content.get("type")
            if response_type == "text":
                text = content.get("text", "No text provided")
                return f"{text}"

            elif response_type == "image":
                images = content.get("image", [])
                image_urls = ", ".join(image.get("image_url") for image in images)
                return f"{image_urls}"

            elif response_type == "code":
                return f"{content.get('code')}"

            elif response_type == "execution_output":
                return f"{content.get('content')}"

            elif response_type == "system_error":
                return f"{content.get('content')}"

            elif response_type == "tool_calls":
                return f"{data_dict['tool_calls']}"

            elif response_type == "browser_result":
                content = json.loads(content.get("content", "{}"))
                return f"Browser Result - Title: {content.get('title')} URL: {content.get('url')}"


def send_message(assistant_id, access_token, prompt, conversation_id=None, file_list=None, meta_data=None):
    url = "https://chatglm.cn/chatglm/assistant-api/v1/stream"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "assistant_id": assistant_id,
        "prompt": prompt,
    }


    if conversation_id:
        data["conversation_id"] = conversation_id
    if file_list:
        data["file_list"] = file_list
    if meta_data:
        data["meta_data"] = meta_data

    with requests.post(url, json=data, headers=headers) as response:
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    if decoded_line.startswith('data:'):
                        data_dict = json.loads(decoded_line[5:])
                        output = handle_response(data_dict)


        else:
            return "Request failed", response.status_code
        print(output)
    

assistant_id = "66144184ae0b09fe5019e4fe" 
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNTE3NDQ4NCwianRpIjoiMGI5NWY2NDAtY2Y0OS00OTJkLTkyNjAtYjFhZWY1OTlmODEzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IkFQSV82NDZkZDhhMTEyNTlhMmYwZjI2NjEzM2FfY2M4OWQ4OGQiLCJuYmYiOjE3MTUxNzQ0ODQsImV4cCI6MTcxNjAzODQ4NCwidWlkIjoiNjYzYWVkOTUwNzQ5NWFkMTA4ODg3ODFhIiwidXBsYXRmb3JtIjoiIiwicm9sZXMiOlsiYXV0aGVkX3VzZXIiXX0.Y3F2HUAh2AdmfINuVHsRxt21x8xXrRKyR1nNQDQG23k"
prompt = "你是谁"
result = send_message(assistant_id, access_token, prompt)
result
