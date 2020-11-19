# -*- coding: utf-8 -*-
import requests
import pymongo
from multiprocessing.dummy import Pool as mp
import datetime
db = pymongo.MongoClient()['ceis_nlp']['xiaohongshu']

def get_list(url, page):
    '''
    获取列表页
    '''
    return requests.get(url, headers=head).json()

def save_mongo(item):
    '''
    :param item:需要保存的item
    :return: 保存数据
    '''
    try:
        res = db.save(item)
        print(res)
    except:
        print('重复!')
def get_content(info):
    '''
    :param info:列表页的单条数据
    :return: 加入content后的item
    '''

    info_url = 'https://www.xiaohongshu.com/wx_mp_api/sns/v1/note/{}/single_feed?sid=session.1567474343950544022616'.format(info['id'])
    content_data = requests.get(info_url, headers=head).json()
    info['desc'] = repr(content_data['data'][0]['note_list'][0]['desc'])
    info['time'] = datetime.datetime.fromtimestamp(content_data['data'][0]['note_list'][0]['time'])
    info["_id"] = info["id"]
    save_mongo(info)

def read_data(listpage_json):
    '''
    :param listpage_json:列表页的json数据
    :return: 单条详情数据
    '''
    info_data = listpage_json['data']['notes']
    for info in info_data:
        get_content(info)


def main(url, page):
    s = get_list(url, page)
    print(s)
    read_data(s)

if __name__ == '__main__':
    authorization = '19bc4862-d820-481e-b83d-******'
    head = {"accept": "*/*",
            "content-type": "application/json",
            "device-fingerprint": "WC39ZUyXRgdFrJLIl36pz6dYNcrGscYZZWqJlPTC2v9Zkrt3jCwWKSyDu9wYQhprJgZD8KTs1jiM0/jeT0GYQI+Xx06PQ2kgctL/WmrP2Tauiuo9Z2Nzm4Q==1487577677129",
            "authorization": authorization,
            "referer": "https://servicewechat.com/wxffc08ac7df482a27/270/page-frame.html",
            "accept-language": "zh-cn",
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.5(0x17000523) NetType/WIFI Language/zh_CN",
            "accept-encoding": "br, gzip, deflate"
            }

    pools = mp(16)
    keyword = '国庆旅游'
    # 1:按热度排序 2:按时间排序 3:综合排序
    sort = {"1": "popularity_descending", "2": "time_descending", "3": "general"}
    for page in range(25, 51):
        url = 'https://www.xiaohongshu.com/wx_mp_api/sns/v1/search/notes?keyword={}&sort={}&page={}&per_page=30&sid=session.1567474343950544022616'.format(keyword, sort["1"], page)
        pools.apply_async(main, args=(url, page,))
        #print(pools)
        main(url, page)

    #pools.close()
    #pools.join()

