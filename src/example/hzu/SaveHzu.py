
from src.example.instance.SaveToMysql import save_to_mysql
from src.example.instance.News import SiteClass
from src.example.hzu.GetNewsFromHzu import get_news_from_hzu

# 执行获取并保存数据的操作
save_to_mysql(get_news_from_hzu(), SiteClass.HZU)
