import mysql.connector
from mysql.connector import errorcode

insert_news = ('insert into news '
               '(id,site_class,title,link) '
               'values ("%s","%s","%s","%s")')

insert_detail = ("insert into detail "
                 "(id,nos,type_class,content) "
                 "values (%s,%s,%s,%s)")
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
    # 执行惠州学院的新闻记录的存储
    cursor.execute('insert into news (id,site_class,title,link) '
                   'values (3, 0, "title", "link")')
    print(cursor.fetchone())
    database.commit()
    cursor.execute("select * from news")
    for line in cursor.fetchall():
        print(line)
    # cursor.execute(insert_news, (0, 0, 'title', 'link'))
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    cursor.close()
    database.close()
    print("close mysql")
