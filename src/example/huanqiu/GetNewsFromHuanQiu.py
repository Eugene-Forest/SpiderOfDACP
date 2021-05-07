# get some information from huanqiu website
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup

from src.example.instance.News import *

# 定义常量环球时报网站
HUANQUI_NEWS_LINK = "https://www.huanqiu.com/"


def get_news_from_huan_qiu():
    """
    获取环球网的要闻的新闻信息集合。

    :return: 一个包含链接和文字的新闻列表。
        若为空，说明该方法需要更新。
    """
    try:
        html = urlopen(HUANQUI_NEWS_LINK)
        bs = BeautifulSoup(html.read(), 'html.parser')
        # 获取新闻链接以及文本
        items = bs.find('div', {'class', 'rightSec'}).find_all('p')
        news_list = []
        for item in items:
            title = item.a.get_text()
            link = item.a['href']
            news = News(title)
            if 'article' not in link:
                news.set_link(link)
            else:
                news = __get_news_content(news, link)
            if news is not None:
                news_list.append(news)
        return news_list
    except AttributeError as e:
        print(e)
        print('某个标签元素不存在 或者url错误(服务器不存在)导致html.read()出错')
        return None
    except HTTPError as e:
        print(e)
        print('The page is not exist or have a error in getting page.')
        return None
    except URLError as e:
        print(e)
        print("url is wrong or the url couldn't open.")
        return None


def get_important_news_from_huan_qiu():
    try:
        html = urlopen(HUANQUI_NEWS_LINK)
        bs = BeautifulSoup(html.read(), 'html.parser')
        # 获取新闻链接以及文本
        items = bs.find('div', {'class', 'conFir'}). \
            find('div', {'class': 'rightFir'}).find_all('dt')
        news_list = []
        for item in items:
            title = item.find('a').get_text()
            link = item.find('a').attrs['href']
            news = News(title)
            if 'article' not in link:
                news.set_link(link)
            else:
                news = __get_news_content(news, link)
            if news is not None:
                news_list.append(news)
        return news_list
    except AttributeError as e:
        print(e)
        print('某个标签元素不存在 或者url错误(服务器不存在)导致html.read()出错')
        return None
    except HTTPError as e:
        print(e)
        print('The page is not exist or have a error in getting page.')
        return None
    except URLError as e:
        print(e)
        print("url is wrong or the url couldn't open.")
        return None


def __get_news_content(news: News, link):
    """
    获取对应新闻实体。如果出错，那么会返回 None。

    :param news: 新闻对象
    :param link: 新闻内容网页链接
    :return: 新闻对象；如果出现网页错误、或其他错误，则返回 None。
    """
    try:
        html = urlopen(link)
        bs = BeautifulSoup(html.read(), 'html.parser')
        # 获取新闻链接以及文本
        content = bs.find('div', {'class': 'container'})
        time = content.find('div', {'class': 't-container'}). \
            find('div', {'class': 'metadata-info'}). \
            find('p', {'class': 'time'}).get_text()
        items = content.find('div', {'class': 'b-container'}). \
            article.find_all('p')
        paragraphs = []
        news.set_publish(time)
        for item in items:
            # 通过捕获来区分图片和文本
            image = item.img
            if image is not None:
                image_link = image.attrs['src']
                if 'http' not in image_link:
                    image_link = 'https:' + image_link
                paragraph = Paragraph(ContentType.IMAGE, image_link)
                # if don't have data-alt?
                alt = ""
                try:
                    alt = image.attrs['data-alt']
                except KeyError:
                    print('do not have the attr which is data-alt')
                if alt is not '':
                    paragraphs.append(paragraph)
                    paragraphs.append(Paragraph(ContentType.TEXT, alt))
                else:
                    paragraph.set_next(False)
                    paragraphs.append(paragraph)
            else:
                text = item.get_text()
                if text is not '':
                    paragraphs.append(Paragraph(ContentType.TEXT, text))
        news.set_paragraphs(paragraphs)
        return news
    except AttributeError as e:
        print(e)
        print('某个标签元素不存在 或者url错误(服务器不存在)导致html.read()出错')
        return None
    except HTTPError as e:
        print(e)
        print('The page is not exist or have a error in getting page.')
        return None
    except URLError as e:
        print(e)
        print("url is wrong or the url couldn't open.")
        return None


if __name__ == '__main__':
    newslist = get_news_from_huan_qiu()
    print(len(newslist))
    print('\n')
    for element in newslist:
        print(element.print_news_content())
