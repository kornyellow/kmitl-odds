def main():
    print(" ***** Fun with hashing *****")
    table_data, hashes = input("Enter Input : ").split("/")
    table_data = list(map(int, table_data.split()))
    hashes = hashes.split(",")

    hash_table = Hash(table_data[0], table_data[1])
    for h in hashes:
        hash_table.insert(*h.split())
        print(hash_table, end="")
        if hash_table.is_full():
            print("This table is full !!!!!!")
            break

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


class Hash:
    def __init__(self, size, max_collision):
        self.items = 0
        self.size = size
        self.max_collision = max_collision
        self.data = []
        for i in range(self.size):
            self.data.append(None)

    def is_full(self):
        return self.size == self.items

    def insert(self, key, value, index=-1, iteration=0):
        ascii_sum = 0
        for x in key:
            ascii_sum += ord(x)
        hash_index = ascii_sum % self.size
        if iteration > 0:
            hash_index = (hash_index + (iteration*iteration)) % self.size

        if self.data[hash_index] == None:
            self.items += 1
            self.data[hash_index] = Data(key, value)
        elif iteration < self.max_collision:
            print("collision number {0} at {1}".format(iteration+1, hash_index))
            return self.insert(key, value, hash_index, iteration + 1)
        else:
            print("Max of collisionChain")

    def __str__(self):
        ret = ""
        for i in range(self.size):
            ret += "#" + str(i + 1) + "\t" + str(self.data[i]) + "\n"
        ret += "---------------------------\n"
        return ret


if __name__ == "__main__":
    main()
