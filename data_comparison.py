import csv
import pandas as pd
import datetime
from pyecharts.charts import Line,Page
from pyecharts import options as opts
file_csv='/var/sensordata/server-sgf/tcpdata506-8008.csv'
A_file="/var/sensordata/D_A-506-BMP180-GY30-TSL2561.csv"
B_file="/var/sensordata/D_B-506-BMP180-GY30.csv"
C_file="/var/sensordata/D_C-506-BMP180-GY30.csv"
S_file="/var/sensordata/D_S-506-BMP180-GY30.csv"
date_list_7=[]
date_list_30=[]
A_data_7_list=[]
A_data_30_list=[]
B_data_7_list=[]
B_data_30_list=[]
C_data_7_list=[]
C_data_30_list=[]
S_data_7_list=[]
S_data_30_list=[]
Y_data_7_list=[]
Y_data_30_list=[]
K_data_7_list=[]
K_data_30_list=[]
L_data_7_list=[]
L_data_30_list=[]
O_data_7_list=[]
O_data_30_list=[]
P_data_7_list=[]
P_data_30_list=[]
Q_data_7_list=[]
Q_data_30_list=[]
A_temp_data_7_list = []
A_lum_data_7_list = []
B_temp_data_7_list = []
B_lum_data_7_list = []
C_temp_data_7_list = []
C_lum_data_7_list = []
S_temp_data_7_list = []
S_lum_data_7_list = []
A_temp_data_30_list = []
A_lum_data_30_list = []
B_temp_data_30_list = []
B_lum_data_30_list = []
C_temp_data_30_list = []
C_lum_data_30_list = []
S_temp_data_30_list = []
S_lum_data_30_list = []
Y_temp_data_7_list=[]
Y_lum_data_7_list = []
K_temp_data_7_list=[]
K_lum_data_7_list = []
L_temp_data_7_list=[]
L_lum_data_7_list = []
O_temp_data_7_list=[]
O_lum_data_7_list = []
P_temp_data_7_list=[]
P_lum_data_7_list = []
Q_temp_data_7_list=[]
Q_lum_data_7_list = []
Y_temp_data_30_list=[]
Y_lum_data_30_list = []
K_temp_data_30_list=[]
K_lum_data_30_list = []
L_temp_data_30_list=[]
L_lum_data_30_list = []
O_temp_data_30_list=[]
O_lum_data_30_list = []
P_temp_data_30_list=[]
P_lum_data_30_list = []
Q_temp_data_30_list=[]
Q_lum_data_30_list=[]

#制作7天和10天时间轴
with open(C_file) as f:
    reader = csv.reader(f)
    dates = [row for row in reader]
the_end_date=dates[-1][0]+' '+dates[-1][1]+':00'
the_end_date=datetime.datetime.strptime(the_end_date,"%Y-%m-%d %H:%M:%S")
the_begin_date_7=str(pd.date_range(end=the_end_date, periods=7)[0])[:10]
the_begin_date_30=str(pd.date_range(end=the_end_date, periods=30)[0])[:10]
the_begin_date_7=datetime.datetime.strptime(the_begin_date_7,"%Y-%m-%d")
the_begin_date_30=datetime.datetime.strptime(the_begin_date_30,"%Y-%m-%d")
time=the_begin_date_30
while(1):
    if(time<=the_end_date and time>=the_begin_date_7):
        date_list_7.append(str(time)[:16])
    if (time <= the_end_date and time >= the_begin_date_30):
        date_list_30.append(str(time)[:16])
    if(time>the_end_date):
        break
    time = time + +datetime.timedelta(minutes=10)


#A数据
with open(A_file) as f:
    reader = csv.reader(f)
    A_rows = [row for row in reader]
del A_rows[:70000]

for row in A_rows:
    time= row[0].replace('/','-')
    time= str(datetime.datetime.strptime(time, "%Y-%m-%d"))[0:10]
    if(time>=str(the_begin_date_7)[0:10]):
        A_data_7_list.append(row)
    if(time>=str(the_begin_date_30)[0:10]):
        A_data_30_list.append(row)
a=0
for i in range(len(date_list_7)):
    if(str(datetime.datetime.strptime(A_data_7_list[a][0].replace('/','-'), "%Y-%m-%d"))[0:10]==date_list_7[i][:10]):
         A_temp_data_7_list.append(float(A_data_7_list[a][3]))
         A_lum_data_7_list.append(float(A_data_7_list[a][5]))
         a=a+1
    else:
        A_temp_data_7_list.append(0)
        A_lum_data_7_list.append(0)
