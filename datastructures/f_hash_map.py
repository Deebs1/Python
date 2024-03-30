class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h+=ord(char)
        return h % self.MAX

    # def add(self, key, val):
    #     h = self.get_hash(key)
    #     self.arr[h] = val
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val


    # def get(self, key):
    #     h = self.get_hash(key)
    #     return self.arr[h]

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()
print(t.get_hash('march 6'))
# t.add('march 6', 130)
t['march 6'] = 130
t['march 1'] = 23
t['march 3'] = 44
print(t['march 6'])
# print(t.get('march 6'))
del t['march 6']
print(t.arr)