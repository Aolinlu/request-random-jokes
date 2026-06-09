import json
import random
import sys
from urllib.request import urlopen

# API映射表
API_MAP = {
    "xiaohua": "https://v.api.aa1.cn/api/api-wenan-gaoxiao/index.php?aa1=json",
    "duanzi": "https://v.api.aa1.cn/api/api-wenan-gaoxiao/index.php?aa1=json",
    "dujitang": "https://v.api.aa1.cn/api/api-wenan-dujitang/index.php?aa1=json"
}

def parse_content(raw_content):
    content = raw_content.strip().strip('"')
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        return content

    if isinstance(data, list) and data:
        data = data[0]

    if isinstance(data, dict):
        for value in data.values():
            if isinstance(value, str):
                return value.strip()

    if isinstance(data, str):
        return data.strip()

    return content

def get_content(api_url):
    with urlopen(api_url, timeout=3) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return parse_content(response.read().decode(charset))

if __name__ == "__main__":
    # 解析参数
    if len(sys.argv) > 1:
        req_type = sys.argv[1].lower()
        if req_type in API_MAP:
            api_url = API_MAP[req_type]
        else:
            # 无效参数时随机选一个
            api_url = random.choice(list(API_MAP.values()))
    else:
        # 无参数时随机选一个API
        api_url = random.choice(list(API_MAP.values()))
    
    content = get_content(api_url)
    print(content)
