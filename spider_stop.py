import requests
import csv
import json
import os


TOKEN = 'eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE3MDc2MjM5OTl9.Yp7UnI_XLKojchK4hAf0S2tVFqHEHG5nD4kI5DsAenc'

with open('lines.csv', 'r', encoding='utf-8') as f:
    r = csv.reader(f)
    h = next(r)
    lines = list(r)
for line in lines:
    line_id = line[h.index('lineId')]
    line_name = line[h.index('caption')]
    r = requests.post(
        'https://www.bjbus.com/api/api_etastation.php?lineId={}&token={}'.format(line_id, TOKEN),
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
    )
    r.encoding = 'utf-8'
    j = json.loads(r.text)
    data = j['data']
    header = list(data[0].keys())
    with open(os.path.join('stops', '{}_{}'.format(line_id, line_name)), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(header)
        for each in data:
            w.writerow(list(each.values()))
    print(line_id, line_name, len(data))

    