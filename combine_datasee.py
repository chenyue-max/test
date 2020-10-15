# -*- coding:UTF-8 -*-
from HTMLTable import (
    HTMLTable,
)
# coding:utf-8
import pandas as pd
import os
import webbrowser
# 命名生成的html
cd_A = '/var/sensordata/D_A-506-BMP180-GY30-TSL2561.csv'
cd_B = '/var/sensordata/D_B-506-BMP180-GY30.csv'
cd_C = '/var/sensordata/D_C-506-BMP180-GY30.csv'
cd_S = '/var/sensordata/D_S-506-BMP180-GY30.csv'
cd_nano = '/var/sensordata/server-sgf/tcpdata506-8008.csv'

data_A = pd.read_csv(cd_A).tail(1)
data_B = pd.read_csv(cd_B, encoding='gb18030').tail(1)
data_C = pd.read_csv(cd_C).tail(1)
data_S = pd.read_csv(cd_S).tail(1)
data_nano = pd.read_csv(cd_nano)
length = len(data_nano)
# 标题
table = HTMLTable(caption='506数据可视化')
# 表头行
table.append_header_rows((
    ('设备(ip)', '当前日期', '时间',           'CPU温度',
     '环境温度',  '湿度',    '气压', 'GY_30光强', 'TSL2560光强', '', '甲醛'),
    ('',        '',            '',            '',
     '',            '', '',      '', 't_v', 't_i', ''),

))
# 合并单元格
table[0][0].attr.rowspan = 2
table[0][1].attr.rowspan = 2
table[0][2].attr.rowspan = 2
table[0][3].attr.rowspan = 2
table[0][4].attr.rowspan = 2
table[0][5].attr.rowspan = 2
table[0][6].attr.rowspan = 2
table[0][7].attr.rowspan = 2
table[0][10].attr.rowspan = 2

table[0][8].attr.colspan = 2
# table[0][2].attr.colspan = 2

Y = []
K = []
L = []
Z = []
for i in range(length-1, 0, -1):
    if data_nano.iloc[i, 2] == 'Y-Tem-Press-Lig':
        Y.append(data_nano.iloc[i, 2])  # 设备
        Y.append(data_nano.iloc[i, 0])  # 日期
        Y.append(data_nano.iloc[i, 1])  # 时间
        Y.append(data_nano.iloc[i, 4])  # 温度
        Y.append(data_nano.iloc[i, 6])  # 气压
        Y.append(data_nano.iloc[i, 7])  # 光强
        break
for i in range(length-1, 0, -1):
    if data_nano.iloc[i, 2] == 'K-Tem-Press-Lig':
        K.append(data_nano.iloc[i, 2])  # 设备
        K.append(data_nano.iloc[i, 0])  # 日期
        K.append(data_nano.iloc[i, 1])  # 时间
        K.append(data_nano.iloc[i, 4])  # 温度
        K.append(data_nano.iloc[i, 6])  # 气压
        K.append(data_nano.iloc[i, 7])  # 光强
        break
for i in range(length-1, 0, -1):
    if data_nano.iloc[i, 2] == 'L-Tem-Press-Lig':
        L.append(data_nano.iloc[i, 2])  # 设备
        L.append(data_nano.iloc[i, 0])  # 日期
        L.append(data_nano.iloc[i, 1])  # 时间
        L.append(data_nano.iloc[i, 4])  # 温度
        L.append(data_nano.iloc[i, 6])  # 气压
        L.append(data_nano.iloc[i, 7])  # 光强
        break
for i in range(length-1, 0, -1):
    if data_nano.iloc[i, 2] == 'Z-Tem-Press-Lig':
        Z.append(data_nano.iloc[i, 2])  # 设备
        Z.append(data_nano.iloc[i, 0])  # 日期
        Z.append(data_nano.iloc[i, 1])  # 时间
        Z.append(data_nano.iloc[i, 4])  # 温度
        Z.append(data_nano.iloc[i, 6])  # 气压
        Z.append(data_nano.iloc[i, 7])  # 光强
        break


# 数据行
try:
    table.append_data_rows((
        ('A(192.168.3.200)', data_A.iloc[0, 0], data_A.iloc[0, 1], data_A.iloc[0, 2],
         data_A.iloc[0, 3], '', data_A.iloc[0, 4], data_A.iloc[0, 5], data_A.iloc[0, 6], data_A.iloc[0, 7], ''),
        ('B(192.168.3.208)', data_B.iloc[0, 0], data_B.iloc[0, 1], data_B.iloc[0, 2],
         data_B.iloc[0, 3], '', data_B.iloc[0, 4], data_B.iloc[0, 5], '', '', ''),
        ('C(192.168.3.215)', data_C.iloc[0, 0], data_C.iloc[0, 1], data_C.iloc[0, 2],
         data_C.iloc[0, 3], '', data_C.iloc[0, 4], data_C.iloc[0, 5], '', '', ''),
        ('S(192.168.3.180)', data_S.iloc[0, 0], data_S.iloc[0, 1], data_S.iloc[0, 2],
         data_S.iloc[0, 3], '', data_S.iloc[0, 4], data_S.iloc[0, 5], '', '', ''),
        (Y[0], Y[1], Y[2], '', Y[3], '', Y[4], Y[5], '', '', ''),
        (Z[0], Z[1], Z[2], '', Z[3], '', Z[4], Z[5], '', '', ''),
        (K[0], K[1], K[2], '', K[3], '', K[4], K[5], '', '', ''),
        (L[0], L[1], L[2], '', L[3], '', L[4], L[5], '', '', ''),
    ))
except:
    pass
# 标题样式
table.caption.set_style({
    'font-size': '15px',
})
# 表格样式，即<table>标签样式
table.set_style({
    'border-collapse': 'collapse',
    'word-break': 'keep-all',
    'white-space': 'nowrap',
    'font-size': '14px',
})
# 统一设置所有单元格样式，<td>或<th>
table.set_cell_style({
    'border-color': '#000',
    'border-width': '1px',
    'border-style': 'solid',
    'padding': '5px',
})
# 表头样式
table.set_header_row_style({
    'color': '#fff',
    'background-color': '#48a6fb',
    'font-size': '18px',
})

# 覆盖表头单元格字体样式
table.set_header_cell_style({
    'padding': '15px',
})
# 调小次表头字体大小
table[1].set_cell_style({
    'padding': '8px',
    'font-size': '15px',
})
# # 遍历数据行，如果增长量为负，标红背景颜色
# for row in table.iter_data_rows():
#     if row[2].value < 0:
#         row.set_style({
#             'background-color': '#ffdddd',
#         })
html = table.to_html()
filename = '/var/sensordata/html/506_devices_status.html'
with open(filename, 'w') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
    f.write("基于树莓派的数据可视化网页\n")
    f.write(html)


"""
table.append_header_rows((
    ('名称',    '产量 (吨)',    '环比',             ''),
    ('',        '',             '增长量 (吨)',      '增长率 (%)'),
))
"""
