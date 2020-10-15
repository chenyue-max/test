import csv
import datetime
import data_comparison_1_7
from pyecharts.charts import Line,Page
from pyecharts import options as opts
file_csv='tcpdata506-8008.csv'
date_list=data_comparison_1_7.date_list
Y_data_list = []
Y_temp_data_list=[]
Y_lum_data_list = []
K_data_list = []
K_temp_data_list=[]
K_lum_data_list = []
L_data_list = []
L_temp_data_list=[]
L_lum_data_list = []
O_data_list = []
O_temp_data_list=[]
O_lum_data_list = []
P_data_list = []
P_temp_data_list=[]
P_lum_data_list = []
Q_data_list = []
Q_temp_data_list=[]
Q_lum_data_list = []


with open(file_csv) as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
    del rows[0:27745]
for row in rows:
    row[0]=row[0].replace("/", "-")
    row[0]=str(datetime.datetime.strptime(row[0], "%Y-%m-%d"))[0:10]
    row[1] =str(datetime.datetime.strptime(row[1], "%H:%M:%S"))[11:19]




# Y
for row in rows:
    if (row[0] >= date_list[0][0:10] ):
        if (row[2] == 'Y-Tem-Press-Lig' or row[2] == 'Anano-R3C2Y-Tem-Press-Lig'):
            if(len(Y_data_list)==0):
                Y_data_list .append(row)
            if(Y_data_list[-1][1][3]!=row[1][3]):
                Y_data_list.append(row)
a=0
for i in range(len(date_list)):
        if(date_list[i][0:10]==Y_data_list[a][0] and date_list[i][11:15]==Y_data_list[a][1][0:4]):
            Y_temp_data_list.append(float(Y_data_list[a][4]))
            Y_lum_data_list.append(float(Y_data_list[a][7]))
            a=a+1
        else:
            Y_temp_data_list.append(0)
            Y_lum_data_list.append(0)
print(Y_data_list[509])
print(date_list[517])
#k
for row in rows:
    if (row[0] >= date_list[0][0:10]):
        if (row[2] == 'K-Tem-Press-Lig' or row[2] == 'Anano-R1C1K-Tem-Press-Lig'):
            if(len(K_data_list)==0):
                K_data_list .append(row)
            if(K_data_list[-1][1][3]!=row[1][3]):
                K_data_list.append(row)
a=0
for i in range(len(date_list)):
    if(i<=len(K_data_list)):
        if(date_list[i][0:10]==K_data_list[a][0] and date_list[i][11:15]==K_data_list[a][1][0:4]):
            K_temp_data_list.append(float(K_data_list[a][4]))
            K_lum_data_list.append(float(K_data_list[a][7]))
            a=a+1
        else:
            K_temp_data_list.append(0)
            K_lum_data_list.append(0)
    else:
        K_temp_data_list.append(0)
        K_lum_data_list.append(0)

# L
for row in rows:
    if (row[0] >= date_list[0][0:10]):
        if (row[2] == 'L-Tem-Press-Lig' or row[2] == 'Anano-R2C1L-Tem-Press-Lig'):
            if(len(L_data_list)==0):
                L_data_list .append(row)
            if(L_data_list[-1][1][3]!=row[1][3]):
                L_data_list.append(row)
a=0
for i in range(len(date_list)):
    if(i<=len(L_data_list)):
        if(date_list[i][0:10]==L_data_list[a][0] and date_list[i][11:15]==L_data_list[a][1][0:4]):
            L_temp_data_list.append(float(L_data_list[a][4]))
            L_lum_data_list.append(float(L_data_list[a][7]))
            a=a+1
        else:
            L_temp_data_list.append(0)
            L_lum_data_list.append(0)
    else:
        L_temp_data_list.append(0)
        L_lum_data_list.append(0)

#O
for row in rows:
    if (row[0] >= date_list[0][0:10]):
        if (row[2] == 'O-Tem-Press-Lig' or row[2] == 'Anano-R3C10-Tem-Press-Lig'):
            if(len(O_data_list)==0):
                O_data_list .append(row)
            if(O_data_list[-1][1][3]!=row[1][3]):
                O_data_list.append(row)
a=0
for i in range(len(date_list)):
        if(date_list[i][0:10]==O_data_list[a][0] and date_list[i][11:15]==O_data_list[a][1][0:4]):
            O_temp_data_list.append(float(O_data_list[a][4]))
            O_lum_data_list.append(float(O_data_list[a][7]))
            a=a+1
        else:
            O_temp_data_list.append(0)
            O_lum_data_list.append(0)


#P
for row in rows:
    if (row[0] >= date_list[0][0:10]):
        if (row[2] == 'P-Tem-Press-Lig' or row[2] == 'Anano-R3C2P-Tem-Press-Lig'):
            if(len(P_data_list)==0):
                P_data_list .append(row)
            if(P_data_list[-1][1][3]!=row[1][3]):
                P_data_list.append(row)
a=0

for i in range(len(date_list)):
        if(date_list[i][0:10]==P_data_list[a][0] and date_list[i][11:15]==P_data_list[a][1][0:4]):
            P_temp_data_list.append(float(P_data_list[a][4]))
            P_lum_data_list.append(float(P_data_list[a][7]))
            a=a+1
        else:
            P_temp_data_list.append(0)
            P_lum_data_list.append(0)

