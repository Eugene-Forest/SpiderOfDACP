from src.example.instance.SaveToMysql import save_to_mysql
from src.example.huanqiu.GetNewsFromHuanQiu import get_news_from_huan_qiu, SiteClass,get_important_news_from_huan_qiu


# 执行获取并保存的操作
save_to_mysql(get_news_from_huan_qiu(), SiteClass.HUAN_QUI)
save_to_mysql(get_important_news_from_huan_qiu(),SiteClass.OTHER)
