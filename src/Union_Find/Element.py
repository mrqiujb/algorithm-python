class Element(object):
    def __init__(self, num):
        self.id = num
        self.parent = -1

    def is_exist(self, i: int) -> bool:
        if self.id == i:
            return True
        else:
            return False

    def set_parent(self, i: int):
        self.parent = i

    def get_parent(self) -> int:
        return self.parent

