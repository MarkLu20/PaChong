#coding=utf-8
import urllib
from  urllib import  request
import re

def getHtml(url):
    page = request.urlopen(url)
    html = page.read()
    html=html.decode()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        request.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1


html = getHtml("http://tieba.baidu.com/p/2460150866")

print(getImg(html))