#-*- coding=UTF-8 -*-
import urllib
import urllib.request
import re
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
page = 1
#i = str(page)
url = "https://www.qiushibaike.com/"

try:
    user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    headers = {"User-Agent":user_agent}
    request = urllib.request.Request(url,headers=headers)
#    request.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
#    print(content)
    pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class'+'="content".*?title="(.*?)">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
#    pattern = re.compile('<span>.*?</span>',re.S)
    items = pattern.findall(content)
    for item in items:
        print(item)
except urllib.request.URLError as e:
    print("error")
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)
