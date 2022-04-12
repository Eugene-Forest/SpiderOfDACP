from urllib.request import urlopen
from urllib.parse import quote
import json

LINK = "https://api.sou-yun.cn/api/Biography?scope=&author=%E9%AD%8F%E5%BE%81&beginYear=0&endYear=0"

SUSHI = "https://api.sou-yun.cn/api/Biography?scope=&author=%E8%8B%8F%E8%BD%BC&beginYear=0&endYear=0"

BASE_LINK = "https://api.sou-yun.cn/api/Biography?"

Test_LINK = "https://api.sou-yun.cn/api/Biography?scope=当代/灵宝市函谷关&author=苏轼&beginYear=0&endYear=0"

Test = "scope=当代/灵宝市函谷关&author=苏轼&beginYear=0&endYear=0"


def formatUrl(query):
    url = ""
    params = query.split("&")
    for param in params:
        contents = param.split("=")
        url = url + contents[0] + "="
        contents[1] = quote(contents[1])
        url = url + contents[1] + "&"
    return BASE_LINK + url


def get_json(url):
    # 写入文件测试
    # f = open("demofile2.txt", "w", encoding='utf-8')

    response = urlopen(url).read().decode("utf-8")
    print("请求加载完成")
    # f.write("请求加载完成")
    responseJson = json.loads(response)
    print("解析为json完成")
    # f.write("解析为json完成")
    markers = responseJson.get("Traces")[0].get("Markers")
    # 解析第一个
    # detail = markers[0].get("Detail")
    # title = markers[0].get("Title")
    # print(detail)
    # print(title)
    # print("----")
    for marker in markers:
        # 第一个marker detail 解析打印有问题(应当是控制台的缓存不能缓冲这么多的数据)，但是其数据本身没有问题
        detail = marker.get("Detail")
        title = marker.get("Title")
        # 对detail再判断解析
        if detail is None:
            requestUri = marker.get("RequestUri")
            # print(formatUrl(requestUri))
            responseDetail = urlopen(formatUrl(requestUri)).read().decode("utf-8")
            responseDetailJson = json.loads(responseDetail)
            detailMarkers = responseDetailJson.get("Traces")[0].get("Markers")
            print(detailMarkers[0].get("Detail"))
            print(detailMarkers[0].get("Title"))
            # f.write(detailMarkers[0].get("Detail"))
            # f.write(detailMarkers[0].get("Title"))
        else:
            print(detail)
            print(title)
            # f.write(detail)
            # f.write(title)
    # f.close()


if __name__ == '__main__':
    get_json(SUSHI)
    # formatUrl(Test)
