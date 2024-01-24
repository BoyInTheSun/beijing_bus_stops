import csv
import os
import json

data = dict()  # {stopName: [lineId, ...]}

filenames = os.listdir('stops')
for filename in filenames:
    with open(os.path.join('stops', filename), encoding='utf-8') as f:
        r = csv.reader(f)
        h = next(r)
        lines = list(r)
    for line in lines:
        if not line[h.index('stopName')] in data:
            data[line[h.index('stopName')]] = list()
        if line[h.index('lineId')] not in data[line[h.index('stopName')]]:
            data[line[h.index('stopName')]].append(line[h.index('lineId')])
# 排序
data = {x: sorted(data[x]) for x in data}
data_sorted = sorted(data.items(), key=lambda x: len(x[1]), reverse=True)
data_sorted = {x[0]: x[1] for x in data_sorted}


with open('stops.json', 'w', encoding='utf-8') as f:
    json.dump(data_sorted, f, ensure_ascii=False)


'''
data = sorted(data.items(), key=lambda x: x[0])  # 排序

with open('stops.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['stationId', 'stopName', 'lineIds'])
    w.writerows(data)
'''
