class HashTable:
    # Areas of this code are paraphrased from (Lysecky et al., 2018)
    # Creates a hash table with 10 "buckets"
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a "Key, Value" array into the hash table.
    # the "Key" is the value that is hashed then placed in the correct bucket.
    # Average runtime of n/10 and worst case Runtime of O(n) where n in number of packages in hash table
    def insert(self, key, item):
        bucket = int(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Average runtime of n/10 and worst case Runtime of O(n) where n in number of packages in hash table
    # Searches by key, returns the value
    def search(self, key):
        bucket = int(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None
    # Average runtime of n/10 and worst case Runtime of O(n) where n in number of packages in hash table
    # Search by key, removes value from hash table.
    def remove(self, key):
        bucket = int(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
