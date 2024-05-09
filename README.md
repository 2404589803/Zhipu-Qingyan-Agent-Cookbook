<h1>
  <img src="asset/glm.png" alt="glm" style="height: 1.5em; vertical-align: bottom;" />
  Zhipu-Qingyan-Agent-cookbook
</h1>

目前是第（1）版

在今天，智谱AI终于开放了智谱清言智能体api调用的功能，这个功能的公开，代表着智谱清言生态的进一步扩大。智能体的应用不再限于网页和手机app应用中，而真正进入了开发者的群体中！通过对智能体api的调用，及开发者社区的强大的创造能力，对智谱清言生态益处可谓是更上一层楼！

接下来，我将逐一实践智谱清言智能体api调用的功能，然后使用我目前正在开发的项目，与智谱清言智能体api调用相结合。让我们看看会有什么奇妙的化学反应发生！😜

但请注意，当前智谱清言智能体仅支持通过API方式调用创作者自己创建的智能体。

## 智谱清言智能体api调用鉴权

### 获取access_token

与ChatGLM的api调用有一定的相似之处。

首先，在鉴权之前，我们先需要获取Access Token。

第一步，打开以下网址：

https://chatglm.cn/developersPanel/apiSet

找到智能体API管理界面

界面如下：

![alt text](asset/1.png)

然后点击新建，再输入名称。

最后新建的结果如下图：

![alt text](asset/2.png)

根据使用文档的定义，我编写了一个用于Access Token获取的脚本。

[Access Token获取](basic/Zhipu_Qingyan_agent_api_call_authentication.py)

脚本运行完成之后，得到的信息如下：

```json

{"message":"success","result":{"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNTE3NDQ4NCwianRpIjoiMGI5NWY2NDAtY2Y0OS00OTJkLTkyNjAtYjFhZWY1OTlmODEzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IkFQSV82NDZkZDhhMTEyNTlhMmYwZjI2NjEzM2FfY2M4OWQ4OGQiLCJuYmYiOjE3MTUxNzQ0ODQsImV4cCI6MTcxNjAzODQ4NCwidWlkIjoiNjYzYWVkOTUwNzQ5NWFkMTA4ODg3ODFhIiwidXBsYXRmb3JtIjoiIiwicm9sZXMiOlsiYXV0aGVkX3VzZXIiXX0.Y3F2HUAh2AdmfINuVHsRxt21x8xXrRKyR1nNQDQG23k","expires_in":864000,"token_expires":1716038484},"status":0}
```

## 智谱清言智能体api调用智能体

在获取到Access Token之后，我们就可以通过API调用智能体了。在本次调用中，我用了 **智解LaTeX** 这个
智能体，首先，我们需要在网页端打开这个智能体的页面，获取智能体的ID。

![alt text](asset/3.png)

接着，我们将浏览器链接最右边的字符串复制下来，即：66144184ae0b09fe5019e4fe（这个智能体的ID）

![alt text](asset/4.png)

为了调用智能体，我使用了以下代码进行了智能体的调用。

同时为了输出的美观，我也使用了SSE（流式）输出。代码如下：


[智谱清言智能体api调用](basic/Zhipu_Qingyan_agent_api_assistant_session_call.py)


在实际开发中，我们需要修改ssistant_id（智能体ID，更换智能体时修改）、access_token（填入你第一步获取到的access_token）、prompt（提示词）这三个参数。

运行代码，得到的结果如下：

```text

你好，我是智解LaTeX，一个专门用于将数学公式描述转换为LaTeX代码的AI助手。我的主要功能是帮助用户简化数学排版的流程，无论是从文字描述到公式，还是从图片到公式，我都能提供高效的转换服务。我的目标是让用户的数学排版工作更加便捷和高效。

```

智能体的调用工作便完成了。
