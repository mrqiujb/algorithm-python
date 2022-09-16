from Element import Sortable
from Element import Element


class SimpleSort(object):
    def __init__(self, sequence):
        # isinstance(a,b) 如果a是b的实例，或者a是b的子类的实例返回true
        # 类似于linq的语句
        # 任何元素x在sequence中 满足不是实例（flase取not为true）或小于0都报异常
        if any(not isinstance(x, Sortable) for x in sequence):
            raise TypeError("Sequence must be can Sortable and id is not of non-negative integers")
        self.elements = sequence
        self.size = len(self.elements)

    # 选择排序两个特点
    # 运行时间与输入无关 为0n2 交换次数为n 比较次数为n-1-i n-1 + n-2 + n-3 + ... + 1 =n(n-1)/2
    # 移动次数最少 n次移动
    def SelectionSort(self, desc: bool = True) -> bool:
        size = len(self.elements)
        for i in range(0, self.size):
            point = i
            min_weight_index = i
            for j in range(i + 1, self.size):
                if self.elements[j].get_weight() < self.elements[min_weight_index].get_weight():
                    min_weight_index = j
            tem = self.elements[min_weight_index]
            self.elements[min_weight_index] = self.elements[point]
            self.elements[point] = tem

    def InsertSort(self, desc: bool = True) -> bool:
        order_last = 0
        for i in range(1, self.size):
            index = i
            for j in range(0, i + 1):
                if self.elements[j].get_weight() > self.elements[index].get_weight():
                    tem = self.elements[index]
                    for k in range(i, j - 1, -1):
                        self.elements[k] = self.elements[k - 1]
                    self.elements[j] = tem

    def Show(self):
        list = []
        for i in range(0, len(self.elements)):
            print(self.elements[i].get_weight(), end=" ")
            list.append(self.elements[i].get_weight())
        return list

    def SelectionSoortTest(self, list):
        assert self.Show() == list


if __name__ == "__main__":
    list = []
    list.append(Element(5))
    list.append(Element(9))
    list.append(Element(2))
    list.append(Element(4))
    list.append(Element(7))
    list.append(Element(0))
    list.append(Element(8))
    list.append(Element(6))
    list.append(Element(10))
    list.append(Element(3))
    list.append(Element(1))
    a = SimpleSort(list)
    a.InsertSort()
    a.SelectionSoortTest([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
