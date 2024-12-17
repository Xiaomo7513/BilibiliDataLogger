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
    # [<播放量>, <弹幕数>, <评论数>, <收藏数>, <硬币数>, <分享数>, <点赞数>]
    return [data['data']['stat'][key] for key in ('view', 'danmaku', 'reply', 'favorite', 'coin', 'share', 'like')]

BVID = argv[1]

if os.path.exists(f'results/{BVID}.json'):
    with open(f'results/{BVID}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
else:
    if not os.path.exists('results'): os.mkdir('results')
    data = {}
data[time.strftime('%Y%m%d')] = get_video_stats(BVID)
with open(f'results/{BVID}.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, separators=(',', ':'))