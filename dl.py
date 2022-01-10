import requests
from bs4 import BeautifulSoup
import re
import os

# url = "https://sgzzlb.lingxigames.com/m"
# resp = requests.get(url)
# page = BeautifulSoup(resp.text,'lxml')
# dl_link = page.find('a',{
#     "class":"btn-an",
#     "title":"安卓下载"
# })['href']
# print(dl_link)
# with open("dl.html", "w", encoding="utf8") as p:
#     p.write(page.prettify())

url = "https://cdn-cn.lingxigames.com/prism-sgzzlb/1.0.0/test/static/js/fabm.620a04ba.js"
headers = {
    "Referer": "https://sgzzlb.lingxigames.com/",
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '1', 
    'sec-ch-ua-platform': '"Android"',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36 Edg/97.0.1072.55'
}
resp = requests.get(url,headers=headers)
dl_link = re.search(r'Android"==i\.platformName&&g\(\)\("\.bottom_dl,\.download,\.btn-download"\)\.attr\("href","(?P<link>.*?)"\)',resp.text).group("link")

# dl_link = re.search("link:\"(?P<link>https://.*?)\"",resp.text).group('link')

file_name = re.search(r"(?P<u>.*/)(?P<filename>.*)", dl_link).group("filename")+".apk"
print(file_name)
if os.path.exists(file_name):
    pass
else:
    with open (file_name, "wb") as f:
        f.write(requests.get(dl_link).content)
