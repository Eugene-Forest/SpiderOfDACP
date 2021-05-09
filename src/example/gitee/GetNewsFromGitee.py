# get some information from gitee.com/eugene-forest
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 定义主页链接
GITHUB_LINK = "https://gitee.com/eugene-forest/"


def get_news_from_gitee():
    try:
        html = urlopen(GITHUB_LINK)
        bs = BeautifulSoup(html.read(), 'html.parser')
        # 获取新闻链接以及文本
        # todo: 无法直接通过html爬取
        content = bs.find('div', {'class': {'users__contribution'}}) \
            .find('div', {'class': {'contribution-events'}}) \
            .find('div', {'id': {'event-timeline-app'}})
        print(content)
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
    get_news_from_gitee()
