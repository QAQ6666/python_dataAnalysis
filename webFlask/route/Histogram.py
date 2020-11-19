# -*- coding: utf-8 -*-
from pyecharts.charts import Bar
from pyecharts import options as opts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType
from route import pmTop

def histogram():
    list = pmTop.getpmtop()
    arealist = []
    pmlist = []
    for obj in list:
        arealist.append(obj['area'])
        pmlist.append(obj['pm2_5'])

    bar = Bar()
    bar.add_xaxis(arealist)
    bar.add_yaxis("pm指数", pmlist)
    bar.set_global_opts(title_opts=opts.TitleOpts(title="PM TOP25", subtitle="榜单"),
                        yaxis_opts=opts.AxisOpts(name="PM指数"),
                        xaxis_opts=opts.AxisOpts(name="城市Name",offset=5,name_gap=25,
                                                 axislabel_opts=opts.LabelOpts(font_size=12#字的大小
                                                                    ,rotate=-90 #字旋转的角度
                                                                               )))
    # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
    # 也可以传入路径参数，如 bar.render("mycharts.html")
    return bar
