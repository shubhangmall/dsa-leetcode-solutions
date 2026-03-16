from sortedcontainers import SortedList
from collections import deque, defaultdict

# addNumber:              O(log n) — SortedList insert
# removeFirstAddedNumber: O(log n) — SortedList remove
# getMean:                O(1) — running sum divided by count
# getMedian:              O(log n) — SortedList index access
# getMode:                O(log n) — SortedList index access
# space:                  O(n) — storing n elements

class StatisticsTracker:
    def __init__(self):
        # queue to track insertion order for FIFO removal
        self.q = deque()
        # running sum for O(1) mean calculation
        self.s = 0
        # frequency map tracking count of each number
        self.cnt = defaultdict(int)
        # sorted list of all numbers for O(log n) median access
        self.sl = SortedList()
        # sorted list of (number, frequency) pairs
        # sorted by highest frequency first, then smallest number first
        self.sl2 = SortedList(key=lambda x: (-x[1], x[0]))

    def addNumber(self, number: int) -> None:
        # add number to insertion order queue
        self.q.append(number)
        # add number to sorted list
        self.sl.add(number)
        # remove old (number, frequency) pair from mode tracker before updating
        self.sl2.discard((number, self.cnt[number]))
        # increment frequency count for this number
        self.cnt[number] += 1
        # add updated (number, frequency) pair to mode tracker
        self.sl2.add((number, self.cnt[number]))
        # update running sum
        self.s += number

    def removeFirstAddedNumber(self) -> None:
        # get and remove the first added number from queue
        number = self.q.popleft()
        # remove number from sorted list
        self.sl.remove(number)
        # remove old (number, frequency) pair from mode tracker before updating
        self.sl2.discard((number, self.cnt[number]))
        # decrement frequency count for this number
        self.cnt[number] -= 1
        # add updated (number, frequency) pair back to mode tracker
        self.sl2.add((number, self.cnt[number]))
        # update running sum
        self.s -= number

    def getMean(self) -> int:
        # return floor division of sum by count of elements
        return self.s // len(self.q)

    def getMedian(self) -> int:
        # return middle element of sorted list
        # for even count this returns the larger of two middle elements
        return self.sl[len(self.q) // 2]

    def getMode(self) -> int:
        # sl2 is sorted by highest frequency then smallest number
        # so first element is always the current mode
        return self.sl2[0][0]