a=0
for i in range(len(date_list_30)):
    if (str(datetime.datetime.strptime(A_data_30_list[a][0].replace('/', '-'), "%Y-%m-%d"))[0:10] == date_list_30[i][:10]):
        A_temp_data_30_list.append(float(A_data_30_list[a][3]))
        A_lum_data_30_list.append(float(A_data_30_list[a][5]))
        a=a+1
    else:
        A_temp_data_30_list.append(0)
        A_lum_data_30_list.append(0)

# B数据
with open(B_file) as f:
    reader = csv.reader(f)
    B_rows = [row for row in reader]
del B_rows[:70000]

for row in B_rows:
    time = row[0].replace('/', '-')
    time = str(datetime.datetime.strptime(time, "%Y-%m-%d"))[0:10]
    if (time >= str(the_begin_date_7)[0:10]):
        B_data_7_list.append(row)
    if (time >= str(the_begin_date_30)[0:10]):
        B_data_30_list.append(row)
a = 0
for i in range(len(date_list_7)):
    if (str(datetime.datetime.strptime(B_data_7_list[a][0].replace('/', '-'), "%Y-%m-%d"))[0:10] == date_list_7[i][:10]):
         B_temp_data_7_list.append(float(B_data_7_list[a][3]))
         B_lum_data_7_list.append(float(B_data_7_list[a][5]))
         a = a + 1
    else:
        B_temp_data_7_list.append(0)
        B_lum_data_7_list.append(0)
a = 0
for i in range(len(date_list_30)-1):
    if (str(datetime.datetime.strptime(B_data_30_list[a][0].replace('/', '-'), "%Y-%m-%d"))[0:10] == date_list_30[i][:10]):
        B_temp_data_30_list.append(float(B_data_30_list[a][3]))
        B_lum_data_30_list.append(float(B_data_30_list[a][5]))
        a = a + 1
    else:
        B_temp_data_30_list.append(0)
        B_lum_data_30_list.append(0)

# C数据
with open(C_file) as f:
    reader = csv.reader(f)
    C_rows = [row for row in reader]
del C_rows[:2000]

for row in C_rows:
    time = row[0].replace('/', '-')
    time = str(datetime.datetime.strptime(time, "%Y-%m-%d"))[0:10]
    if (time >= str(the_begin_date_7)[0:10]):
        C_data_7_list.append(row)
    if (time >= str(the_begin_date_30)[0:10]):
        C_data_30_list.append(row)

a = 0
for i in range(len(date_list_7)):
    if (str(datetime.datetime.strptime(C_data_7_list[a][0].replace('/', '-'), "%Y-%m-%d"))[0:10] == date_list_7[i][:10]):
        C_temp_data_7_list.append(float(C_data_7_list[a][3]))
        C_lum_data_7_list.append(float(C_data_7_list[a][5]))
        a = a + 1
    else:
        C_temp_data_7_list.append(0)
        C_lum_data_7_list.append(0)


a = 0
for i in range(len(date_list_30)):
    if (str(datetime.datetime.strptime(C_data_30_list[a][0].replace('/', '-'), "%Y-%m-%d"))[0:10] == date_list_30[i][:10]):
        C_temp_data_30_list.append(C_data_30_list[a][3])
        C_lum_data_30_list.append(C_data_30_list[a][5])
        a = a + 1
    else:
        C_temp_data_30_list.append(0)
        C_lum_data_30_list.append(0)

# S数据
with open(S_file) as f:
    reader = csv.reader(f)
    S_rows = [row for row in reader]
del S_rows[:2000]

for row in S_rows:
    time = row[0].replace('/', '-')
    time = str(datetime.datetime.strptime(time, "%Y-%m-%d"))[0:10]
    if (time >= str(the_begin_date_7)[0:10]):
        S_data_7_list.append(row)
    if (time >= str(the_begin_date_30)[0:10]):
        S_data_30_list.append(row)

a = 0
for i in range(len(date_list_7)):
    if (str(datetime.datetime.strptime(S_data_7_list[a][0].replace('/', '-'), "%Y-%m-%d"))[0:10] == date_list_7[i][:10]):
        S_temp_data_7_list.append(float(S_data_7_list[a][3]))
        S_lum_data_7_list.append(float(S_data_7_list[a][5]))
        a = a + 1
    else:
        S_temp_data_7_list.append(0)
        S_lum_data_7_list.append(0)


