#!/usr/bin/python3
import requests
import os
url = 'https://www.right.com.cn/forum/home.php?mod=spacecp&ac=usergroup'
cookie =os.environ.get("RIGHT_SIGN", "")
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
    'referer': 'http://www.right.com.cn/forum/home.php?mod=spacecp&ac=plugin&id=qqconnect:spacecp',
    'host': 'www.right.com.cn'
}
def main():
    r = requests.get(url, headers=headers)
    if r.text.find('用户组') >= 0:
        print('今日签到成功！')

if __name__ == '__main__':
    main()
