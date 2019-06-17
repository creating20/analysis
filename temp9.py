# -*- coding: utf-8 -*-
"""
Created on Sun May 19 23:27:43 2019

@author: 格格巫
"""

import requests
from bs4 import BeautifulSoup
import re
#'https://sz.58.com/tech/'

def url_analysis(u,s,h,n):
    '''
        用于分析网页，最后得到一个含有二级网址的标签列表
        u：起始网址
        s：二级网址包含的特定字段
        n：页码
        h:头部信息
    '''
    m=[]
    for i in range(1,n+1):
        r=requests.get(url=u+str(i)+'/',allow_redirects=False,headers=h)
        soup=BeautifulSoup(r.text,'lxml')
        r2=soup.find_all('a',href=re.compile(s))

     
        for j in r2:
            r3=j.attrs['href']
            m.append(r3)
    
    return(m)
    
def content(u,h):
    '''
    爬取标签信息
    u：二级网址
    h：头部信息
    '''
    r=requests.get(url=u,allow_redirects=False,headers=h)
    soup=BeautifulSoup(r.text,'lxml')
    t=soup.find('span',class_='pos_title')
    name=soup.find('span',class_='pos_name')
    number=soup.find('span',class_="item_condition pad_left_none")
    stu=soup.find('span',class_="item_condition")
    exprience=soup.find('span',class_="item_condition border_right_None")
    discribe=soup.find('div',class_="posDes")
    m=[t,',',name,',',number,',',stu,',',exprience,',',discribe,',','\n']
    if m[0]!=None:
        return[m[0].text,',',m[2].text,',',m[4].text,',',m[6].text,',',m[8].text,',',m[10].text,',','\n']
    else:
        return[None, ',', None, ',', None, ',', None, ',', None, ',', None, ',','\n']
    
    
if __name__=='__main__':
    web_u='https://sz.58.com/chengxuyuan/pn'
    web_s='https://sz.58.com/tech/'
    n=1
    
    h = {"User-Agent" : "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    
    f=open(r'C:\Users\格格巫\Desktop\txt1.csv','w+',encoding='utf-8')
    f.seek(0)
    f.write('title,name,number,stu,exprience,discribe\n')
    for i in url_analysis(web_u,web_s,h,n):
        data=content(i,h)
        if data[0]!=None:
            f.writelines(data)
            print(data)
        else:
            continue
    f.close()
    
    print('successful')
        
    