class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.q = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.q:
            return -1
        self.q.move_to_end(key)
        return self.q[key]

    def put(self, key: int, value: int) -> None:
        if key in self.q:
            self.q.move_to_end(key)
        self.q[key] = value
        if len(self.q) > self.capacity:
            self.q.popitem(last=False)
        return
