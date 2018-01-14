#import requests
import io
import sys
#import chardet
from urllib import request
import os
# type=sys.getfilesystemencoding()
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
#sys.setdefaultencoding('utf-8')
response=request.urlopen('https://www.crifan.com/unicodeencodeerror_gbk_codec_can_not_encode_character_in_position_illegal_multibyte_sequence/')
html=response.read()
typeEncode = sys.getfilesystemencoding()
html = html.decode('gbk','ignore').encode('GBK','ignore')
#print(html)


#=html.decode().encode("utf-8")
html=html.decode('gbk','ignore')

#html=object(html)
#print(html)
# if not os.path.isdir("F:\Test.txt"):
#     os.makedev("F:\test.txt")
fp=open("F:\Test.html",'w')
# for content in range(len(html)):
fp.write(html)
#fp.close()