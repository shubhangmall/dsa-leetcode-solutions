import random 

class RandomizedSet:
    # time: O(1)
    # space: O(n) to maintain inserted n elements
    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
      # return true if val is not in hash map
      if val not in self.numMap:
        self.numMap[val] = len(self.numList)
        self.numList.append(val)
        return True
      # return false if val is in hash map
      if val in self.numMap:
        return False

    def remove(self, val: int) -> bool:
      # return false if val is not in hash map
      if val not in self.numMap:
        return False
      # return true if val is in hash map
      if val in self.numMap:
        # get the index of val from hash map
        i = self.numMap[val]
        # get the last element from list
        lastVal = self.numList[-1]
        # replace val at i with lastVal in list
        self.numList[i] = lastVal
        # remove the last element from list
        self.numList.pop()
        # update list index of last element
        self.numMap[lastVal] = i
        # remove val from hash map
        del self.numMap[val]
        return True

    def getRandom(self) -> int:
      return random.choice(self.numList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()