#Q
for row in rows:
    if (row[0] >= date_list[0][0:10]):
        if (row[2] == 'Q-Tem-Press-Lig' or row[2] == 'Anano-R3C3Q-Tem-Press-Lig'):
            if(len(Q_data_list)==0):
                Q_data_list .append(row)
            if(Q_data_list[-1][1][3]!=row[1][3]):
                Q_data_list.append(row)
a=0
for i in range(len(date_list)):
    if(i<=len(Q_data_list)):
            if(date_list[i][0:10]==Q_data_list[a][0] and date_list[i][11:15]==Q_data_list[a][1][0:4]):
                Q_temp_data_list.append(float(Q_data_list[a][4]))
                Q_lum_data_list.append(float(Q_data_list[a][7]))
                a=a+1
            else:
                Q_temp_data_list.append(0)
                Q_lum_data_list.append(0)
    else:
        Q_temp_data_list.append(0)
        Q_lum_data_list.append(0)

#画出YKL 温度的折线图
YKL_temp_line= (Line(init_opts=opts.InitOpts(width="680px", height="450px"))
                       .set_global_opts(title_opts=opts.TitleOpts(title="温度折线图"),
                                        tooltip_opts=opts.TooltipOpts(trigger="axis"),
                                        toolbox_opts=opts.ToolboxOpts(is_show=False),
                                        yaxis_opts=opts.AxisOpts(
                                            type_="value",
                                            name=' temp(℃)',
                                            axistick_opts=opts.AxisTickOpts(is_show=True),
                                            splitline_opts=opts.SplitLineOpts(is_show=True),
                                            max_=float(max(Y_temp_data_list))+3,
                                            min_=float(min(Y_temp_data_list))-3,

                                        ),
                                        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=True,
                                                                 name='date',
                                                                ),

                                        datazoom_opts=[
                                            opts.DataZoomOpts(range_start=0, range_end=100,
                                                               xaxis_index=0, type_="inside"),
                                        ])
                       .add_xaxis(date_list)
                       .add_yaxis('Y', Y_temp_data_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('K',K_temp_data_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('L', L_temp_data_list , label_opts=opts.LabelOpts(is_show=False),
                                  )

                                 )

#画出OPQ 温度的折线图
OPQ_temp_line= (Line(init_opts=opts.InitOpts(width="680px", height="450px"))
                       .set_global_opts(title_opts=opts.TitleOpts(title="温度折线图"),
                                        tooltip_opts=opts.TooltipOpts(trigger="axis"),
                                        toolbox_opts=opts.ToolboxOpts(is_show=False),
                                        yaxis_opts=opts.AxisOpts(
                                            type_="value",
                                            name=' temp(℃)',
                                            axistick_opts=opts.AxisTickOpts(is_show=True),
                                            splitline_opts=opts.SplitLineOpts(is_show=True),
                                            max_=float(max(O_temp_data_list))+3,
                                            min_=float(min(O_temp_data_list))-3,

                                        ),
                                        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=True,
                                                                 name='date',
                                                                ),

                                        datazoom_opts=[
                                            opts.DataZoomOpts(range_start=0, range_end=100,
                                                               xaxis_index=0, type_="inside"),
                                        ])
                       .add_xaxis(date_list)
                       .add_yaxis('O', O_temp_data_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('P',P_temp_data_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('Q', Q_temp_data_list , label_opts=opts.LabelOpts(is_show=False),
                                  )

                                 )

#画出YKL 光强的折线图
YKL_lum_line=(Line(init_opts=opts.InitOpts(width="680px", height="450px"))
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
                       .add_yaxis('Y', Y_lum_data_list ,markpoint_opts=opts.MarkPointOpts(
        ),label_opts=opts.LabelOpts(is_show=False),
                                 )
                       .add_yaxis('K',K_lum_data_list ,        markpoint_opts=opts.MarkPointOpts(
        ), label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('L', L_lum_data_list ,        markpoint_opts=opts.MarkPointOpts(
        ), label_opts=opts.LabelOpts(is_show=False),


                                )
                       )
# 画出OPQ 光强的折线图
OPQ_lum_line = (Line(init_opts=opts.InitOpts(width="680px", height="450px"))
                .set_global_opts(title_opts=opts.TitleOpts(title="光强折线图"),
                                 tooltip_opts=opts.TooltipOpts(trigger="axis"),
                                 toolbox_opts=opts.ToolboxOpts(is_show=False),
                                 yaxis_opts=opts.AxisOpts(
                                     type_="value",
                                     name='lum(cd/m²)', is_scale=True,
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
                .add_yaxis('O', O_lum_data_list, markpoint_opts=opts.MarkPointOpts(
), label_opts=opts.LabelOpts(is_show=False),
                           )
                .add_yaxis('P', P_lum_data_list, markpoint_opts=opts.MarkPointOpts(
), label_opts=opts.LabelOpts(is_show=False),
                           )
                .add_yaxis('Q', Q_lum_data_list, markpoint_opts=opts.MarkPointOpts(
), label_opts=opts.LabelOpts(is_show=False),

                           )
                )


page = Page(layout=Page.SimplePageLayout)
page.add(YKL_temp_line,OPQ_temp_line,YKL_lum_line,OPQ_lum_line)
page.render('YKLOPQ_comparison_line_7.html')