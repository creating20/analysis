# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import jieba
import jieba.analyse
import codecs
import os
import wordcloud
from PIL import Image
import matplotlib.pyplot as plt
pd.set_option('max_colwidth',500)
path=os.getcwd()+'/chengxuyuan58.csv'
f=open(path,encoding='UTF-8')
data=pd.read_csv(f, header=0,encoding='utf-8',dtype=str).astype(str)
segments = []
stopwords = [line.strip() for line in codecs.open('stoped.txt', 'r', 'utf-8').readlines()]
for index, row in data.iterrows():
    content = row[4]
    words = jieba.cut(content)
    splitedStr = ''
    for word in words:
        #停用词判断，如果当前的关键词不在停用词库中才进行记录
        if word not in stopwords:
            # 记录全局分词
            segments.append({'word':word, 'count':1})
            splitedStr += word + ' '
            
            
dfSg = pd.DataFrame(segments)

# 词频统计
dfWord = dfSg.groupby('word')['count'].sum()
#导出csv
dfWord.to_csv('keywords.csv',encoding='utf-8')

#制作云词图

mask = np.array(Image.open('wordcloud.jpg')) # 定义词频背景
wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/simhei.ttf', # 设置字体格式
    
    mask=mask, # 设置背景图
    max_words=50, # 最多显示词数
    max_font_size=1000, # 字体最大值
    background_color="white",
    
)

wc.generate_from_frequencies(dfWord) # 从字典生成词云
#image_colors = wordcloud.ImageColorGenerator(mask) # 从背景图建立颜色方案
wc.recolor(color_func=wordcloud.get_single_color_func('blue')) # 将词云颜色设置为背景图方案
plt.figure(figsize=(8,8))
plt.imshow(wc) # 显示词云
plt.axis('off') # 关闭坐标轴
plt.show() # 显示图像




