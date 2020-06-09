import requests
from bs4 import BeautifulSoup
import pandas


l=[]

r=requests.get("https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY")
c=r.content
soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div", {"class":"_3liAhj"})
for item in all:
    d={}
    d["price"]=item.find("div",{"class":"_1vC4OE"}).text
    try:
      d["Name"]=item.find("a",{"class":"_2cLu-l"}).text
    except:
        d["Name"]="None"

    l.append(d)
df=pandas.DataFrame(l)
df.to_csv("outputiphone1.excel")


