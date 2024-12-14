import requests
import json
import time
import os
from sys import argv

def get_video_stats(bvid):
    API = 'https://api.bilibili.com/x/web-interface/view?bvid={}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    url = API.format(bvid)
    data = requests.get(url, headers=headers).json()
    # for key in ('view', 'danmaku', 'reply', 'favorite', 'coin', 'share', 'like'):
    return {key: data['data']['stat'][key] for key in ('view', 'danmaku', 'reply', 'favorite', 'coin', 'share', 'like')}

BVID = argv[1]

if os.path.exists(f'results/{BVID}.json'):
    with open(f'results/{BVID}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
else:
    data = {}
data[int(time.time())] = get_video_stats(BVID)
with open(f'results/{BVID}.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)