import bs4
import requests
import os
req = requests.get(r"https://www.sohu.com/a/239299040_655858")
req.encoding="utf-8"
bs = bs4.BeautifulSoup(req.text,"html.parser")
obj = bs.find_all("p")
objHtml=[]
objImg=[]
targetPath = "D:\\pics22223\\"
for s in obj:
    objHtml.append(s.find("img"))
    
for tmp in objHtml:
    if(tmp is not None):
        objImg.append(tmp.get("src"))
        print(tmp.get("src"));
for img in objImg:
    if not os.path.exists(targetPath):
        os.mkdir(targetPath);
    with open("D:\\pics22223\\"+os.path.basename(img),'wb') as f:
        f.write(requests.get(img).content)
    print(os.path.basename(img)+"保存成功");