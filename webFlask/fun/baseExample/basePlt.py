import matplotlib.pyplot as plt
import tushare as ts

plt.rcParams['font.sans-serif']=['KaiTi']
plt.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(5,4))
x=['A','B','C','D','E','F','G']
y=[1,4,7,3,2,5,6]
plt.plot(x,y,label=u'折线',marker='o')
#plt.legend()

hs=ts.get_hist_data('hs300')
#hs.info()
hs.head()
#hs['close'].plot()
hs.sort_index(inplace=True)
hs['price_change'].plot().axhline(y=0,color='red')