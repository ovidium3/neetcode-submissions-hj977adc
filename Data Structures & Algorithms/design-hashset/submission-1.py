class MyHashSet:
    def __init__(self):
        self.size = 8                  # initial bucket count
        self.count = 0                # number of elements
        self.load_factor = 0.75
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def _resize(self):
        old_buckets = self.buckets
        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]

        for bucket in old_buckets:
            for key in bucket:
                h = self._hash(key)
                self.buckets[h].append(key)

    def add(self, key: int) -> None:
        h = self._hash(key)
        bucket = self.buckets[h]

        for k in bucket:
            if k == key:
                return  # already exists

        bucket.append(key)
        self.count += 1

        if self.count / self.size > self.load_factor:
            self._resize()

    def remove(self, key: int) -> None:
        h = self._hash(key)
        bucket = self.buckets[h]

        for i in range(len(bucket)):
            if bucket[i] == key:
                bucket[i] = bucket[-1]
                bucket.pop()
                self.count -= 1
                return

    def contains(self, key: int) -> bool:
        h = self._hash(key)
        bucket = self.buckets[h]

        for k in bucket:
            if k == key:
                return True
        return False