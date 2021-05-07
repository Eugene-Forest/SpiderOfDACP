# get some information from huanqiu website
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup

from src.example.instance.News import *

# 定义常量凤凰网
IFENG_NEWS_LINK = "https://www.ifeng.com/"
