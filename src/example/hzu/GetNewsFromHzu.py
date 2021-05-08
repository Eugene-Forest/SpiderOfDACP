# get some information from school's website
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup

from src.example.instance.News import *

# 定义常量惠州学院新闻网 https://news.hzu.edu.cn
HZU_NEWS_LINK = "https://news.hzu.edu.cn"


def get_news_from_hzu():
    """
    获取惠州学院新闻网的学校要闻的新闻信息集合。

    :return: 一个包含链接和文字的新闻列表。
        若为空，说明该方法需要更新。
    """
    try:
        html = urlopen(HZU_NEWS_LINK)
        bs = BeautifulSoup(html.read(), 'html.parser')
        # 获取新闻链接以及文本
        items = bs.find('div', {'class': {'post-body'}}) \
            .find('ul', {'class': {'post-news'}}) \
            .findAll('li', {'class': {'xxyw-news-item'}})
        news_list = []
        for item in items:
            # 获取新闻标题以及发布时间等信息
            title = item.a['title']
            link = item.a['href']
            time = item.find('div', {'class': {'xxye-time'}}).get_text()
            # 创建并初始化新闻对象
            news = News(title)
            news.set_publish(time)
            # 判断新闻链接是否完整，如果不完整则补充前缀
            if "http" not in link:
                # print(title)
                news = __get_news_link_content(news, HZU_NEWS_LINK + link)
            else:
                news.set_link(link)
            if news is None:
                continue
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


def __get_news_link_content(news: News, article_url):
    try:
        html = urlopen(article_url)
    except HTTPError as e:
        print(e)
        print('The page is not exist or have a error in getting page.')
        return None
    except URLError as e:
        print(e)
        print("url is wrong or the url couldn't open.")
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        # 获取新闻文章主体
        article = bs.find('div', {'class': 'wp_articlecontent'})
        paragraphs = []
        # 找到主体
        for item in article.find_all('p'):
            # 判断是否为图片部分
            if item.attrs['style'] == 'text-align:center' \
                    or item.attrs['style'] == 'text-align:center;':
                # 该部分依赖网页结构不变才可获取图片链接，否则会报错
                link = item.find('img').attrs['src']
                if 'http' not in link:
                    link = HZU_NEWS_LINK + link
                paragraphs.append(Paragraph(content_type=ContentType.IMAGE, content=link))
            else:
                text = item.get_text()
                if text is '' or None:
                    continue
                else:
                    paragraphs.append(Paragraph(content_type=ContentType.TEXT, content=item.get_text()))
        news.set_paragraphs(paragraphs)
        return news
    except AttributeError as e:
        print(e)
        print('某个标签元素不存在 或者url错误(服务器不存在)导致html.read()出错')
        return None


if __name__ == '__main__':
    newslist = get_news_from_hzu()
    print(len(newslist))
    print('\n')
    for element in newslist:
        print(element.print_news_content())
