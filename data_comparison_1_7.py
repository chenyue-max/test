import csv
import pandas as pd
import datetime
from pyecharts.charts import Line,Page
from pyecharts import options as opts


A_file="D_A-506-BMP180-GY30-TSL2561.csv"
B_file="D_B-506-BMP180-GY30.csv"
C_file="D_C-506-BMP180-GY30.csv"
S_file="D_S-506-BMP180-GY30.csv"
use_date_list=[]
date_list=[]
A_temp_data_list = []
B_temp_data_list = []
C_temp_data_list = []
S_temp_data_list = []
A_lum_data_list = []
B_lum_data_list = []
C_lum_data_list = []
S_lum_data_list = []
#制作时间轴

#删除前面大概70000条信息
with open(A_file) as f:
    reader = csv.reader(f)
    A_rows = [row for row in reader]
del A_rows[:70000]
#找到最新日期的前七天
the_end_date=A_rows[-1][0]
the_begin_date=str(pd.date_range(end=the_end_date, periods=7)[0])[:10]
the_begin_date=str(datetime.datetime.strptime(the_begin_date,"%Y-%m-%d"))[:10]
#将日期格式化，通过比较大小筛选出七天的时间数据
for i in range(len(A_rows)):
    A_rows[i][0]= str(datetime.datetime.strptime(A_rows[i][0].replace('/','-'), "%Y-%m-%d"))[:10]
for i in range(len(A_rows)):
    if (A_rows[i][0]>=the_begin_date):
        use_date_list.append(A_rows[i])
for row in use_date_list:
    date_list.append(row[0]+' '+str(datetime.datetime.strptime(row[1].replace('/','-'), '%H:%M'))[11:16])
    A_temp_data_list.append(row[3])
    A_lum_data_list.append(row[5])
number=len(date_list)
#提取出B C S 的温度.光强
with open(B_file) as f:
    reader = csv.reader(f)
    B_rows = [row for row in reader]
B_rows=B_rows[-number:]
for row in B_rows:
    B_temp_data_list.append(row[3])
    B_lum_data_list.append(row[5])
with open(C_file) as f:
    reader = csv.reader(_.replace('\x00', '') for _ in f)
    C_rows = [row for row in reader]
C_rows=C_rows[-number:]
for row in C_rows:
    C_temp_data_list.append(row[3])
    C_lum_data_list.append(row[5])
with open(S_file) as f:
    reader = csv.reader(f)
    S_rows = [row for row in reader]
S_rows=S_rows[-number:]
for row in S_rows:
    S_temp_data_list.append(row[3])
    S_lum_data_list.append(row[5])
#画出A B C S 温度的折线图
ABCS_temp_line= (Line(init_opts=opts.InitOpts(width="680px", height="450px"))
                       .set_global_opts(title_opts=opts.TitleOpts(title="温度折线图"),
                                        tooltip_opts=opts.TooltipOpts(trigger="axis"),
                                        toolbox_opts=opts.ToolboxOpts(is_show=False),
                                        yaxis_opts=opts.AxisOpts(
                                            type_="value",
                                            name=' temp(℃)',
                                            axistick_opts=opts.AxisTickOpts(is_show=True),
                                            splitline_opts=opts.SplitLineOpts(is_show=True),
                                            max_=float(max(A_temp_data_list))+3,
                                            min_=float(min(A_temp_data_list))-3,

                                        ),
                                        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=True,
                                                                 name='date',
                                                                ),

                                        datazoom_opts=[
                                            opts.DataZoomOpts(range_start=0, range_end=100,
                                                               xaxis_index=0, type_="inside"),
                                        ])
                       .add_xaxis(date_list)
                       .add_yaxis('A', A_temp_data_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('B',B_temp_data_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('C', C_temp_data_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('S ',S_temp_data_list , label_opts=opts.LabelOpts(is_show=False),
                                 )
                       )
#画出A B C S 光强的折线图
ABCS_lum_line=(Line(init_opts=opts.InitOpts(width="680px", height="450px"))
                       .set_global_opts(title_opts=opts.TitleOpts(title="光强折线图"),
                                        tooltip_opts=opts.TooltipOpts(trigger="axis"),
                                        toolbox_opts=opts.ToolboxOpts(is_show=False),
                                        yaxis_opts=opts.AxisOpts(
                                            type_="value",
                                            name='lum(cd/m²)',is_scale=True,
                                            axistick_opts=opts.AxisTickOpts(is_show=True),
                                            splitline_opts=opts.SplitLineOpts(is_show=True),
                                        ),
                                        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,
                                                                 name='date'),
                                        datazoom_opts=[
                                            opts.DataZoomOpts(range_start=0, range_end=100,
                                                              xaxis_index=0, type_="inside"),
                                        ],
                                        )
                       .add_xaxis(date_list)
                       .add_yaxis('A', A_lum_data_list ,markpoint_opts=opts.MarkPointOpts(
        ),label_opts=opts.LabelOpts(is_show=False),
                                 )
                       .add_yaxis('B',B_lum_data_list ,        markpoint_opts=opts.MarkPointOpts(
        ), label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('C', C_lum_data_list ,        markpoint_opts=opts.MarkPointOpts(
        ), label_opts=opts.LabelOpts(is_show=False),
                                )
                       .add_yaxis('S ',S_lum_data_list ,        markpoint_opts=opts.MarkPointOpts(
        ), label_opts=opts.LabelOpts(is_show=False),
                                )
                       )




page = Page(layout=Page.SimplePageLayout)
page.add(ABCS_temp_line,ABCS_lum_line)
page.render('ABCS_comparison_line_7.html')






















