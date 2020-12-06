#  hashing_table.py Python program that uses remainder method for hashing function and linear probing for rehashing

class HashTable:
    def __init__(self):
        self.size = 11
        #  slots hold the key
        self.slots = [None]*self.size
        #  data holds the corresponding values
        self.data = [None]*self.size

    #  returns the number of items in hashtable
    def __len__(self):
        length = 0
        for i in range(len(self.slots)):
            if self.slots[i] is not None:
                length = length + 1
        return length

    #  returns True if key is in hashtable, otherwise False
    def __contains__(self, item):
        hashvalue = self.hashfunction(item)
        starting_hash = hashvalue
        stop = False
        found = False
        while (self.slots[hashvalue] != None
                and not found
                and not stop):
            if self.slots[hashvalue] == item:
                found = True
            else:
                hashvalue = self.rehash(hashvalue)
                if hashvalue == starting_hash:
                    stop = True
        return found



    def put(self, key, value):
        starting_hash = self.hashfunction(key)
        #  If key is no present in hashing table
        if self.slots[starting_hash] == None:
            self.slots[starting_hash] = key
            self.data[starting_hash] = value
        else:
            #  If key is found, replace previous value with new value
            if self.slots[starting_hash] == key:
                self.data[starting_hash] = value
            else:
                rehashed_value = self.rehash(starting_hash)
                while self.slots[rehashed_value] != key and \
                                self.slots[rehashed_value] != None:
                    rehashed_value = self.rehash(rehashed_value)
                #  When an empty slot is found, fill in key and value
                if self.slots[rehashed_value] == None:
                    self.slots[rehashed_value] = key
                    self.data[rehashed_value] = value
                #  Key is found, replaced the old value with new value
                else:
                    self.data[rehashed_value] = value

    def get(self, key):
        start_position = self.hashfunction(key)
        found = False
        stop = False
        data = None
        position = start_position
        while self.slots[position] != None and \
                        not found and not stop:
            #  Key found, set data equal to the stored value
            if self.slots[position] == key:
                data = self.data[position]
                found = True
            else:
                #  Rehash value and stop when program has iterated through entire table
                position = self.rehash(position)
                if position == start_position:
                    stop = True

        return data

    #  Hashing function based on remainder method
    def hashfunction(self, key):
        return key % self.size

    #  Rehash using linear probing +1
    def rehash(self, oldhash):
        return (oldhash + 1) % self.size

    #  Fills in the corresponding key and value
    def __setitem__(self, key, value):
        self.put(key, value)

    #  Returns value from key
    def __getitem__(self, key):
        return self.get(key)

def test():

    h = HashTable()
    h[50] = 'dog'
    #  key 60, 5, and 16 map to the same slot
    h[60] = 'cat'
    h[5] = 'panda'
    h[16] = 'lion'
    print(h.slots)
    print(len(h))

test()
