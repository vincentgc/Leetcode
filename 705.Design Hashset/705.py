class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Hash = [-1 for i in range(1000000)]
        

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.Hash[key] = 1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.Hash[key] = -1
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.Hash[key] == 1
