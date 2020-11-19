import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie

data1 = pd.read_csv(open(r'..\resources\qiushi_info.csv',encoding='utf-8'))
data2 = pd.read_csv(open(r'..\resources\user_info.csv',encoding='utf-8'))

def xius():
    data1 = globals()['data1']
    data2 = globals()['data2']
    data1['age'].replace('不详',0,inplace=True)
    data1['age'] = data1['age'].astype('int64')
    data1['age'].replace(0,int(data1[data1['age']!=0]['age'].mean()),inplace=True)

    data2.isnull().sum()
    data2.dropna(inplace=True)
    data2['fans'] = data2['fans'].astype('int64')
    data2['topic'] = data2['topic'].astype('int64')
    data2['qiushi'] = data2['qiushi'].astype('int64')
    data2['comment_1'] = data2['comment_1'].astype('int64')
    data2['favour'] = data2['favour'].astype('int64')
    data2['handpick'] = data2['handpick'].astype('int64')
    #%%

    data2['province'] = data2['home'].str.split('· ').str[0]
    #%%

    data2['qiushi_age'] = data2['qiushi_age'].str.strip('天')
    data2['qiushi_age'] = data2['qiushi_age'].astype('int64')

    data1 = data1.dropna()
    data = pd.merge(data1,data2,on='user_url')
    data = data.drop_duplicates(['id'])
    sex_count = data['sex'].value_counts()

    attr = list(sex_count.index)
    v = list(sex_count)
    pie = Pie(init_opts=opts.InitOpts())
    pie.add('', [list(z) for z in zip(attr, v)])
    pie.set_colors([ "pink", "orange"])
    pie.set_global_opts(title_opts=opts.TitleOpts(title="用户男女分布"))
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    #pie.render("Pyecharts嵌套饼图.html")
    return pie
#xius()
def issingle():
    data1 = globals()['data1']
    data2 = globals()['data2']

    data1 = data1.dropna()
    data2 = pd.read_csv(open(r'..\resources\user_info.csv', encoding='utf-8'))
    data = pd.merge(data1,data2,on='user_url')

    data['martial_status'].replace('不详','secret',inplace=True)

    marry_count = data['martial_status'].value_counts()


    attr = list(marry_count.index)
    v = list(marry_count)
    pie = Pie(init_opts=opts.InitOpts())
    pie.add('', [list(z) for z in zip(attr, v)])
    pie.set_colors(["red", "pink", "orange", "purple"])
    pie.set_global_opts(title_opts=opts.TitleOpts(title="用户婚姻状况"))
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    return pie



