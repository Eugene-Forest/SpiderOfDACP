# 定义 gitee 的动态的数据结构

class Activity:
    """发起人"""
    sponsor = ''

    actions = []


class DynamicState:
    publish = ''

    def __init__(self, publish):
        self.publish = publish
