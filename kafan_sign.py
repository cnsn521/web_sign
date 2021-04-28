#!/usr/bin/python3
import requests
import os
url = 'https://bbs.kafan.cn/'
cookie = os.environ.get("KAFAN_SIGN", "")
headers = {
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Upgrade-Insecure-Reques': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://bbs.kafan.cn/',
    'Cookie': cookie,
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache'
}
def main():
    r = requests.get(url, headers=headers)
    # print(r.content)
    content = r.content
    m = r.text.find('discuz_uid')
    if r.status_code == 200 and r.text[m+14:m+16] != '0':
        # print(r.content)
        n = content.find(('formhash=').encode())
    #   print('cookie 正确，获取formhash！')
    else:
    #   print('cookie错误，登陆失败！')
      exit()
    # print(n)
    # print(r.text)

    formhash = content[n+9:n+17].decode()
    print(formhash)
    url1 = 'https://bbs.kafan.cn/plugin.php?id=dsu_amupper&ppersubmit=true&formhash={formhash1}&infloat=yes&handlekey=dsu_amupper&inajax=1&ajaxtarget=fwin_content_dsu_amupper'.format(formhash1=formhash)
    # print(url1)
    p = requests.get(url1, headers=headers)
    # print(p.text)
    # print(p.text.find('您已签到完毕，今日已无需再次签到！'))
    if p.status_code == 200 and p.text.find("succeedhandle") > 0:
        print('签到成功！')
    elif p.status_code == 200 and p.text.find("您已签到完毕，今日已无需再次签到！") > 0:
        print("您已签到完毕，今日已无需再次签到！")
    else:
        print("kafan_sign error!")

if __name__ == '__main__':
    main()
