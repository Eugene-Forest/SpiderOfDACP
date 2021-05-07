import pymysql

insert_news = ('insert into news '
               '(id,site_class,title,link) '
               'values ("%s","%s","%s","%s")')

insert_detail = ("insert into detail "
                 "(id,nos,type_class,content) "
                 "values (%s,%s,%s,%s)")

# 连接数据库
connection = pymysql.connect(
    host="localhost",
    user='root',
    passwd='1244303915',
    database='project_website'
)

with connection:
    # 获取光标
    with connection.cursor() as cursor:
        cursor.execute("select * from news")
        for line in cursor.fetchall():
            print(line)
        cursor.execute("truncate table news")
        # 执行惠州学院的新闻记录的存储
        title = 'test'
        link = 'baidu'
        cursor.execute(insert_news, (6, 1, title, link))
        connection.commit()
        cursor.execute("select * from news")
        for line in cursor.fetchall():
            print(line)
        # cursor.execute(insert_news, (0, 0, 'title', 'link'))
