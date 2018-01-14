import urllib.request
import sys
content=urllib.request.urlopen('https://www.crifan.com/unicodeencodeerror_gbk_codec_can_not_encode_character_in_position_illegal_multibyte_sequence/').read()
typeEncode = sys.getfilesystemencoding()
content = content.decode("utf-8").encode(typeEncode)
#soup=BeautifulSoup(html,”lxml”)
#print soup.prettify()
fp=open("F:\Test.html",'w')
fp.write(content)
fp.close()

