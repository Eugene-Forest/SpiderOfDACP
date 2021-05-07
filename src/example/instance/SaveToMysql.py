import mysql.connector
from mysql.connector import errorcode

from src.example.hzu.GetNewsFromHzu import get_news_from_hzu
from src.example.instance.News import ContentType, SiteClass

insert_news = ('replace into news '
               '(id,site_class,title,publish,link) '
               'values (%s,%s,%s,%s,%s)')

insert_detail = ("replace into detail "
                 "(site_class,id,nos,type_class,content) "
                 "values (%s,%s,%s,%s,%s)")


def save_to_mysql(news_list, site_type: SiteClass):
    """
    将新闻列表保存到数据库中

    :param site_type: 新闻来源
    :param news_list: 新闻列表
    """
    try:
        # 连接数据库
        database = mysql.connector.connect(
            host="localhost",
            user='root',
            passwd='1244303915',
            database='project_website'
        )
        # 获取光标
        cursor = database.cursor()
        # 清空数据
        # cursor.execute("truncate table news")
        # cursor.execute("truncate table detail")
        # 定义新闻id标识
        i = 0
        # 开始循环插入新闻记录
        for news in news_list:
            # 获取新闻标题和链接
            title = news.get_title()
            link = news.get_link()
            time = news.get_publish()
            # 执行惠州学院的新闻记录的存储
            cursor.execute(insert_news, (i, site_type, title, time, link))
            # 判断当前新闻是否是外链新闻，如果不是则继续处理
            if link is '':
                # 定义新闻内容段落标识
                j = 0
                # 获取新闻的内容列表
                contents = news.get_paragraphs()
                # 循环存入数据库
                for paragraph in contents:
                    cursor.execute(insert_detail,
                                   (site_type, i, j, paragraph.get_content_type(), paragraph.get_content()))
                    # 判断段落兄弟标识判度是否自增段落数
                    if paragraph.get_next() is True:
                        j = j + 1
            # id自增
            i = i + 1
        # 提交更改
        database.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor.close()
        database.close()
        print("close mysql")


if __name__ == '__main__':
    save_to_mysql(get_news_from_hzu(), SiteClass.HZU)
