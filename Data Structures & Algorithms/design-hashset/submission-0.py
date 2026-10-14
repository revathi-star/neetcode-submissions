class MyHashSet:

    def __init__(self):
        super().__init__()
        self.l=[]

    def add(self, key: int) -> None:
        if key not in self.l:
            self.l.append(key)

    def remove(self, key: int) -> None:
        for i,v in enumerate(self.l):
            if v==key:
                self.l.pop(i)
        # if type(self.l) == int:
        #     self.l = [(self.l)]

    def contains(self, key: int) -> bool:
        return key in self.l


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)