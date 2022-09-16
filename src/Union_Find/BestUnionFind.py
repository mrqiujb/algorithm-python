import Element


class BestUnionFind(object):
    def __init__(self, N: int):
        """
        初始化并查集
        :param N:
        """
        self.ele = []
        self.count = N
        self.sets = N
        self.size = []
        for i in range(0, self.count):
            self.ele.append(Element(i))
            self.size.append(1)

    def find(self, i: int) -> int:
        """
        查找根结点，顺手完成压缩路径
        :param i:
        :return:
        """
        if i < 0 or i > self.count - 1: return False
        point = i
        while self.ele[point].get_parent() != -1:
            point = self.ele[point].get_parent()
        # 在这完成路径压缩，上述循环已经找到了根结点
        # 多进行一次循环，将路径上的元素全部指向根
        root = point
        point = i

        while self.ele[point].get_parent() != -1:
            tem = point
            point = self.ele[point].get_parent()
            self.ele[tem].set_parent(root)
        return root

    def is_connect(self, i: int, j: int) -> bool:
        """
        判断两个结点是否连通
        :param i:
        :param j:
        :return:
        """
        if i > (self.count - 1) or j > (self.count - 1) or i < 0 or j < 0: return False  # 避免越界
        rooti = self.find(i)
        rootj = self.find(j)
        if rooti == rootj and rootj != -1 and rooti != -1:
            return True
        else:
            return False

    def union(self, i: int, j: int) -> bool:
        """
        合并两个连通分量
        :param i:
        :param j:
        :return:
        """
        if i > (self.count - 1) or j > (self.count - 1) or i < 0 or j < 0: return False  # 避免越界
        rooti = self.find(i)
        rootj = self.find(j)
        if self.is_connect(i, j): return True
        # 下面代码并不能完成路径压缩
        # 当两个短树合并时，无论a-》b还是b-》a，都会造成树的层数高于两层
        # 同理size数组就可以丢弃了
        if self.size[i] > self.size[j]:
            self.ele[rooti].parent = rootj
            self.size[rootj] = self.size[rootj] + self.size[rooti]
        else:
            self.ele[rootj].parent = rooti
            self.size[rooti] = self.size[rootj] + self.size[rooti]
        self.sets = self.sets - 1
