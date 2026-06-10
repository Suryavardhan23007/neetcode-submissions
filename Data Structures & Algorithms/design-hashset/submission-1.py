class MyHashSet:

    def __init__(self):
        self.size = 1000001
        self.data = [None]*1000001

    def add(self, key: int) -> None:
        self.data[key] = key

    def remove(self, key: int) -> None:
        self.data[key] = None

    def contains(self, key: int) -> bool:
        if self.data[key] != None:
            return True
        else:
            return False