a = 0
for i in range(len(date_list_30)):
    if (str(datetime.datetime.strptime(S_data_30_list[a][0].replace('/', '-'), "%Y-%m-%d"))[0:10] == date_list_30[i][:10]):
        S_temp_data_30_list.append(float(S_data_30_list[a][3]))
        S_lum_data_30_list.append(float(S_data_30_list[a][5]))
        a = a + 1
    else:
        S_temp_data_30_list.append(0)
        S_lum_data_30_list.append(0)

#处理数据
with open(file_csv) as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
    del rows[0:27745]
for row in rows:
    row[0]=row[0].replace("/", "-")
    row[0]=str(datetime.datetime.strptime(row[0], "%Y-%m-%d"))[0:10]
    row[1] =str(datetime.datetime.strptime(row[1], "%H:%M:%S"))[11:19]


#Y
for row in rows:
    if (row[0] >= date_list_7[0][0:10] ):
        if (row[2] == 'Y-Tem-Press-Lig' or row[2] == 'Anano-R3C2Y-Tem-Press-Lig'):
            if(len(Y_data_7_list)==0):
                Y_data_7_list .append(row)
            if(Y_data_7_list[-1][1][3]!=row[1][3]):
                Y_data_7_list.append(row)
    if (row[0] >= date_list_30[0][0:10] ):
        if (row[2] == 'Y-Tem-Press-Lig' or row[2] == 'Anano-R3C2Y-Tem-Press-Lig'):
            if(len(Y_data_30_list)==0):
                Y_data_30_list .append(row)
            if(Y_data_30_list[-1][1][3]!=row[1][3]):
                Y_data_30_list.append(row)

a=0
for i in range(len(date_list_7)):
    if (a <= len(Y_data_7_list) - 1):
        if(date_list_7[i][0:10]==Y_data_7_list[a][0] and date_list_7[i][11:15]==Y_data_7_list[a][1][0:4]):
            Y_temp_data_7_list.append(float(Y_data_7_list[a][4]))
            Y_lum_data_7_list.append(float(Y_data_7_list[a][7]))
            a=a+1
        else:
            Y_temp_data_7_list.append(0)
            Y_lum_data_7_list.append(0)
    else:
        Y_temp_data_7_list.append(0)
        Y_lum_data_7_list.append(0)

a=0
for i in range(len(date_list_30)):
    if (a <= len(Y_data_30_list) - 1):
        if(date_list_30[i][0:10]==Y_data_30_list[a][0] and date_list_30[i][11:15]==Y_data_30_list[a][1][0:4]):
            Y_temp_data_30_list.append(float(Y_data_30_list[a][4]))
            Y_lum_data_30_list.append(float(Y_data_30_list[a][7]))
            a=a+1
        else:
            Y_temp_data_30_list.append(0)
            Y_lum_data_30_list.append(0)
    else:
        Y_temp_data_30_list.append(0)
        Y_lum_data_30_list.append(0)

#K
for row in rows:
    if (row[0] >= date_list_7[0][0:10] ):
        if (row[2] == 'K-Tem-Press-Lig' or row[2] == 'Anano-R1C1K-Tem-Press-Lig'):
            if(len(K_data_7_list)==0):
                K_data_7_list .append(row)
            if(K_data_7_list[-1][1][3]!=row[1][3]):
                K_data_7_list.append(row)
    if (row[0] >= date_list_30[0][0:10] ):
        if (row[2] == 'K-Tem-Press-Lig' or row[2] == 'Anano-R1C1K-Tem-Press-Lig'):
            if(len(K_data_30_list)==0):
                K_data_30_list .append(row)
            if(K_data_30_list[-1][1][3]!=row[1][3]):
                K_data_30_list.append(row)

a=0
for i in range(len(date_list_7)):
    if (a <= len(K_data_7_list) - 1):
        if(date_list_7[i][0:10]==K_data_7_list[a][0] and date_list_7[i][11:15]==K_data_7_list[a][1][0:4]):
            K_temp_data_7_list.append(float(K_data_7_list[a][4]))
            K_lum_data_7_list.append(float(K_data_7_list[a][7]))
            a=a+1
        else:
            K_temp_data_7_list.append(0)
            K_lum_data_7_list.append(0)
    else:
        K_temp_data_7_list.append(0)
        K_lum_data_7_list.append(0)

