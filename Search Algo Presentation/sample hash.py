class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        # A simple hash function for demonstration purposes
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            # If the bucket is empty, create a new list
            self.table[index] = [(key, value)]
        else:
            # If the bucket is not empty, append to the existing list
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    # Update the value if the key already exists
                    self.table[index][i] = (key, value)
                    break
            else:
                # If the key doesn't exist in the list, append it
                self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            # Search for the key in the list
            for existing_key, value in self.table[index]:
                if existing_key == key:
                    return value
        # Key not found
        raise KeyError(f"Key '{key}' not found in the hash table")

    def remove(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            # Remove the key from the list if it exists
            self.table[index] = [(existing_key, value) for existing_key, value in self.table[index] if existing_key != key]
        else:
            raise KeyError(f"Key '{key}' not found in the hash table")


# Example usage:
hash_table = HashTable(size=10)

hash_table.insert("one", 1)
hash_table.insert("two", 2)
hash_table.insert("three", 3)

print(hash_table.get("one"))  # Output: 1
print(hash_table.get("two"))  # Output: 2

hash_table.remove("two")

try:
    print(hash_table.get("two"))
except KeyError as e:
    print(e)  # Output: Key 'two' not found in the hash table
