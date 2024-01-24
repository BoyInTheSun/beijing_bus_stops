import requests
import json
import csv

def search_line_list(keyword):
    r = requests.get(
        'https://www.bjbus.com/api/api_etaline_list.php?hidden_MapTool=busex2.BusInfo&city=%25u5317%25u4EAC&pageindex=1&pagesize=30&fromuser=bjbus&datasource=bjbus&clientid=&webapp=mobilewebapp&what={}'.format(keyword),
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
    )
    print(keyword)
    j = json.loads(r.text)
    data = j['response']['resultset']['data']['feature']
    if len(data) < 25:
        return data
    else:
        data = list()
        for i in range(10):
            r = requests.get(
                'https://www.bjbus.com/api/api_etaline_list.php?hidden_MapTool=busex2.BusInfo&city=%25u5317%25u4EAC&pageindex=1&pagesize=30&fromuser=bjbus&datasource=bjbus&clientid=&webapp=mobilewebapp&what={}{}'.format(keyword, i),
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                }
            )
            print(keyword, i)
            j = json.loads(r.text)
            if not j['response']['resultset']:
                continue
            temp = j['response']['resultset']['data']['feature']
            if len(temp) < 25:
                data += temp
            else:
                for ii in range(10):
                    r = requests.get(
                        'https://www.bjbus.com/api/api_etaline_list.php?hidden_MapTool=busex2.BusInfo&city=%25u5317%25u4EAC&pageindex=1&pagesize=30&fromuser=bjbus&datasource=bjbus&clientid=&webapp=mobilewebapp&what={}{}{}'.format(keyword, i, ii),
                        headers={
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                        }
                    )
                    print(keyword, i, ii)
                    j = json.loads(r.text)
                    if not j['response']['resultset']:
                        continue
                    data += j['response']['resultset']['data']['feature']
        return data
        

data = list()
for k in list('123456789CFH临MSTXY专夜') + ['快速公交', '快速直达专线', '通勤', '北京朝阳站地铁直达摆渡线']:
    data += search_line_list(k)

header = list(data[0].keys())

with open('lines.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(header)
    for each in data:
        w.writerow(list(each.values()))
