class Solution:
    # time: O(n) — single pass right to left through heights
    # space: O(n) — result stores up to n indices in worst case
    def findBuildings(self, heights: List[int]) -> List[int]:
        # handle edge case of single building — always has ocean view
        if len(heights) == 1:
            return [0]
        else:
            # initialize result list to store ocean view building indices
            result = []
            # track the maximum height seen so far scanning right to left
            max_height = 0
            # get the last index to start scanning from
            last_index = len(heights) - 1
            # scan right to left through all buildings
            for i in range(last_index, -1, -1):
                # check if current building is taller than all buildings to its right
                if heights[i] > max_height:
                    # add building index to result
                    result.append(i)
                    # update max height seen so far
                    max_height = heights[i]
            # reverse result to return indices in increasing order
            result.reverse()
            # return all building indices with ocean view
            return result