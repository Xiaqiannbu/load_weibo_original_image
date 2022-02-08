import requests
import json

def loadImgInfo(uid,cookie,sinceid):
    referer='https://weibo.com/'+uid+'?tabtype=album'
    url='https://weibo.com/ajax/profile/getImageWall?uid='+uid+'&sinceid='+sinceid
    headers={
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': cookie,
                # 'SINAGLOBAL=7894581607788.815.1629189676214; XSRF-TOKEN=ay1cbLKwIOjHA2k1UZFupGJ_; _s_tentry=-; Apache='
                #   '5179581557747.079.1629623824989; ULV=1629623825000:4:4:1:5179581557747.079.1629623824989:1629529942766;'
                #   ' YF-V-WEIBO-G0=b09171a17b2b5a470c42e2f713edace0; UM_distinctid=17ce52c13645f0-00db4686876fb5-b7a183d-'
                #   '1fa400-17ce52c13657c6; TC-V-WEIBO-G0=b09171a17b2b5a470c42e2f713edace0; login_sid_t=581ce870605449c129'
                #   'b5a7d1b4ed4baa; cross_origin_proto=SSL; SSOLoginState=1642332114; UOR=,,www.baidu.com; WBPSESS=pF0-l'
                #   'GcW8F0JJ-ylYhC6vxWBhjqgpI9sPNoX_6G5WPpTj7srdlLlHZNtAqsze53oKJyMIwcy4-PnGmXiwxv_MI8xQ1exxS6vLPP6_WZcjfQ'
                #   'rFPDhTodzGP-N74ZMFpJ9m7bigxl_GdWQgTBnKTYn2g==; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWbHhaSNZ26goQUoJ3'
                #   'r3G9k5JpX5KMhUgL.FozcehzXehe7e022dJLoIEBLxK-LBKBLBKMLxKqL1KnL12-LxKqL1-BL12-LxKnLBoBLB.Bt; ALF=1675435373;'
                #   ' SCF=AvsyQNblGg6Qy2qBnqXnj-Ei-H4s_FOpDpWqZkBtVuW6ckdwSI9E7hemd5Ee2RQU04R6NsIO4DFsdnB9y_pEpZM.; SUB='
                #   '_2A25M_5m-DeRhGeRI61AV8C3MyD2IHXVvjIx2rDV8PUNbmtAKLUankW9NUv8tZUnYlMlyNFPTftIlIztK0-F7cGm0',
        'referer': referer,
        'sec-ch-ua': '"\\Not\"A;Brand";v="99", "Chromium";v="84", "Google Chrome";v="84"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent':'00-1c139e096020309ee08515b68b212990-a3301d11f8d55b85-00',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.30 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'ay1cbLKwIOjHA2k1UZFupGJ_'
    }
    params={
        'uid': uid,
        'sinceid': '0',
        'has_album': 'true'
    }
    res=requests.get(url=url,headers=headers,params=params)
    # print(res)
    res.encoding='utf-8'
    # print('Response:\n',res.text)
    return res.text

def get_district(text, pidList=[]):
    dict=json.loads(text)
    infoList=dict["data"]["list"]
    for info in infoList:
        pid=info['pid']
        pidList.append(pid)
        print(len(pidList),':',pid)
    since_id=dict["data"]['since_id']
    return pidList,since_id

def load_userName(uid, cookie):
    url = 'https://weibo.com/ajax/profile/info?uid=' + uid
    referer='https://weibo.com/u/'+uid
    # print(url)
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': cookie,
        'referer': referer,
        'sec-ch-ua': '"\\Not\"A;Brand";v="99", "Chromium";v="84", "Google Chrome";v="84"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-1c139e096020309ee08515b68b212990-a3301d11f8d55b85-00',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.30 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'ay1cbLKwIOjHA2k1UZFupGJ_'
    }
    res = requests.get(url=url, headers=headers)
    # print(res)
    res.encoding = 'utf-8'
    # print('Response:\n',res.text)
    dict=json.loads(res.text)
    name=dict['data']['user']['screen_name']
    return name