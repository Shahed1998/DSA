class HashTable:
    def __init__(self, size=7):
        self.keyMap = [None] * size

    def hash(self, key):
        total = 0
        prime = 19
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
        # if duplicate key is inserted overwrite the previous value
        else:
            duplicate = 0
            for i in self.keyMap[index]:
                if i[0] == key:
                    i[1] = value
                    duplicate = 1
            if duplicate == 0:
                self.keyMap[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        if self.keyMap[index]:
            for i in range(len(self.keyMap[index])):
                if self.keyMap[index][i][0] == key:
                    return self.keyMap[index][i][1]
        return None

    def keys(self):
        keys = []
        for i in self.keyMap:
            if i == None:
                continue
            for j in i:
                keys.append(j[0])
        return keys

    def values(self):
        values = []
        for i in self.keyMap:
            if i == None:
                continue
            for j in i:
                if j[1] in values:  # removes duplicate values
                    continue
                values.append(j[1])
        return values


ht = HashTable()
ht.set("Hello", "World 🍻")
ht.set("Hello", "bye 😥")
ht.set("bye", "World 🤞")
print(ht.keys())
print(ht.values())
