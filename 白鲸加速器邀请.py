import random
from fake_useragent import UserAgent
import requests
import string

# 定义一个函数，用于获取随机的User-Agent
def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
    ]
    return random.choice(user_agents)

# 定义一个函数，用于生成指定长度的随机字符串
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# 定义一个函数，用于生成随机的设备信息
def generate_random_device_info():
    device_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=32))
    model = generate_random_string(8) + "-Redmi"
    return device_id, model

# 定义请求的URL
url = "https://wa01.googla.org/account/register"

# 定义请求参数
params = {
    "platform": "2",
    "api_version": "14",
    "app_version": "1.45",
    "lang": "zh",
    "_key": "",
    "market_id": "1000",
    "pkg": "com.bjchuhai",
    "sys_version": "13",
    "ts": "1714675386019",
    "sub_pkg": "com.bjchuhai",
    "version_code": "45",
}

# 循环发送10次请求
for _ in range(10):
    # 生成随机的设备信息和邮箱
    device_id, model = generate_random_device_info()
    email = generate_random_string(3) + "UserAgent@gmail.com"

    # 定义请求体
    payload = {
        "passwd": "31eeca8fa1484673311de3602ced6e5c",
        "invite_code": "5NC35",
        "email": email
    }

    # 获取随机的User-Agent
    user_agent = get_random_user_agent()

    # 定义请求头
    headers = {
        "User-Agent": user_agent
    }

    # 合并参数
    params["device_id"] = device_id
    params["model"] = model

    # 发送请求
    response = requests.post(url, data=payload, headers=headers, params=params)

    # 打印响应状态码和响应内容
    print("Response status code:", response.status_code)
    print("Response content:", response.text)