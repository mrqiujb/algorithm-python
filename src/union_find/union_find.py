class UnionFind(object):
    def __init__(self, N: int):
        """
        初始化并查集
        :param N: 元素的个数
        """
        self.count = N
        self.sets = N
        self.elements = []
        for i in range(0, N):
            self.elements.append(i)

    def get_count(self) -> int:
        """
        返回当前元素个数
        :return:
        """
        return self.count

    def get_sets(self) -> int:
        """
        返回分量的个数
        :return:
        """
        return self.sets

    def is_connect(self, i: int, j: int) -> bool:
        """
        判断两个元素是否连通
        :param i: 第一个元素的索引
        :param j: 第二个元素的索引
        :return: 布尔值表示是否连通
        """
        if i > (self.count - 1) or j > (self.count - 1): return False  # 避免越界
        if self.elements[i] == self.elements[j]:
            return True
        else:
            return False

    def find(self, i: int) -> int:
        """
        相连通的元素具有相同的标识符
        :param i: i元素
        :return: 标识符
        """
        if i > (self.count - 1): return -1
        return self.elements[i]

    def union(self, i: int, j: int) -> bool:
        """
        合并两个集合
        :param i: 第一个元素
        :param j: 第二个元素
        :return:
        """
        iid = self.find(i)
        jid = self.find(j)
        if iid == jid or iid == -1 or jid == -1: return False
        for k in range(0, self.count):
            if self.elements[k] == jid:
                self.elements[k] = iid
        self.sets = self.sets - 1

    def print_union(self) -> None:
        """
        打印集合

        """
        flags = []
        for i in range(0, self.get_count()):
            flags.append(0)
        for i in range(0, self.get_count()):
            id = self.find(i)
            for j in range(i, self.get_count()):
                if self.elements[j] == id and flags[j] == 0:
                    print("集合：" + str(id) + " element is " + str(j))
                    flags[j] = 1


if __name__ == '__main__':
    u = UnionFind(10)  # 0 1 2 3 4 5 6 7 8 9 10
    # 0 1 2 3 4 5 6 7 8 9 10
    u.union(1, 8)  # 0 1 2 3 4 5 6 7 8 9 10
    # 0 1 2 3 4 5 6 7 1 9 10
    u.union(1, 9)  # 0 1 2 3 4 5 6 7 8 9 10
    # 0 1 2 3 4 5 6 7 1 1 10
    u.union(2, 10)  # 0 1 2 3 4 5 6 7 8 9 10
    # 0 1 2 3 4 5 6 7 1 1 2
    u.union(0, 5)  # 0 1 2 3 4 5 6 7 8 9 10
    # 0 1 2 3 4 0 6 7 1 1 2
    u.union(3, 4)  # 0 1 2 3 4 5 6 7 8 9 10
    # 0 1 2 3 3 0 6 7 1 1 2
    u.union(6, 7)  # 0 1 2 3 4 5 6 7 8 9 10
    # 0 1 2 3 3 0 6 6 1 1 2
    u.print_union()
