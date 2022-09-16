# 接口类，排序时根据权重大小调整该元素在list里面的顺序
class Sortable(object):

    def set_weight(self, weight: int) -> bool:
        pass

    def get_weight(self) -> int:
        pass


# 排序元素类，可以添加另外信息变得实用一些，仅需实现如下函数即可
class Element(Sortable):
    def __init__(self, weight: int):
        self.weight = weight

    def get_weight(self) -> int:
        return self.weight

    def set_weight(self, weight: int) -> bool:
        self.weight = weight
        return True