a=0
for i in range(len(date_list_30)):
    if (a <= len(K_data_30_list) - 1):
        if(date_list_30[i][0:10]==K_data_30_list[a][0] and date_list_30[i][11:15]==K_data_30_list[a][1][0:4]):
            K_temp_data_30_list.append(float(K_data_30_list[a][4]))
            K_lum_data_30_list.append(float(K_data_30_list[a][7]))
            a=a+1
        else:
            K_temp_data_30_list.append(0)
            K_lum_data_30_list.append(0)
    else:
        K_temp_data_30_list.append(0)
        K_lum_data_30_list.append(0)

#L
for row in rows:
    if (row[0] >= date_list_7[0][0:10] ):
        if (row[2] == 'L-Tem-Press-Lig' or row[2] == 'Anano-R2C1L-Tem-Press-Lig'):
            if(len(L_data_7_list)==0):
                L_data_7_list .append(row)
            if(L_data_7_list[-1][1][3]!=row[1][3]):
                L_data_7_list.append(row)
    if (row[0] >= date_list_30[0][0:10] ):
        if (row[2] == 'L-Tem-Press-Lig' or row[2] == 'Anano-R2C1L-Tem-Press-Lig'):
            if(len(L_data_30_list)==0):
                L_data_30_list .append(row)
            if(L_data_30_list[-1][1][3]!=row[1][3]):
                L_data_30_list.append(row)
a=0
for i in range(len(date_list_7)):
    if (a <= len(L_data_7_list) - 1):
        if(date_list_7[i][0:10]==L_data_7_list[a][0] and date_list_7[i][11:15]==L_data_7_list[a][1][0:4]):
            L_temp_data_7_list.append(float(L_data_7_list[a][4]))
            L_lum_data_7_list.append(float(L_data_7_list[a][7]))
            a=a+1
        else:
            L_temp_data_7_list.append(0)
            L_lum_data_7_list.append(0)
    else:
        L_temp_data_7_list.append(0)
        L_lum_data_7_list.append(0)
a=0
for i in range(len(date_list_30)):
    if(a<=len(L_data_30_list)-1):
        if(date_list_30[i][0:10]==L_data_30_list[a][0] and date_list_30[i][11:15]==L_data_30_list[a][1][0:4]):
            L_temp_data_30_list.append(float(L_data_30_list[a][4]))
            L_lum_data_30_list.append(float(L_data_30_list[a][7]))
            a=a+1
        else:
            L_temp_data_30_list.append(0)
            L_lum_data_30_list.append(0)
    else:
        L_temp_data_30_list.append(0)
        L_lum_data_30_list.append(0)

#O
for row in rows:
    if (row[0] >= date_list_7[0][0:10] ):
        if (row[2] == 'O-Tem-Press-Lig' or row[2] == 'Anano-R3C10-Tem-Press-Lig'):
            if(len(O_data_7_list)==0):
                O_data_7_list .append(row)
            if(O_data_7_list[-1][1][3]!=row[1][3]):
                O_data_7_list.append(row)
    if (row[0] >= date_list_30[0][0:10] ):
        if (row[2] == 'O-Tem-Press-Lig' or row[2] == 'Anano-R3C10-Tem-Press-Lig'):
            if(len(O_data_30_list)==0):
                O_data_30_list .append(row)
            if(O_data_30_list[-1][1][3]!=row[1][3]):
                O_data_30_list.append(row)
a=0
for i in range(len(date_list_7)):
    if (a <= len(O_data_7_list) - 1):
        if(date_list_7[i][0:10]==O_data_7_list[a][0] and date_list_7[i][11:15]==O_data_7_list[a][1][0:4]):
            O_temp_data_7_list.append(float(O_data_7_list[a][4]))
            O_lum_data_7_list.append(float(O_data_7_list[a][7]))
            a=a+1
        else:
            O_temp_data_7_list.append(0)
            O_lum_data_7_list.append(0)
    else:
        O_temp_data_7_list.append(0)
        O_lum_data_7_list.append(0)
