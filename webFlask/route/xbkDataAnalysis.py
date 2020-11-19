# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
import matplotlib.pyplot as plt
import base64
from io import BytesIO

starbucks = pd.read_csv(open('../resources/directory.csv', encoding='utf-8'))

def xbk():

    starbucks.head()
    print(starbucks.shape)
    # 对分布国家统计
    cc = len(starbucks['Country'].unique())
    # 对分布城市统计
    ccc = len(starbucks['City'].unique())
    # 统计成一个列表
    country_count = starbucks['Country'].value_counts()[0:10]
    numcout = []
    for s in country_count:
        numcout.append(s)

    # 获取国家前十列表
    labels = list(country_count.index)

    bar = Bar()
    bar.add_xaxis(labels)
    bar.add_yaxis("数量统计", numcout)
    bar.set_global_opts(title_opts=opts.TitleOpts(title="星巴克店铺分布:国家 Top 10"),
                        yaxis_opts=opts.AxisOpts(name="Count",splitline_opts=opts.SplitLineOpts(is_show=True  # 是否展示Y轴分割线
                                                          , linestyle_opts=opts.LineStyleOpts(width=1  ##设置宽度
                                                                                              , opacity=0.5  # 设置透明度
                                                                                              , type_='dotted'
                                                                                              # 'solid', 'dashed', 'dotted'
                                                                                              , color='grey')
                                                          )  # y轴分割线显示的相关设置,X轴和y轴都有

                        , axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(width=3  ##设置宽度
                                                                                            # ,opacity=0 #设置透明度
                                                                                            , type_='dashed'
                                                                                            # 'solid', 'dashed', 'dotted'
                                                                                            , color='red')
                                                          )),
                        xaxis_opts=opts.AxisOpts(name="Country", offset=5, name_gap=25,
                                                 axislabel_opts=opts.LabelOpts(font_size=14))
                        )

    #plt.style.use('ggplot')
    #plt.xlabel('Country')
    #plt.ylabel('Count')
    #plt.title('Country Top 10')
    #plt.bar(range(len(labels)), country_count)
    #plt.xticks(range(len(labels)), labels, fontsize=14)
    #plt.plot()
    #plt.show()
    return bar
#xbk()
def xbkCN():
    cn_startbucks = starbucks[starbucks['Country'] == 'CN']
    citycount = cn_startbucks['City'].value_counts()[0:10]
    #设置图表样式!!
    plt.style.use('ggplot')
    plt.rcParams['font.sans-serif'] = ['simhei']
    plt.rcParams['axes.unicode_minus'] = False
    labels = list(citycount.index)
    plt.xlabel('City')
    plt.ylabel('Count')
    plt.title('星巴克各个城市分布')
    plt.barh(range(len(labels)),citycount)
    plt.yticks(range(len(labels)),labels,fontsize = 12)
    plt.plot()
    #plt.show()
    # figure 保存为二进制文件
    buffer = BytesIO()
    plt.savefig(buffer)
    plot_data = buffer.getvalue()
    # 将matplotlib图片转换为HTML
    imb = base64.b64encode(plot_data)  # 对plot_data进行编码
    ims = imb.decode()
    imd = "data:image/png;base64," + ims
    return imd
#xbkCN()