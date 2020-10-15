import csv
from pyecharts.charts import Line
from pyecharts import options as opts
def get_list_time_and_db_data(file_csv):
    with open(file_csv) as f:
        reader=csv.reader(f)
        rows=[row for row in reader]
        list_data=[]
        list_time=[]
        list_db_data=[]
        for row in rows:
            list_time.append(row[0]+'-'+row[1])
            list_db_data.append(row[5])
        number=list_time.index('2020-09-07-00:00')
        del list_time[0:number]
        del list_db_data[0:number]
        number=list_time.index('2020-09-11-04:10')
        del list_time[number:]
        del list_db_data[number:]
        list_data.append(list_time)
        list_data.append(list_db_data)
        return list_data


def get_list_tcp(file_csv):
    with open(file_csv) as f:
        reader=csv.reader(f)
        rows=[row for row in reader]
        list_tcp_data01=[]
        list_tcp_data02 = []
        list_tcp_data= []
        del rows[0:rows.index(['2020-09-07', '00:00:09', 'L-Tem-Press-Lig', '', '30.00', '', '1003.71', '0'])]
        for row in rows:
            if(row[2]=='Y-Tem-Press-Lig'):
                row[1]=row[1][0:5]
                list_tcp_data01.append(row)
        list_tcp_data02.append(list_tcp_data01[0])
        for i in range(len(list_tcp_data01)):
            if(list_tcp_data01[i][1][3]!=list_tcp_data02[len(list_tcp_data02)-1][1][3]):
                 list_tcp_data02.append(list_tcp_data01[i])
        for i in range(len(list_tcp_data02)):
            list_tcp_data.append(list_tcp_data02[i][7])
        return list_tcp_data

def line_data_comparison():
    line_data_comparison= (Line(init_opts=opts.InitOpts(width="680px", height="450px"))
                       .set_global_opts(title_opts=opts.TitleOpts(title="光强分析"),
                                        tooltip_opts=opts.TooltipOpts(trigger="axis"),
                                        toolbox_opts=opts.ToolboxOpts(is_show=False),
                                        yaxis_opts=opts.AxisOpts(
                                            type_="value",
                                            name='Light intensity',
                                            axistick_opts=opts.AxisTickOpts(is_show=True),
                                            splitline_opts=opts.SplitLineOpts(is_show=True),
                                        ),
                                        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,
                                                                 name='Time'),
                                        datazoom_opts=[
                                            opts.DataZoomOpts(range_start=0, range_end=100),
                                            opts.DataZoomOpts(type_="inside", range_start=0, range_end=100),
                                        ],
                                        )
                       .add_xaxis(get_list_time_and_db_data('D_B-506-BMP180-GY30.csv')[0])
                       .add_yaxis('D_B',get_list_time_and_db_data('D_B-506-BMP180-GY30.csv')[1] , label_opts=opts.LabelOpts(is_show=False),
                                  markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]))
                        .add_yaxis(' Tcp', get_list_tcp('tcpdata506-8008.csv') , label_opts=opts.LabelOpts(is_show=False),
                                      markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]))
                       .render("line_data_comparison.html")
                       )


if __name__ == '__main__':
    get_list_time_and_db_data('D_B-506-BMP180-GY30.csv')
    get_list_tcp('tcpdata506-8008.csv')
    line_data_comparison()
