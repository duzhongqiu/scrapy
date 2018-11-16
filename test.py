#!/usr/bin/python3.6
#-*-coding:utf-8-*-
#!@time:2018/11/9 15:27
#!@Auther:duzhongqiu
#!@File:test.py
import requests
from bs4 import BeautifulSoup


url = 'http://www.cssmoban.com/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36'}

response = requests.get(url,headers=headers)
response.encoding = 'utf-8'
souptext = response.text
souplist = BeautifulSoup(souptext,'lxml')

allclassify = souplist.find_all('p',class_='pbutton sort clearfix')
oneclassifylist = BeautifulSoup(str(allclassify),'lxml')
oneclassify = oneclassifylist.find_all('a')
for resp in oneclassify:
    classifyurl = resp.get('href')
    classifyname = resp.get('title')
    print(classifyurl)


'''
/tags.asp?n=%E4%BC%81%E4%B8%9A 企业网站模板
/tags.asp?n=%E5%95%86%E5%8A%A1 商务网站模板
/tags.asp?n=%E5%8D%9A%E5%AE%A2 博客网站模板
/tags.asp?n=html5              HTML5网站模板
/tags.asp?n=css3               css3网站模板
/tags.asp?n=%E6%95%B4%E7%AB%99 整站网站模板
/tags.asp?n=%E7%A7%91%E6%8A%80 科技网站模板
/tags.asp?n=%E7%94%B5%E8%84%91 电脑网站模板
/tags.asp?n=%E4%B8%BB%E6%9C%BA&n=%E5%9F%9F%E5%90%8D 域名主机网站模板
/tags.asp?n=%E6%91%84%E5%BD%B1 摄影网站模板
/tags.asp?n=%E7%9B%B8%E5%86%8C 相册网站模板
/tags.asp?n=%E5%A9%9A%E7%BA%B1 婚嫁网站模板
/tags.asp?n=%E5%95%86%E5%9F%8E 商城网站模板
/tags.asp?n=%E9%A4%90%E9%A5%AE&n=%E9%A4%90%E5%8E%85&n=%E8%A5%BF%E9%A4%90&n=%E7%BE%8E%E9%A3%9F&n=%E9%A3%9F%E5%93%81 餐饮网站模板
/tags.asp?n=%E9%85%92%E5%BA%97 酒店网站模板
/tags.asp?n=%E6%97%85%E6%B8%B8 旅游网站模板
/tags.asp?n=%E4%BD%93%E8%82%B2 体育网站模板
/tags.asp?n=%E4%BA%A4%E5%8F%8B 交友网站模板
/tags.asp?n=%E7%BE%8E%E5%AE%B9 美容网站模板
/tags.asp?n=%E4%BC%9A%E6%89%80 会所网站模板
/tags.asp?n=%E5%8C%BB%E9%99%A2&n=%E5%8C%BB%E5%AD%A6 医疗网站模板
/tags.asp?n=%E7%BE%8E%E5%AE%B9 美容网站模板
/tags.asp?n=%E5%AE%A0%E7%89%A9&n=%E7%8B%97&n=%E7%8B%97 宠物网站模板
/tags.asp?n=%E6%B1%BD%E8%BD%A6&n=%E8%BD%A6 汽车网站模板
/tags.asp?n=%E5%BB%BA%E7%AD%91 建筑网站模板
/tags.asp?n=%E5%AD%A6%E6%A0%A1 学校网站模板
/tags.asp?n=%E5%92%96%E5%95%A1 咖啡网站模板
/tags.asp?n=%E7%AE%80%E5%8E%86&n=web%E7%AE%80%E5%8E%86 个人简历网站模板
'''

'''
/tags.asp?n=%E4%BC%81%E4%B8%9A,
/tags.asp?n=%E5%95%86%E5%8A%A1,
/tags.asp?n=%E5%8D%9A%E5%AE%A2,
/tags.asp?n=html5
/tags.asp?n=css3
/tags.asp?n=%E6%95%B4%E7%AB%99
/tags.asp?n=%E7%A7%91%E6%8A%80
/tags.asp?n=%E7%94%B5%E8%84%91
/tags.asp?n=%E4%B8%BB%E6%9C%BA&n=%E5%9F%9F%E5%90%8D
/tags.asp?n=%E6%91%84%E5%BD%B1
/tags.asp?n=%E7%9B%B8%E5%86%8C
/tags.asp?n=%E5%A9%9A%E7%BA%B1
/tags.asp?n=%E5%95%86%E5%9F%8E
/tags.asp?n=%E9%A4%90%E9%A5%AE&n=%E9%A4%90%E5%8E%85&n=%E8%A5%BF%E9%A4%90&n=%E7%BE%8E%E9%A3%9F&n=%E9%A3%9F%E5%93%81
/tags.asp?n=%E9%85%92%E5%BA%97
/tags.asp?n=%E6%97%85%E6%B8%B8
/tags.asp?n=%E4%BD%93%E8%82%B2
/tags.asp?n=%E4%BA%A4%E5%8F%8B
/tags.asp?n=%E7%BE%8E%E5%AE%B9
/tags.asp?n=%E4%BC%9A%E6%89%80
/tags.asp?n=%E5%8C%BB%E9%99%A2&n=%E5%8C%BB%E5%AD%A6
/tags.asp?n=%E7%BE%8E%E5%AE%B9
/tags.asp?n=%E5%AE%A0%E7%89%A9&n=%E7%8B%97&n=%E7%8B%97
/tags.asp?n=%E6%B1%BD%E8%BD%A6&n=%E8%BD%A6
/tags.asp?n=%E5%BB%BA%E7%AD%91
/tags.asp?n=%E5%AD%A6%E6%A0%A1
/tags.asp?n=%E5%92%96%E5%95%A1
/tags.asp?n=%E7%AE%80%E5%8E%86&n=web%E7%AE%80%E5%8E%86
'''