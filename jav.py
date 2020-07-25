mport datetime
import re
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver
import wget
import os
import urllib.request
import subprocess


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except:
        return None


def mkdir(path):
    # 引入模块
    import os

    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')

        return False


def parse_html(html):
    selector = etree.HTML(html)

    # 目录剔除空格 linux下的目录不一样



    title = selector.xpath('/html/body/div[1]/div[1]/div[5]/h1/text()')
    links = selector.xpath('//*[@id="gallery-2"]/dl/dt/a/@href')
    print(title)
    print(links)
    f_path = "/root/javink/" +"".join(title[0].split())
    fpic_path = "".join(f_path.split())
    mkdir(fpic_path)

    print(fpic_path)
    print(links)
    for one_url in links:
        cmd = 'wget -P {0} {1}'.format(fpic_path, one_url)
        subprocess.call(cmd, shell=True)

        print(cmd)


if __name__ == "__main__":
    all_url = ['https://www.jav.ink/graphis-collection-2002-2018/feti-style-keiko-takashina/',
               'https://www.jav.ink/japanese-av-idols/feti-style/keiko-takashina/',
               'https://www.jav.ink/japanese-av-idols/graphis-gals/anri-okita/',
               'https://www.jav.ink/japanese-av-idols/limited-edition/anri-okita-3/',
               'https://www.jav.ink/japanese-av-idols/limited-edition/anri-okita-4/',
               'https://www.jav.ink/japanese-av-idols/graphis-gals/anri-okita-2/',
               'https://www.jav.ink/graphis-collection-2002-2018/anri-okita-a-trip/',
               'https://www.jav.ink/japanese-av-idols/limited-edition/anri-okita-5/',
               'https://www.jav.ink/japanese-av-idols/special-contents/anri-okita-6/',
               'https://www.jav.ink/graphis-collection-2002-2018/anri-okita-%e6%b2%96%e7%94%b0%e6%9d%8f%e6%a2%a8/',
               'https://www.jav.ink/graphis-collection-2002-2018/anri-okita-%e6%b2%96%e7%94%b0%e6%9d%8f%e9%87%8c-2/',
               'https://www.jav.ink/graphis-collection-2002-2018/anri-okita-a-trip-2/',
               'https://www.jav.ink/graphis-collection-2002-2018/anri-okita-%e6%b2%96%e7%94%b0%e6%9d%8f%e6%a2%a8-nonstandardized/',
               'https://www.jav.ink/graphis-collection-2002-2018/anri-okita-%e6%b2%96%e7%94%b0%e6%9d%8f%e6%a2%a8-console/',
               'https://www.jav.ink/graphis-collection-2002-2018/anri-okita-%e6%b2%96%e7%94%b0%e6%9d%8f%e6%a2%a8-a-trip/',
               'https://www.jav.ink/japanese-av-idols/graphis-gals/ai-sayama-2/',
               'https://www.jav.ink/japanese-av-idols/graphis-gals/ai-sayama/',
               'https://www.jav.ink/japanese-av-idols/special-contents/ai-sayama-4/',
               'https://www.jav.ink/graphis-collection-2002-2018/calendar-ai-sayama/',
               'https://www.jav.ink/japanese-av-idols/limited-edition/ai-sayama-3/',
               'https://www.jav.ink/graphis-collection-2002-2018/ai-sayama-%e4%bd%90%e5%b1%b1%e6%84%9b-white-reflection/',
               'https://www.jav.ink/graphis-collection-2002-2018/ai-sayama-%e4%bd%90%e5%b1%b1%e6%84%9b-adult/',
               'https://www.jav.ink/graphis-collection-2002-2018/ai-sayama-adult/',
               'https://www.jav.ink/graphis-collection-2002-2018/yuria-satomi-%e9%87%8c%e7%be%8e%e3%82%86%e3%82%8a%e3%81%82-foxy-lady/',
               'https://www.jav.ink/graphis-collection-2002-2018/yuria-satomi-%e9%87%8c%e7%be%8e%e3%82%86%e3%82%8a%e3%81%82-pussy-cat/',
               'https://www.jav.ink/japanese-av-idols/graphis-gals/yuria-satomi-2/',
               'https://www.jav.ink/graphis-collection-2002-2018/matsuri-kiritani-%e6%a1%90%e8%b0%b7-%e3%81%be%e3%81%a4%e3%82%8a-%e3%80%8e-primula-julian-%e3%80%8f-5/',
               'https://www.jav.ink/graphis-collection-2002-2018/matsuri-kiritani-%e6%a1%90%e8%b0%b7%e3%81%be%e3%81%a4%e3%82%8a-le-soleil/',
               'https://www.jav.ink/graphis-collection-2002-2018/matsuri-kiritani-%e6%a1%90%e8%b0%b7%e3%81%be%e3%81%a4%e3%82%8a-3/',
               'https://www.jav.ink/graphis-collection-2002-2018/matsuri-kiritani-%e6%a1%90%e8%b0%b7-%e3%81%be%e3%81%a4%e3%82%8a-%e3%80%8e-primula-julian-%e3%80%8f-2/',
               'https://www.jav.ink/graphis-collection-2002-2018/matsuri-kiritani-%e6%a1%90%e8%b0%b7-%e3%81%be%e3%81%a4%e3%82%8a-%e3%80%8e-primula-julian-%e3%80%8f-3/',
               'https://www.jav.ink/graphis-collection-2002-2018/matsuri-kiritani-%e6%a1%90%e8%b0%b7-%e3%81%be%e3%81%a4%e3%82%8a-%e3%80%8e-primula-julian-%e3%80%8f-4/',
               'https://www.jav.ink/graphis-collection-2002-2018/matsuri-kiritani-%e6%a1%90%e8%b0%b7%e3%81%be%e3%81%a4%e3%82%8a/',
               'https://www.jav.ink/graphis-collection-2002-2018/matsuri-kiritani-%e6%a1%90%e8%b0%b7%e3%81%be%e3%81%a4%e3%82%8a-2/',
               'https://www.jav.ink/graphis-collection-2002-2018/matsuri-kiritani-%e6%a1%90%e8%b0%b7-%e3%81%be%e3%81%a4%e3%82%8a-%e3%80%8e-primula-julian-%e3%80%8f/',
               'https://www.jav.ink/japanese-av-idols/special-contents/kanon-ozora/',
               'https://www.jav.ink/graphis-collection-2002-2018/kanon-ozora-%e5%a4%a7%e7%a9%ba-%e3%81%8b%e3%81%ae%e3%82%93-great/',
               'https://www.jav.ink/graphis-collection-2002-2018/haruna-hana-%e6%98%a5%e8%8f%9c%e3%81%af%e3%81%aa-fourth-dimension/',
               'https://www.jav.ink/japanese-av-idols/limited-edition/hana-haruna-2/',
               'https://www.jav.ink/japanese-av-idols/graphis-gals/hana-haruna/',
               'https://www.jav.ink/japanese-av-idols/graphis-gals/riko-honda/',
               'https://www.jav.ink/graphis-collection-2002-2018/ran-niyama-%e6%96%b0%e5%b1%b1%e3%82%89%e3%82%93-amazing-miracle/',
               'https://www.jav.ink/japanese-av-idols/graphis-gals/ran-niyama/',
               'https://www.jav.ink/graphis-collection-2002-2018/early-summer-special-2018-marina-shiraishi-%e7%99%bd%e7%9f%b3%e8%8c%89%e8%8e%89%e5%a5%88/',
               'https://www.jav.ink/graphis-collection-2002-2018/marina-shiraishi-4/',
               'https://www.jav.ink/graphis-collection-2002-2018/early-summer-special-2018-marina-shiraishi-%e7%99%bd%e7%9f%b3%e8%8c%89%e8%8e%89%e5%a5%88-2/',
               'https://www.jav.ink/graphis-collection-2002-2018/marina-shiraishi-%e7%99%bd%e7%9f%b3%e8%8c%89%e8%8e%89%e5%a5%88-baby-face/',
               'https://www.jav.ink/graphis-collection-2002-2018/marina-shiraishi-%e7%99%bd%e7%9f%b3%e8%8c%89%e8%8e%89%e5%a5%88-short-trip/',
               'https://www.jav.ink/graphis-collection-2002-2018/marina-shiraishi-%e7%99%bd%e7%9f%b3%e8%8c%89%e8%8e%89%e5%a5%88-primary-colors/',
               'https://www.jav.ink/japanese-av-idols/graphis-gals/marina-shiraishi-2/',
               'https://www.jav.ink/japanese-av-idols/special-contents/marina-shiraishi-3/',
               'https://www.jav.ink/graphis-collection-2002-2018/marina-shiraishi-%e7%99%bd%e7%9f%b3%e8%8c%89%e8%8e%89%e5%a5%88/',
               'https://www.jav.ink/japanese-av-idols/graphis-gals/marina-shiraishi/']
    for url in all_url:
        html = get_one_page(url)
        parse_html(html)
        time.sleep(10)


