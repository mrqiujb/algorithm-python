import random
import time

from Element import Sortable
from Element import Element


class SimpleSort(object):
    def __init__(self, sequence=None):
        # isinstance(a,b) 如果a是b的实例，或者a是b的子类的实例返回true
        # 类似于linq的语句
        # 任何元素x在sequence中 满足不是实例（flase取not为true）或小于0都报异常
        if sequence == None:
            return
        if any(not isinstance(x, Sortable) for x in sequence):
            raise TypeError("Sequence must be can Sortable and id is not of non-negative integers")
        self.elements = sequence
        self.size = len(self.elements)

    def InitElementsByList(self, l):
        if any(not isinstance(x, int) for x in l):
            raise TypeError("Sequence must be can list of integers")
        self.elements = []
        for i in range(0, len(l)):
            self.elements.append(Element(l[i]))
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

    def ShellSort(self):
        # 先划分为n/2组
        gap = int(self.size / 2)
        while gap > 0:
            for i in range(0, gap):  # 划分分组
                for j in range(i + gap, self.size, gap):  # 分组插入排序 找到第二个元素开始
                    index = j
                    for k in range(j - gap, -1, -gap):
                        if self.elements[k].get_weight() > self.elements[index].get_weight():
                            tem = self.elements[k]
                            self.elements[k] = self.elements[index]
                            self.elements[index] = tem
                            index -= gap
                        else:
                            break
            gap = int(gap / 2)

    def Show(self):
        list = []
        for i in range(0, len(self.elements)):
            print(self.elements[i].get_weight(), end=" ")
            list.append(self.elements[i].get_weight())
        print("\n")
        return list

    def SortTest(self, type, n):
        data = random.sample(self.BuildRadomNum(n), n)
        print(data, end='\n')

        if type == 1:  # 希尔排序
            self.InitElementsByList(data)
            self.ShellSort()
        elif type == 2:  # 插入排序
            self.InitElementsByList(data)
            self.InsertSort()
        elif type == 3:  # 选择排序
            self.InitElementsByList(data)
            self.SelectionSort()
        assert self.Show() == self.BuildRadomNum(n)

    def BuildRadomNum(self, n):
        data = []
        for i in range(0, n):

            data.append(i)
        return data


if __name__ == "__main__":
    # 数据量大小
    N = 10
    a = SimpleSort()

    for i in range(0, 100):
        a.SortTest(1, N)