a=0
for i in range(len(date_list_30)):
    if(a<=len(O_data_30_list)-1):
        if(date_list_30[i][0:10]==O_data_30_list[a][0] and date_list_30[i][11:15]==O_data_30_list[a][1][0:4]):
            O_temp_data_30_list.append(float(O_data_30_list[a][4]))
            O_lum_data_30_list.append(float(O_data_30_list[a][7]))
            a=a+1
        else:
            O_temp_data_30_list.append(0)
            O_lum_data_30_list.append(0)
    else:
        O_temp_data_30_list.append(0)
        O_lum_data_30_list.append(0)

#P
for row in rows:
    if (row[0] >= date_list_7[0][0:10] ):
        if (row[2] == 'P-Tem-Press-Lig' or row[2] == 'Anano-R3C2P-Tem-Press-Lig'):
            if(len(P_data_7_list)==0):
                P_data_7_list .append(row)
            if(P_data_7_list[-1][1][3]!=row[1][3]):
                P_data_7_list.append(row)
    if (row[0] >= date_list_30[0][0:10] ):
        if (row[2] == 'P-Tem-Press-Lig' or row[2] == 'Anano-R3C2P-Tem-Press-Lig'):
            if(len(P_data_30_list)==0):
                P_data_30_list .append(row)
            if(P_data_30_list[-1][1][3]!=row[1][3]):
                P_data_30_list.append(row)
a=0
for i in range(len(date_list_7)):
    if (a <= len(P_data_7_list) - 1):
        if(date_list_7[i][0:10]==P_data_7_list[a][0] and date_list_7[i][11:15]==P_data_7_list[a][1][0:4]):
            P_temp_data_7_list.append(float(P_data_7_list[a][4]))
            P_lum_data_7_list.append(float(P_data_7_list[a][7]))
            a=a+1
        else:
            P_temp_data_7_list.append(0)
            P_lum_data_7_list.append(0)
    else:
        P_temp_data_7_list.append(0)
        P_lum_data_7_list.append(0)
a=0
for i in range(len(date_list_30)):
    if(a<=len(P_data_30_list)-1):
        if(date_list_30[i][0:10]==P_data_30_list[a][0] and date_list_30[i][11:15]==P_data_30_list[a][1][0:4]):
            P_temp_data_30_list.append(float(P_data_30_list[a][4]))
            P_lum_data_30_list.append(float(P_data_30_list[a][7]))
            a=a+1
        else:
            P_temp_data_30_list.append(0)
            P_lum_data_30_list.append(0)
    else:
        P_temp_data_30_list.append(0)
        P_lum_data_30_list.append(0)

#Q
for row in rows:
    if (row[0] >= date_list_7[0][0:10] ):
        if (row[2] == 'Q-Tem-Press-Lig' or row[2] == 'Anano-R3C3Q-Tem-Press-Lig'):
            if(len(Q_data_7_list)==0):
                Q_data_7_list .append(row)
            if(Q_data_7_list[-1][1][3]!=row[1][3]):
                Q_data_7_list.append(row)
    if (row[0] >= date_list_30[0][0:10] ):
        if (row[2] == 'Q-Tem-Press-Lig' or row[2] == 'Anano-R3C3Q-Tem-Press-Lig'):
            if(len(Q_data_30_list)==0):
                Q_data_30_list .append(row)
            if(Q_data_30_list[-1][1][3]!=row[1][3]):
                Q_data_30_list.append(row)
a=0
for i in range(len(date_list_7)):
    if (a <= len(Q_data_7_list) - 1):
        if(date_list_7[i][0:10]==Q_data_7_list[a][0] and date_list_7[i][11:15]==Q_data_7_list[a][1][0:4]):
            Q_temp_data_7_list.append(float(Q_data_7_list[a][4]))
            Q_lum_data_7_list.append(float(Q_data_7_list[a][7]))
            a=a+1
        else:
            Q_temp_data_7_list.append(0)
            Q_lum_data_7_list.append(0)
    else:
        Q_temp_data_7_list.append(0)
        Q_lum_data_7_list.append(0)
a=0
for i in range(len(date_list_30)):
    if(a<=len(Q_data_30_list)-1):
        if(date_list_30[i][0:10]==Q_data_30_list[a][0] and date_list_30[i][11:15]==Q_data_30_list[a][1][0:4]):
            Q_temp_data_30_list.append(float(Q_data_30_list[a][4]))
            Q_lum_data_30_list.append(float(Q_data_30_list[a][7]))
            a=a+1
        else:
            Q_temp_data_30_list.append(0)
            Q_lum_data_30_list.append(0)
    else:
        Q_temp_data_30_list.append(0)
        Q_lum_data_30_list.append(0)


