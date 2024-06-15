import requests
import os

# 从环境变量中获取sb，并将其分割为accounts列表
accounts = os.environ.get("sb").split("@")

# 设置请求头
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://www.gobing.cn',
    'Referer': 'https://www.gobing.cn/',
    'sec-ch-ua': '"Chromium";v="9", "Not?A_Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.1311 SLBChan/105'
}

# 遍历accounts列表，获取uid和password
for account in accounts:
    uid, password = account.split("#")
    data = {
        "account": uid,
        "password": password
    }

    try:
        # 发送请求，获取响应
        resp1 = requests.post("https://api.gobing.cn/v1/user/login", headers=headers, json=data)
        resp1.raise_for_status()
        parsed_response = resp1.json()
        token = parsed_response['data']['token']

        # 如果token存在，则登录成功
        if token:
            print(f"登录成功: {uid}")
            headers["token"] = token
            print(token)
            resp = requests.post("https://api.gobing.cn/v1/signin/signin", headers=headers)
            print(resp.text)
        else:
            print(f"登陆失败: {uid}")
    except requests.exceptions.RequestException as e:
        print(e)
