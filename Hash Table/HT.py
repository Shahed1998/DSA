class HashTable:
    def __init__(self, size=53):
        self.keyMap = [None] * size

    def hash(self, key):
        total = 0
        prime = 17
        for i in range(0, min(len(key), 100)):
            char = key[i]
            # gets character position in alphabet table
            value = ord(key[i]) - 96
            total = (total * prime + value) % len(self.keyMap)
        return total  # hashed key

    def set(self, key, value):
        index = self.hash(key)
        # checks whether anything is already stored in the index
        if not self.keyMap[index]:
            self.keyMap[index] = []
        self.keyMap[index].append([key, value])


ht = HashTable()
ht.set("Hello", "World")
ht.set("bye", "World")
print(ht.keyMap)
