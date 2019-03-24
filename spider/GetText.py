# -*- coding；UTF-8 -*-
from bs4 import BeautifulSoup
import requests

if __name__=='__main__':
    target='https://www.biqukan.com/1_1094/5403177.html'
    req=requests.get(url=target)
    html=req.text
    bf=BeautifulSoup(html,'html.parser')
    texts=bf.find_all('div',class_='showtxt')
    print(str(texts).replace('</br>','\n\n').replace('<br/>','\n'))
    #print(texts[0])