#!/usr/bin/python3
import requests
import re
import os
pattern = re.compile(r'\d+?\s的每日登录奖励\s\d+\s铜币')
pattern1 = re.compile(r"redeem\?once=(.*?)'")
url = 'https://www.v2ex.com/mission/daily'
cookie = os.environ.get("V2EX_SIGN", "")
headers = {
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Upgrade-Insecure-Reques': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cookie': cookie,
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'referer': 'https://www.v2ex.com/mission/daily'
}
def main():
    r = requests.get(url, headers=headers)
    #print(r.text)
    if r.status_code == 302:
        print('cookies 错误,登陆失败！')
        exit()
    if r.status_code == 200:
        if r.text.find('每日登录奖励已领取') > 0:
            print('今天已经签到过了！')
            url1 = 'https://www.v2ex.com/balance'
            r1 = requests.get(url1, headers=headers)
            #print(r1.text)
            print(pattern.search(r1.text).group())

        else:
            print('开始签到!')
            once_daily = pattern1.search(r.text).group()
            print(once_daily)
            url2 = 'https://www.v2ex.com/mission/daily/'+once_daily[0:len(once_daily)-1]
            print(url2)
            r2 = requests.get(url2,headers=headers)
            if r2.status_code == 302:
                r = requests.get(url, headers=headers)
                if r.text.find('每日登录奖励已领取') > 0:
                    print('今日签到已完成')
            url1 = 'https://www.v2ex.com/balance'
            r1 = requests.get(url1, headers=headers)
            #print(r1.text)
            print(pattern.search(r1.text).group())
if __name__ == '__main__':
    main()
