class ContentType:
    """
    描述新闻段落内容的类
    """

    TEXT = 0
    IMAGE = 1


class SiteClass:
    """
    描述新闻来源的类
    """

    HZU = 0
    HUAN_QUI = 1
    IFENG=2
    OTHER=3


class Paragraph:
    """
    新闻段落内容类
    """

    """作为图片段落的所需的标识，说明下一个内容是否为图片标题，默认是"""
    next_sibling = True

    def __init__(self, content_type: ContentType, content):
        self.content_type = content_type
        self.content = content

    def get_content_type(self):
        return self.content_type

    def get_content(self):
        return self.content

    def set_next(self, brother: bool):
        self.next_sibling = brother

    def get_next(self):
        return self.next_sibling

    def set_content_type(self, content_type: ContentType):
        self.content_type = content_type

    def set_content(self, content):
        self.content = content


class News:
    """
    一个新闻对象，存储新闻标题信息以及具体内容，并存储外链图片；当新闻链接为空字符串时，
    该新闻对象是一个存有文章；当新闻链接不为空时，该新闻对象是一个外链新闻。
    """

    """文章段落组"""
    paragraphs = []

    """新闻详细介绍链接"""
    pageLink = ""

    """新闻标题"""
    title = ""

    """新闻发布时间"""
    publish = ""

    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_publish(self):
        return self.publish

    def set_publish(self, publish):
        self.publish = publish

    def push_paragraph(self, paragraph: Paragraph):
        self.paragraphs.append(paragraph)

    def pop_paragraph(self):
        return self.paragraphs.pop()

    def get_link(self):
        return self.pageLink

    def set_link(self, link):
        self.pageLink = link

    def set_paragraphs(self, paragraphs):
        self.paragraphs = paragraphs[:]

    def get_paragraphs(self):
        return self.paragraphs[:]

    def print_news_content(self):
        print("Title :" + self.title)
        print("Time : " + self.publish)
        print("Hyperlink : " + self.pageLink)
        print("Here is article".center(30, '-'))
        for paragraph in self.paragraphs:
            print(paragraph.get_content())
        print("".center(30, '-'))
