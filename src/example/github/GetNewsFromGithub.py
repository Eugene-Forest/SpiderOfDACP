
# get some information from github.com/eugene-forest
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup

from Activity import *

# 定义主页链接
GITHUB_LINK = "https://github.com/Eugene-Forest"


def get_news_from_github():
    try:
        html = urlopen(GITHUB_LINK)
        bs = BeautifulSoup(html.read(), 'html.parser')
        # 获取新闻链接以及文本
        content = bs.find('div', {'class': {'contribution-activity-listing'}})
        time = content.find('span', {'class': {'color-bg-canvas'}}).get_text()
        print(time)
        items = content.find_all('div', {'class': {'TimelineItem '}})
        print(items)
        activity = Activity(time)
        actions = []
        for item in items:
            body = item.find('div', {'class': {'TimelineItem-body '}})
            title = body.find('span', {'class': {'color-text-primary'}}).get_text()
            action = Action(title)
            contributes = []
            contribute_list = body.find('ul')
            for li in contribute_list:
                time = li.find('time')
                if time is None:
                    details = li.find('div').find_all('a')
                    contributes.append(Contribute(details[0].get_text(), details[1].get_text()))
                else:
                    detail = li.find('div').find('a')
                    contributes.append(Contribute(detail.get_text(), time.get_text()))
            action.set_contributes(contributes)
            actions.append(action)
        activity.set_actions(actions)
        return activity
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
    news = get_news_from_github()
    if news is not None:
        news.print_self()
    else:
        print("news is none")