#画出A B C S 7 温度的折线图
ABCS_temp_7_line= (Line(init_opts=opts.InitOpts(width="680px", height="450px"))
                       .set_global_opts(title_opts=opts.TitleOpts(title="温度折线图"),
                                        tooltip_opts=opts.TooltipOpts(trigger="axis"),
                                        toolbox_opts=opts.ToolboxOpts(is_show=False),
                                        yaxis_opts=opts.AxisOpts(
                                            type_="value",
                                            name=' temp(℃)',
                                            axistick_opts=opts.AxisTickOpts(is_show=True),
                                            splitline_opts=opts.SplitLineOpts(is_show=True),
                                            max_=float(max(A_temp_data_7_list))+2,
                                            min_=float(max(A_temp_data_7_list))-15,

                                        ),
                                        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=True,
                                                                 name='date',
                                                                ),

                                        datazoom_opts=[
                                            opts.DataZoomOpts(range_start=0, range_end=100,
                                                               xaxis_index=0, type_="inside"),
                                        ])
                       .add_xaxis(date_list_7)
                       .add_yaxis('A', A_temp_data_7_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('B',B_temp_data_7_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('C', C_temp_data_7_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('S ',S_temp_data_7_list , label_opts=opts.LabelOpts(is_show=False),
                                 )
                       )

#画出YKL 7温度的折线图
YKL_temp_7_line= (Line(init_opts=opts.InitOpts(width="680px", height="450px"))
                       .set_global_opts(title_opts=opts.TitleOpts(title="温度折线图"),
                                        tooltip_opts=opts.TooltipOpts(trigger="axis"),
                                        toolbox_opts=opts.ToolboxOpts(is_show=False),
                                        yaxis_opts=opts.AxisOpts(
                                            type_="value",
                                            name=' temp(℃)',
                                            axistick_opts=opts.AxisTickOpts(is_show=True),
                                            splitline_opts=opts.SplitLineOpts(is_show=True),
                                            max_=float(max(Y_temp_data_7_list))+2,
                                            min_=float(max(Y_temp_data_7_list))-16,

                                        ),
                                        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=True,
                                                                 name='date',
                                                                ),

                                        datazoom_opts=[
                                            opts.DataZoomOpts(range_start=0, range_end=100,
                                                               xaxis_index=0, type_="inside"),
                                        ])
                       .add_xaxis(date_list_7)
                       .add_yaxis('Y', Y_temp_data_7_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('K',K_temp_data_7_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('L', L_temp_data_7_list , label_opts=opts.LabelOpts(is_show=False),
                                  )

                                 )

#画出OPQ 7温度的折线图
OPQ_temp_7_line= (Line(init_opts=opts.InitOpts(width="680px", height="450px"))
                       .set_global_opts(title_opts=opts.TitleOpts(title="温度折线图"),
                                        tooltip_opts=opts.TooltipOpts(trigger="axis"),
                                        toolbox_opts=opts.ToolboxOpts(is_show=False),
                                        yaxis_opts=opts.AxisOpts(
                                            type_="value",
                                            name=' temp(℃)',
                                            axistick_opts=opts.AxisTickOpts(is_show=True),
                                            splitline_opts=opts.SplitLineOpts(is_show=True),
                                            max_=float(max(O_temp_data_7_list))+2,
                                            min_=float(max(O_temp_data_7_list))-15,

                                        ),
                                        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=True,
                                                                 name='date',
                                                                ),

                                        datazoom_opts=[
                                            opts.DataZoomOpts(range_start=0, range_end=100,
                                                               xaxis_index=0, type_="inside"),
                                        ])
                       .add_xaxis(date_list_7)
                       .add_yaxis('O', O_temp_data_7_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('P',P_temp_data_7_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('Q', Q_temp_data_7_list , label_opts=opts.LabelOpts(is_show=False),
                                  )

                                 )


#画出A B C S 7光强的折线图
ABCS_lum_7_line=(Line(init_opts=opts.InitOpts(width="680px", height="450px"))
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
                       .add_xaxis(date_list_7)
                       .add_yaxis('A', A_lum_data_7_list ,markpoint_opts=opts.MarkPointOpts(
        ),label_opts=opts.LabelOpts(is_show=False),
                                 )
                       .add_yaxis('B',B_lum_data_7_list ,        markpoint_opts=opts.MarkPointOpts(
        ), label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('C', C_lum_data_7_list ,        markpoint_opts=opts.MarkPointOpts(
        ), label_opts=opts.LabelOpts(is_show=False),
                                )
                       .add_yaxis('S ',S_lum_data_7_list ,        markpoint_opts=opts.MarkPointOpts(
        ), label_opts=opts.LabelOpts(is_show=False),
                                )
                       )

#画出YKL 7光强的折线图
YKL_lum_7_line=(Line(init_opts=opts.InitOpts(width="680px", height="450px"))
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
                       .add_xaxis(date_list_7)
                       .add_yaxis('Y', Y_lum_data_7_list ,markpoint_opts=opts.MarkPointOpts(
        ),label_opts=opts.LabelOpts(is_show=False),
                                 )
                       .add_yaxis('K',K_lum_data_7_list ,        markpoint_opts=opts.MarkPointOpts(
        ), label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('L', L_lum_data_7_list ,        markpoint_opts=opts.MarkPointOpts(
        ), label_opts=opts.LabelOpts(is_show=False),


                                )
                       )
# 画出OPQ 7光强的折线图
OPQ_lum_7_line = (Line(init_opts=opts.InitOpts(width="680px", height="450px"))
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
                .add_xaxis(date_list_7)
                .add_yaxis('O', O_lum_data_7_list, markpoint_opts=opts.MarkPointOpts(
), label_opts=opts.LabelOpts(is_show=False),
                           )
                .add_yaxis('P', P_lum_data_7_list, markpoint_opts=opts.MarkPointOpts(
), label_opts=opts.LabelOpts(is_show=False),
                           )
                .add_yaxis('Q', Q_lum_data_7_list, markpoint_opts=opts.MarkPointOpts(
), label_opts=opts.LabelOpts(is_show=False),

                           )
                )

page = Page(layout=Page.SimplePageLayout)
page.add(ABCS_temp_7_line,YKL_temp_7_line,OPQ_temp_7_line,ABCS_lum_7_line,YKL_lum_7_line,OPQ_lum_7_line)
page.render('/var/sensordata/html/comparison_line_7.html')

#画出A B C S 30 温度的折线图
ABCS_temp_30_line= (Line(init_opts=opts.InitOpts(width="680px", height="450px"))
                       .set_global_opts(title_opts=opts.TitleOpts(title="温度折线图"),
                                        tooltip_opts=opts.TooltipOpts(trigger="axis"),
                                        toolbox_opts=opts.ToolboxOpts(is_show=False),
                                        yaxis_opts=opts.AxisOpts(
                                            type_="value",
                                            name=' temp(℃)',
                                            axistick_opts=opts.AxisTickOpts(is_show=True),
                                            splitline_opts=opts.SplitLineOpts(is_show=True),
                                            max_=float(max(A_temp_data_30_list))+2,
                                            min_=float(max(A_temp_data_30_list))-15,

                                        ),
                                        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=True,
                                                                 name='date',
                                                                ),

                                        datazoom_opts=[
                                            opts.DataZoomOpts(range_start=0, range_end=100,
                                                               xaxis_index=0, type_="inside"),
                                        ])
                       .add_xaxis(date_list_30)
                       .add_yaxis('A', A_temp_data_30_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('B',B_temp_data_30_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('C', C_temp_data_30_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('S ',S_temp_data_30_list , label_opts=opts.LabelOpts(is_show=False),
                                 )
                       )
#画出A B C S 30 光强的折线图
ABCS_lum_30_line=(Line(init_opts=opts.InitOpts(width="680px", height="450px"))
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
                       .add_xaxis(date_list_30)
                       .add_yaxis('A', A_lum_data_30_list ,markpoint_opts=opts.MarkPointOpts(
        ),label_opts=opts.LabelOpts(is_show=False),
                                 )
                       .add_yaxis('B',B_lum_data_30_list ,        markpoint_opts=opts.MarkPointOpts(
        ), label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('C', C_lum_data_30_list ,        markpoint_opts=opts.MarkPointOpts(
        ), label_opts=opts.LabelOpts(is_show=False),
                                )
                       .add_yaxis('S ',S_lum_data_30_list ,        markpoint_opts=opts.MarkPointOpts(
        ), label_opts=opts.LabelOpts(is_show=False),
                                )
                       )

#画出YKL 30 温度的折线图
YKL_temp_30_line= (Line(init_opts=opts.InitOpts(width="680px", height="450px"))
                       .set_global_opts(title_opts=opts.TitleOpts(title="温度折线图"),
                                        tooltip_opts=opts.TooltipOpts(trigger="axis"),
                                        toolbox_opts=opts.ToolboxOpts(is_show=False),
                                        yaxis_opts=opts.AxisOpts(
                                            type_="value",
                                            name=' temp(℃)',
                                            axistick_opts=opts.AxisTickOpts(is_show=True),
                                            splitline_opts=opts.SplitLineOpts(is_show=True),
                                            max_=float(max(Y_temp_data_30_list))+2,
                                            min_=float(max(Y_temp_data_30_list))-15,

                                        ),
                                        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=True,
                                                                 name='date',
                                                                ),

                                        datazoom_opts=[
                                            opts.DataZoomOpts(range_start=0, range_end=100,
                                                               xaxis_index=0, type_="inside"),
                                        ])
                       .add_xaxis(date_list_30)
                       .add_yaxis('Y', Y_temp_data_30_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('K',K_temp_data_30_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('L', L_temp_data_30_list , label_opts=opts.LabelOpts(is_show=False),
                                  )

                                 )

#画出OPQ 30 温度的折线图
OPQ_temp_30_line= (Line(init_opts=opts.InitOpts(width="680px", height="450px"))
                       .set_global_opts(title_opts=opts.TitleOpts(title="温度折线图"),
                                        tooltip_opts=opts.TooltipOpts(trigger="axis"),
                                        toolbox_opts=opts.ToolboxOpts(is_show=False),
                                        yaxis_opts=opts.AxisOpts(
                                            type_="value",
                                            name=' temp(℃)',
                                            axistick_opts=opts.AxisTickOpts(is_show=True),
                                            splitline_opts=opts.SplitLineOpts(is_show=True),
                                            max_=float(max(O_temp_data_30_list))+1,
                                            min_=float(max(O_temp_data_30_list))-15,
                                        ),
                                        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=True,
                                                                 name='date',
                                                                ),

                                        datazoom_opts=[
                                            opts.DataZoomOpts(range_start=0, range_end=100,
                                                               xaxis_index=0, type_="inside"),
                                        ])
                       .add_xaxis(date_list_30)
                       .add_yaxis('O', O_temp_data_30_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('P',P_temp_data_30_list , label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('Q', Q_temp_data_30_list , label_opts=opts.LabelOpts(is_show=False),
                                  )

                                 )

#画出YKL 30光强的折线图
YKL_lum_30_line=(Line(init_opts=opts.InitOpts(width="680px", height="450px"))
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
                       .add_xaxis(date_list_30)
                       .add_yaxis('Y', Y_lum_data_30_list ,markpoint_opts=opts.MarkPointOpts(
        ),label_opts=opts.LabelOpts(is_show=False),
                                 )
                       .add_yaxis('K',K_lum_data_30_list ,        markpoint_opts=opts.MarkPointOpts(
        ), label_opts=opts.LabelOpts(is_show=False),
                                  )
                       .add_yaxis('L', L_lum_data_30_list ,        markpoint_opts=opts.MarkPointOpts(
        ), label_opts=opts.LabelOpts(is_show=False),


                                )
                       )
# 画出OPQ 30光强的折线图
OPQ_lum_30_line = (Line(init_opts=opts.InitOpts(width="680px", height="450px"))
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
                .add_xaxis(date_list_30)
                .add_yaxis('O', O_lum_data_30_list, markpoint_opts=opts.MarkPointOpts(
), label_opts=opts.LabelOpts(is_show=False),
                           )
                .add_yaxis('P', P_lum_data_30_list, markpoint_opts=opts.MarkPointOpts(
), label_opts=opts.LabelOpts(is_show=False),
                           )
                .add_yaxis('Q', Q_lum_data_30_list, markpoint_opts=opts.MarkPointOpts(
), label_opts=opts.LabelOpts(is_show=False),

                           )
                )

page = Page(layout=Page.SimplePageLayout)
page.add(ABCS_temp_30_line,YKL_temp_30_line,OPQ_temp_30_line,ABCS_lum_30_line,YKL_lum_30_line,OPQ_lum_30_line)
page.render('/var/sensordata/html/comparison_line_30.html')