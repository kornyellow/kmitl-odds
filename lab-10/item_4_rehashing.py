def main():
    print(" ***** Rehashing *****")
    table_data, hashes = input("Enter Input : ").split("/")
    table_data = list(map(int, table_data.split()))
    hashes = list(map(int, hashes.split()))

    hash_table = Hash(table_data[0], table_data[1], table_data[2])

    print("Initial Table :")
    print(hash_table, end="")

    for h in hashes:
        print("Add : " + str(h))
        hash_table.insert(h)
        print(hash_table, end="")

def next_prime(n):
    prime = 0
    n += 1
    for i in range(2, int(n**0.5)+2):
        if n % i==0:
            prime = 0
            break
        else:
            prime = 1
    if prime == 1:
        return n
    else:
        return next_prime(n)


class Hash:
    def __init__(self, size, max_collision, threshold):
        self.items = 0
        self.size = size
        self.threshold = threshold
        self.max_collision = max_collision
        self.data = []
        for i in range(self.size):
            self.data.append(None)

    def is_full(self):
        return self.size == self.items

    def expand_table(self):
        new_table = []
        new_size = next_prime(self.size * 2)
        for i in range(new_size):
            new_table.append(None)
        old_data = []
        for e in self.data:
            if e != None:
                old_data.insert(0, e)
        self.data = new_table
        self.size = new_size
        self.items = 0
        for e in old_data:
            self.insert(e)

    def insert(self, key, index=-1, iteration=0):
        hash_index = key % self.size
        if iteration > 0:
            hash_index = (hash_index + (iteration*iteration)) % self.size

        if self.data[hash_index] == None:
            self.items += 1
            if self.items / self.size * 100 > self.threshold:
                print("****** Data over threshold - Rehash !!! ******")
                self.expand_table()
                return self.insert(key)
            else:
                self.data[hash_index] = key
        else:
            print("collision number {0} at {1}".format(iteration+1, hash_index))
            if iteration + 1 >= self.max_collision:
                print("****** Max collision - Rehash !!! ******")
                self.expand_table()
                return self.insert(key)
            else:
                return self.insert(key, hash_index, iteration + 1)

    def __str__(self):
        ret = ""
        for i in range(self.size):
            ret += "#" + str(i + 1) + "\t" + str(self.data[i]) + "\n"
        ret += "----------------------------------------\n"
        return ret


if __name__ == "__main__":
    main()
